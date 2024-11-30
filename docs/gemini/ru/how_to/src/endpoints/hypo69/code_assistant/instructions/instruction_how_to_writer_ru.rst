Как использовать функцию проверки валидности email
==========================================================================================

Описание
-------------------------
Функция проверяет корректность введённого email адреса, используя библиотеку `email_validator`. Она возвращает True, если адрес валидный, и False, если нет.  Возможные ошибки содержатся в атрибуте `errors`.

Шаги выполнения
-------------------------
1. Импортируйте функцию `validate_email` из модуля `email_validator`.
2. Передайте строку с email адресом в функцию `validate_email` как аргумент.
3. Функция вернёт `True` если email валиден, или `False` - в противном случае.  Атрибут `errors` содержит информацию об ошибках, если они есть.

Пример использования
-------------------------
.. code-block:: python

    from email_validator import validate_email, EmailNotValidError

    email_address = "test@example.com"

    try:
        validated_email = validate_email(email_address)
        print(f"Email '{email_address}' является валидным: {validated_email.email_valid}")
    except EmailNotValidError as e:
        print(f"Ошибка при проверке email '{email_address}': {e}")

    email_address_invalid = "invalid-email"

    try:
        validated_email = validate_email(email_address_invalid)
        print(f"Email '{email_address_invalid}' является валидным: {validated_email.email_valid}")
    except EmailNotValidError as e:
        print(f"Ошибка при проверке email '{email_address_invalid}': {e}")

    print(f"Ошибки: {validated_email.errors}") # Печать ошибок, если email не валиден