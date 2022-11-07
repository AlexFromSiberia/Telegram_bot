
# Telegram бот, который заполняет форму обратной связи за человека.

---

## Не решённые баги:
- Метод Selenium send_keys отправляет в форму только латиницу. Для кириллицы поле остаётся пустым. Кодировать в utf-8 принудительно не решает проблему. Возможно что-то с моим веб драйвером Chrome.

---

## Что бот умеет :
1. Запрашивает данные пользователя для заполненя формы (имя, фамилия, email, телефон, дата рождения)
2. Записывает все данные пользователя и ставит его в очередь (базе данных формируется список пользователей)
3. Проверяет доступность формы с переодичностью 1 раз в 10 минут 
4. Заполняет форму
5. После сохраняется скриншот экрана успешной отправки формы и ссылку на скриншот отправляет в чат пользователю

## Реализация:
1. Язык Python
2. Картинки пользователя бот сохраняет в папку (путь до неё настраивается) с именем в формате «YYYY-MM-DD_HH:mm_<user id>.jpg».

---

# Установка и запуск:
- Установить requirements
- Задать конфигурацию (необходимые настройки в config.py)
- Для работы также необходимо установить wed драйвер для браузера (и сам браузер если такой не установлен):
  Доп информация здесь:
  Selenium library installation guide + webdriver  here:
  https://selenium-python.readthedocs.io/getting-started.html

  Download your web driver :
  Chrome:	https://sites.google.com/chromium.org/driver/
  Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
  Firefox:	https://github.com/mozilla/geckodriver/releases
  Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
- Запустить main.py
