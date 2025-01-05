import React, { useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import './Chat.css'; // Import the CSS file

const Chat = () => {
    const { t } = useTranslation();
    const [messages, setMessages] = useState([]);
    const [messageInput, setMessageInput] = useState('');
    const [isSending, setIsSending] = useState(false);
    const chatWindowRef = useRef(null);

    useEffect(() => {
        if (chatWindowRef.current) {
            chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
        }
    }, [messages]);

    const sendMessage = async () => {
        const message = messageInput.trim();
        if (!message) return;

        setIsSending(true);
        setMessages((prevMessages) => [...prevMessages, { sender: 'user', text: message, time: new Date().toLocaleTimeString() }]);
        setMessageInput('');

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message }),
            });

            if (!response.ok) {
                throw new Error('Ошибка при отправке сообщения');
            }

            const data = await response.json();
            setMessages((prevMessages) => [...prevMessages, { sender: 'bot', text: data.response, time: new Date().toLocaleTimeString() }]);
        } catch (error) {
            console.error("Error sending message:", error);
            setMessages((prevMessages) => [...prevMessages, { sender: 'bot', text: t('error'), time: new Date().toLocaleTimeString() }]);
        } finally {
            setIsSending(false);
        }
    };

    const handleInputChange = (e) => {
        setMessageInput(e.target.value);
    };

    const handleInputKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div className="chat-container">
            <h2 className="text-center mb-4">{t('title')}</h2>
            <div className="chat-window" id="chat-window" ref={chatWindowRef}>
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender === 'user' ? 'user-message' : 'bot-message'}`}>
                        <strong>{msg.sender === 'user' ? `${t('user')}` : `${t('bot')}`}</strong> ({msg.time}): {msg.text}
                    </div>
                ))}
            </div>
            <div className="input-group">
                <input
                    type="text"
                    className="form-control"
                    id="message-input"
                    placeholder={t('placeholder')}
                    value={messageInput}
                    onChange={handleInputChange}
                    onKeyPress={handleInputKeyPress}
                    disabled={isSending}
                />
                <button
                    className="btn btn-primary"
                    id="send-button"
                    onClick={sendMessage}
                    disabled={isSending}
                >
                    {isSending ? t('sending') : t('send')}
                </button>
            </div>
        </div>
    );
};

export default Chat;