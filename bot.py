

# The first message
@bot.message_handler(commands=['start'])
def start(message):
    img = open('static/welcome.png', 'rb')
    # bot.send_photo(message.chat.id, img)

    # buttons
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Ok")
    # item2 = types.KeyboardButton("Начать с начала")
    # markup.add(item1, item2)
@bot.process_new_messages(new_messages=[1])
    bot.send_message(message.chat.id, 'Приветствую Моё имя {bot.get_me().first_name}',
                    parse_mode='html', reply_markup=markup)









