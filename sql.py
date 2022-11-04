import sqlite3


def add_user(data):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.execute(f'INSERT INTO users (firstname, lastname, e_mail, phone_number, birth_date, chat_id, screenshot_adr, status, extra_info) VALUES {data}')
    connect.commit()
    cursor.close()


# change user status: 1 - means screenshot is already sent
def change_status(user_id):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.execute(f'UPDATE users SET status = 1 WHERE id = {user_id}')
    connect.commit()
    cursor.close()


change_status(7)

# item = ('firstname', 'lastname', 'e_mail', 'phone_number', 'birth_date', 'chat_id', 'screenshot_addr', 'status', 'extra_info')
# add_user(item)
