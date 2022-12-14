import datetime
import config
import requests
import re


def screenshot_adr():
    """
    Creates file name for a screenshot in format «YYYY-MM-DD_HH:mm_<user id>.jpg»
    """
    t = str(datetime.datetime.now())
    date = t[:10]+'_'+t[11:16]+'_'
    return config.screenshots_dir + date


def send_link(chat_id, link):
    """
    Sends the screenshot link to the User,
    using api Telegram: send request to url:
    https://api.telegram.org/bot{token}{api_method}?chat_id={id}&text={text}
    """
    text = f'Ссылка на скриншот об успешной регистрации: {config.prefix}{link}'
    token = config.Token
    api = 'https://api.telegram.org/bot'
    api_method = '/sendMessage'
    method = api + token + api_method
    req = requests.post(method, data={'chat_id': chat_id, 'text': text})


def emailErrorMessage(chat_id):
    """
    Sends email Error Messagethe
    """
    text = f'Email указан не верно. Заполните данные повторно'
    token = config.Token
    api = 'https://api.telegram.org/bot'
    api_method = '/sendMessage'
    method = api + token + api_method
    req = requests.post(method, data={'chat_id': chat_id, 'text': text})


def email_check(email):
    """
    Email validator
    """
    if re.compile(r"[^@]+@[^@]+\.[^@]+").match(email):
        return True
    else:
        return False


