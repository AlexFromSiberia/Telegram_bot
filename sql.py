import sqlite3


def add_user(data):
    """
    Adds information abut a new user into the database
    """
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.execute(f'INSERT INTO users (id, firstname, lastname, e_mail, phone_number, birth_date, chat_id, screenshot_adr, status, extra_info) VALUES {data}')
    connect.commit()
    cursor.close()


def change_status(user_id):
    """
    Changes user status: '1' - means screenshot is already sent
    """
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    cursor.execute(f'UPDATE users SET status = 1 WHERE id = {user_id}')
    connect.commit()
    cursor.close()
#change_status(7)


def get_user_data():
    """
    looks in database for a user with status = "0",
    with min id value (min id means the user is first in the que
    for registration) Next step: register this user.
    :return: user data , tuple:
    ('id', 'firstname', 'lastname', 'e_mail', 'phone_number', 'birth_date', 'chat_id', 'screenshot_addr', 'status')
    or '0' if all users with status '1' already.
    """
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    t = cursor.execute('SELECT * FROM users WHERE status = 0 ORDER by id LIMIT 1')
    try:
        user_data = list(t)[0][:-1]
        cursor.close()
        return user_data
    except:
        return 0


