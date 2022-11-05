import telebot
from telebot import types
import config
from sql import add_user

API_TOKEN = config.Token
bot = telebot.TeleBot(API_TOKEN)
user_dict = {}


# Here stores all user's data we need for registration
class User:
    def __init__(self, firstname):
        self.firstname = firstname
        self.lastname = None
        self.e_mail = None
        self.phone_number = None
        self.birth_date = None


# Allows the bot to say Hallo to User
@bot.message_handler(commands=['start', ])
def start(message):
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}! '
                                      f'Я помогу Вам выполнить регистрацию.'
                                      f'Чтобы избежать ошибок, сделаем всё по этапам.'
                                      f'А если всё равно ошиблись - введите: /start')
    # asking for name add launch next step --> process_firstname
    msg = bot.reply_to(message, 'Введите Ваше имя')
    bot.register_next_step_handler(msg, process_firstname)


# next question and launch next step --> process_lastname
def process_firstname(message):
    try:
        chat_id = message.chat.id
        firstname = message.text
        user = User(firstname)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Ваша фамилия?')
        bot.register_next_step_handler(msg, process_lastname)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Пожалуйста начните с начала')


def process_lastname(message):
    try:
        chat_id = message.chat.id
        lastname = message.text
        user = user_dict[chat_id]
        user.lastname = lastname
        msg = bot.reply_to(message, 'Ваш Email?')
        bot.register_next_step_handler(msg, process_e_mail)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Пожалуйста начните с начала')


def process_e_mail(message):
    try:
        chat_id = message.chat.id
        e_mail = message.text
        user = user_dict[chat_id]
        user.e_mail = e_mail
        msg = bot.reply_to(message, 'Номер телефона?')
        bot.register_next_step_handler(msg, process_phone_number)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Пожалуйста начните с начала')


def process_phone_number(message):
    try:
        chat_id = message.chat.id
        phone_number = message.text
        user = user_dict[chat_id]
        user.phone_number = phone_number
        msg = bot.reply_to(message, 'Дата рождения в фоормате дд.мм.гггг?')
        bot.register_next_step_handler(msg, process_birth_date)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Пожалуйста начните с начала')


def process_birth_date(message):
    try:
        chat_id = message.chat.id
        birth_date = message.text
        user = user_dict[chat_id]
        user.birth_date = birth_date
        bot.send_message(chat_id, f'Проверим: {user.firstname} {user.lastname}, {user.e_mail}, {user.phone_number}, '
                                  f'{user.birth_date}')
        print('user_dict', user_dict)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Пожалуйста начните с начала')

    # checking if we have all the data we need for now:
    if user.firstname and user.lastname and user.e_mail and user.phone_number and user.birth_date :
        data = (user.firstname,
                user.lastname,
                user.e_mail,
                user.phone_number,
                user.birth_date,
                chat_id,
                'screenshot_adr',
                '0',
                'extra_info')
        # sql.add_user(data) - write data to the data base
        add_user(data)


# Run the program
if __name__ == '__main__':
    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers(delay=2)
    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()
    bot.infinity_polling()
