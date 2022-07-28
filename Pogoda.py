import telebot
from telebot import types
from pyowm import OWM
import config
# установка бибилиотеки для работы с телеграмм
# через запрос в терминале pip install pyTelegramBotAPI
# импорт библиотеки для работы в телеграмме
# импорт функци прогноза погоды
# находим в телеграмме главаря всех ботов
# регистрируем своего бота, и присваевыем ему имя
# указываем к какому боту нужно обращатся (указыываем токен)
bot = telebot.TeleBot(config.Token)
# Создаем декоратор
@bot.message_handler(commands = ['start'])
# Создаем  функцию, обрабатывающюю команды
def start(message):
  username = f'Привет, <b>{message.from_user.first_name}</b>'
  # f в начале строки означает, что строка будет форматииованной, можно использовать вместо сложения строк
  # <b>&</b> отвечают за жирный текст
  # открываем файл c приветвеным фото
  hello = open('hihihi.png', 'rb')
# Режим открытия файла - read binary(без него не отправляет фото в телеграмм)
  bot.send_photo(message.chat.id, hello)
  bot.send_message(message.chat.id,username, parse_mode='html')
  bot.send_message(message.chat.id,"Если хочешь поболтать, напиши 'Привет'. Если хочешь узнать актуальный прогноз погоды напиши 'Погода' ", parse_mode='html')
# За выбор форматирования при отправке сообщений отвечает аргумент parse_mode(у меня работает, толькое сли указыввать HTML)

# создаем новую функцию, для отслеживания текста пользователя и привнесем веселья
@bot.message_handler(content_types=['text'])
def user_text(message):
  if message.text == 'Привет':
     bot.send_message(message.chat.id, "Привет, как твои дела?", parse_mode='html')
  elif message.text == 'Хорошо'or message.text== 'Нормально'or message.text== 'Отлично'or message.text== 'Замечательно'or message.text== 'Превосходно':
     bot.send_message(message.chat.id, "Я рад за тебя, продолжай в том же духе!", parse_mode='html')
  elif message.text == 'Плохо'or message.text== 'Отстой'or message.text== 'Не очень'or message.text== 'Ужасно'or message.text== 'Отвратительно':
    bot.send_message(message.chat.id, "Хочешь повеселю тебя?", parse_mode='html')
  elif message.text == 'Нет'or message.text== 'Не хочу'or message.text== 'Ноу'or message.text== 'Нет, спасибо':
    bot.send_message(message.chat.id, "Ну и ладно, не очень то и хотелось ...", parse_mode='html')
  elif message.text == 'Да'or message.text== 'Хочу'or message.text== 'Да, конечно'or message.text== 'А почему бы и нет'or message.text== 'Давай':
    bot.send_message(message.chat.id, "Введи команду Шутка 1 - Шутка 8", parse_mode='html')
  elif message.text == 'Шутка 1':
    jk1 = open('187254_original.jpg', 'rb')
    bot.send_photo(message.chat.id, jk1)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши Стоп ", parse_mode='html')
  elif message.text == 'Шутка 2':
    jk2 = open('187539_original.jpg','rb')
    bot.send_photo(message.chat.id, jk2)
    bot.send_message(message.chat.id, "Хочешь еще? Или перейдем к информации?", parse_mode='html')
  elif message.text == 'Шутка 3':
    jk4 = open('developer10.jpeg', 'rb')
    bot.send_photo(message.chat.id, jk4)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши Стоп ", parse_mode='html')
  elif message.text == 'Шутка 4':
    jk5 = open('screenshot_20201125-173523__01-1024x1010.jpg', 'rb')
    bot.send_photo(message.chat.id, jk5)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши Стоп ", parse_mode='html')
  elif message.text == 'Шутка 5':
    jk6 = open('screenshot_20201125-173620__01-1024x991.jpg', 'rb')
    bot.send_photo(message.chat.id, jk6)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши Стоп ", parse_mode='html')
  elif message.text == 'Шутка 6':
    jk7 = open('screenshot_20201125-173626__01-1024x876.jpg', 'rb')
    bot.send_photo(message.chat.id, jk7)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши Стоп ", parse_mode='html')
  elif message.text == 'Шутка 7':
    jk8 = open('screenshot_20201125-173710__01-868x1024.jpg', 'rb')
    bot.send_photo(message.chat.id, jk8)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши Стоп ", parse_mode='html')
  elif message.text == 'Шутка 8':
    jk9 = open('screenshot_20201125-174012__01-925x1024.jpg', 'rb')
    bot.send_photo(message.chat.id, jk9)
    bot.send_message(message.chat.id, "Продолжим?Если нет, напиши 'Стоп' ", parse_mode='html')
  elif message.text == 'Стоп':
    bot.send_message(message.chat.id, "Ээээээ, в смысле СТОП, я так старалась искать мемасики, а ну все досмотри! ", parse_mode='html')
  elif message.text == 'Погода':
    bot.send_message(message.from_user.id, text='Выбери свой город', reply_markup=markup)
  else:
    bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


# Создаем копки
markup=types.InlineKeyboardMarkup()
# # И добавляем кнопку на экран
minsk = types.InlineKeyboardButton('Минск', callback_data='Минск')
markup.add(minsk)
brest = types.InlineKeyboardButton( 'Брест', callback_data='Брест')
markup.add(brest)
vitebsk = types.InlineKeyboardButton('Витебск', callback_data='Витебск')
markup.add(vitebsk)
homel = types.InlineKeyboardButton('Гомель', callback_data='Гомель')
markup.add(homel)
hrodna = types.InlineKeyboardButton('Гродно', callback_data='Гродно')
markup.add(hrodna)
mogilev = types.InlineKeyboardButton('Могилев', callback_data='Могилев')
markup.add(mogilev)

# создаем функцию для определения геолокации
def loc(lat,lon):
  # LAT LON это широта и долгота
  url = f'https://yandex.ru/pogoda/maps/nowcast?lat={lat}&lon={lon}&via=hnav&le_lightning=1'
  # вставляем адрес сайта, откда мы буе=дем брать прогноз погоды
  return url
def weather(city:str):
  owm =OWM(config.API)
  # вставляем API для нахождения географических координат наших городов с сайта OpenWeatherMap
  mng = owm.weather_manager()
  # помогает получить текущий прогноз погоды
  observation = mng.weather_at_place(city)
  # помогает получить текущий прогноз погоды в определенном городе
  weather=observation.weather
  # пдключаем систему наблюдения за погодой
  location =loc(observation.location.lat, observation.location.lon)
  # указываем широту и долготу той местности в котрой нам нужно узнать погоду
  temperature = weather.temperature('celsius')
  # указываем единицу измерения температуры
  return temperature, location


# Создаем обработчик обратного вызова(привязываем кнопки)
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  if call.data == "Минск":
    city = call.data
    try:
      w = weather(city)
      bot.send_message(call.from_user.id, f'Температура в  {city}е  составляет  {round(w[0]["temp"])} градусов')
      # round w[0]temp округление значений темпиратуры до целого числа
      bot.send_message(call.from_user.id, w[1])
    except Exception:
      bot.send_message(call.from_user.id, 'Желаю вам прекрасного дня :)')
  elif call.data == "Брест":
    city = call.data
    try:
      w = weather(city)
      bot.send_message(call.from_user.id, f'Температура в  {city}е  составляет {round(w[0]["temp"])}  градусов')
      bot.send_message(call.from_user.id, w[1])
    except Exception:
       bot.send_message(call.from_user.id, 'Желаю вам прекрасного дня :)')
  elif call.data == "Витебск":
      city = call.data
      try:
        w = weather(city)
        bot.send_message(call.from_user.id, f'Температура в  {city}е  составляет {round(w[0]["temp"])}  градусов ')
        bot.send_message(call.from_user.id, w[1])
      except Exception:
        bot.send_message(call.from_user.id, 'Желаю вам прекрасного дня :)')
  elif call.data == "Гомель":
    city = call.data
    try:
      w = weather(city)
      bot.send_message(call.from_user.id, f'Температура в  {city}е  составляет  {round(w[0]["temp"])}  градусов')
      bot.send_message(call.from_user.id, w[1])
    except Exception:
      bot.send_message(call.from_user.id, 'Желаю вам прекрасного дня :)')
  elif call.data == "Гродно":
    city = call.data
    try:
      w = weather(city)
      bot.send_message(call.from_user.id, f'Температура в  {city}  составляет {round(w[0]["temp"])}  градусов')
      bot.send_message(call.from_user.id, w[1])
    except Exception:
      bot.send_message(call.from_user.id, 'Желаю вам прекрасного дня :)')
  elif call.data == "Могилев":
    city = call.data
    try:
      w = weather(city)
      bot.send_message(call.from_user.id, f'Температура в  {city}е  составляет  {round(w[0]["temp"])}  градусов')
      bot.send_message(call.from_user.id, w[1])
    except Exception:
      bot.send_message(call.from_user.id, 'Желаю вам прекрасного дня :)')
  else:
       bot.send_message(call.chat.id, "Выберите город из списка", parse_mode='html')

#запускаем код на постоянную обработку
bot.polling(none_stop=True, interval=0)