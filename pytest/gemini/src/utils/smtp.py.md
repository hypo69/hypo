```python
import pytest
import smtplib
import imaplib
import os
from email.mime.text import MIMEText
from unittest.mock import patch, mock_open
from src.utils import smtp
from src.logger.logger import logger
import logging


# Fixture to simulate environment variables
@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("SMTP_SERVER", "smtp.testserver.com")
    monkeypatch.setenv("SMTP_PORT", "587")
    monkeypatch.setenv("SMTP_USER", "testuser")
    monkeypatch.setenv("SMTP_PASSWORD", "testpassword")
    monkeypatch.setenv("SMTP_RECEIVER", "testreceiver@example.com")

# Fixture to simulate successful SMTP connection
@pytest.fixture
def mock_smtp_success():
    with patch("smtplib.SMTP") as MockSMTP:
        instance = MockSMTP.return_value
        instance.starttls.return_value = (220, "2.0.0 Ready to start TLS")
        instance.login.return_value = (235, "2.7.0 Authentication successful")
        instance.sendmail.return_value = {}
        instance.quit.return_value = None
        yield MockSMTP

# Fixture to simulate failed SMTP connection
@pytest.fixture
def mock_smtp_failure():
    with patch("smtplib.SMTP") as MockSMTP:
        instance = MockSMTP.return_value
        instance.starttls.side_effect = smtplib.SMTPException("Failed to connect")
        yield MockSMTP
        
# Fixture to simulate a successful IMAP connection
@pytest.fixture
def mock_imap_success():
    with patch("imaplib.IMAP4_SSL") as MockIMAP:
        instance = MockIMAP.return_value
        instance.login.return_value = ('OK', [b'testuser authenticated'])
        instance.select.return_value = ('OK', [b'1'])
        instance.search.return_value = ('OK', [b'1 2'])
        instance.fetch.side_effect = [
            ('OK', [(b'1', b'Subject: Test Subject\nFrom: test@example.com\n\nTest body'),]),
            ('OK', [(b'2', b'Subject: Test Subject 2\nFrom: test2@example.com\n\nTest body 2'),])
        ]
        instance.close.return_value = None
        instance.logout.return_value = None
        yield MockIMAP

# Fixture to simulate a failed IMAP connection
@pytest.fixture
def mock_imap_failure():
    with patch("imaplib.IMAP4_SSL") as MockIMAP:
        instance = MockIMAP.return_value
        instance.login.side_effect = imaplib.IMAP4.error("Login failed")
        yield MockIMAP


# Test cases for the send function
def test_send_valid_email(mock_env_vars, mock_smtp_success):
    """Checks correct behavior with valid email details."""
    assert smtp.send(subject="Test Subject", body="Test Body", to="testreceiver@example.com") is True
    mock_smtp_success.return_value.login.assert_called_with("testuser", "testpassword")
    mock_smtp_success.return_value.sendmail.assert_called()

def test_send_default_receiver(mock_env_vars, mock_smtp_success):
    """Checks email is sent with the default receiver when no recipient specified."""
    assert smtp.send(subject="Test Subject", body="Test Body") is True
    mock_smtp_success.return_value.sendmail.assert_called()

def test_send_email_failure(mock_env_vars, mock_smtp_failure, caplog):
    """Checks correct handling of email sending failure."""
    caplog.set_level(logging.ERROR)
    assert smtp.send(subject="Test Subject", body="Test Body", to="testreceiver@example.com") is False
    assert "Error sending email" in caplog.text

def test_send_email_empty_subject_and_body(mock_env_vars, mock_smtp_success):
    """Checks email is sent correctly with an empty subject and body."""
    assert smtp.send(to="testreceiver@example.com") is True
    mock_smtp_success.return_value.sendmail.assert_called()
    
def test_send_email_exception_during_login(mock_env_vars, caplog):
    """Checks handling of login error"""
    caplog.set_level(logging.ERROR)
    with patch("smtplib.SMTP") as MockSMTP:
        instance = MockSMTP.return_value
        instance.ehlo.return_value = (250, "server.com")
        instance.starttls.return_value = (220, "2.0.0 Ready to start TLS")
        instance.login.side_effect = smtplib.SMTPAuthenticationError(535, "Authentication failed")
        assert smtp.send(subject="Test Subject", body="Test Body", to="testreceiver@example.com") is False
    assert "Error sending email" in caplog.text

# Test cases for the receive function
def test_receive_valid_emails(mock_imap_success, mock_env_vars):
    """Checks correct behavior when retrieving emails."""
    emails = smtp.receive(imap_server="imap.testserver.com", user="testuser", password="testpassword")
    assert emails is not None
    assert len(emails) == 2
    assert emails[0]['subject'] == 'Test Subject'
    assert emails[0]['from'] == 'test@example.com'
    assert emails[0]['body'] == 'Test body'
    assert emails[1]['subject'] == 'Test Subject 2'
    assert emails[1]['from'] == 'test2@example.com'
    assert emails[1]['body'] == 'Test body 2'

def test_receive_no_emails(mock_env_vars):
    """Checks correct behavior when no emails are found"""
    with patch("imaplib.IMAP4_SSL") as MockIMAP:
        instance = MockIMAP.return_value
        instance.login.return_value = ('OK', [b'testuser authenticated'])
        instance.select.return_value = ('OK', [b'1'])
        instance.search.return_value = ('OK', [b''])
        instance.close.return_value = None
        instance.logout.return_value = None
        emails = smtp.receive(imap_server="imap.testserver.com", user="testuser", password="testpassword")
        assert emails == []
        
def test_receive_imap_failure(mock_env_vars, mock_imap_failure, caplog):
    """Checks correct handling of IMAP connection failure."""
    caplog.set_level(logging.ERROR)
    emails = smtp.receive(imap_server="imap.testserver.com", user="testuser", password="testpassword")
    assert emails is None
    assert "Error occurred while retrieving emails" in caplog.text
    
def test_receive_login_failure(mock_env_vars, caplog):
    """Checks the handling of IMAP login failure"""
    caplog.set_level(logging.ERROR)
    with patch("imaplib.IMAP4_SSL") as MockIMAP:
        instance = MockIMAP.return_value
        instance.login.side_effect = imaplib.IMAP4.error("Login failed")
        emails = smtp.receive(imap_server="imap.testserver.com", user="testuser", password="testpassword")
        assert emails is None
        assert "Error occurred while retrieving emails" in caplog.text
        
def test_receive_select_failure(mock_env_vars, caplog):
    """Checks the handling of IMAP mailbox selection failure"""
    caplog.set_level(logging.ERROR)
    with patch("imaplib.IMAP4_SSL") as MockIMAP:
        instance = MockIMAP.return_value
        instance.login.return_value = ('OK', [b'testuser authenticated'])
        instance.select.side_effect = imaplib.IMAP4.error("Cannot select mailbox")
        emails = smtp.receive(imap_server="imap.testserver.com", user="testuser", password="testpassword")
        assert emails is None
        assert "Error occurred while retrieving emails" in caplog.text
        
def test_receive_decode_error(mock_env_vars, caplog):
    """Checks the handling of email decoding error"""
    caplog.set_level(logging.ERROR)
    with patch("imaplib.IMAP4_SSL") as MockIMAP:
        instance = MockIMAP.return_value
        instance.login.return_value = ('OK', [b'testuser authenticated'])
        instance.select.return_value = ('OK', [b'1'])
        instance.search.return_value = ('OK', [b'1'])
        instance.fetch.return_value = ('OK', [(b'1', b'Subject: Test Subject\nFrom: test@example.com\n\nTest body\xc3\xb1'),])
        instance.close.return_value = None
        instance.logout.return_value = None
        emails = smtp.receive(imap_server="imap.testserver.com", user="testuser", password="testpassword")
        assert emails is not None
        assert len(emails) == 1
        assert emails[0]['body'] == "Test body\ufffd"
```