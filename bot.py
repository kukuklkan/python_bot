#   Iмпортування бібліотек
import telebot
from telebot import types
import json

#   Конфігурація бота
TOKEN = '6271089832:AAE4pT04iRrQZ7DwySc19_V2Tl7FeY-9y6I'
bot = telebot.TeleBot(TOKEN)


#   Зчитування даних з JSON файлу
with open('taryfs.json', 'r') as file:
    data = json.load(file)
    tarrifs = data['tariffs']['main']


#   Команда /start
@bot.message_handler(commands=['start'])
def hello(message):
    user = message.from_user
    user_name = user.first_name 
    user_id = user.id
    profile_link = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    tariff = telebot.types.InlineKeyboardButton('📲Вибір тарифу', callback_data='tariff')
    web = telebot.types.InlineKeyboardButton('🌐Наш сайт', url='https://www.lifecell.ua/uk/')
    markup.add(tariff, web)
    bot.reply_to(message,  f"Вітаю, {profile_link}! \nЧим можу допомогти?", parse_mode='HTML', reply_markup=markup)

#   Обробка кнопок
@bot.callback_query_handler(func=lambda call: True)
def calldack(call):
    msg_id = call.message.message_id
    user_name = call.from_user.first_name
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    profile_link = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    cost_for_hand_made = 120
    if call.message:
        if call.data == 'tariff':
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            default = telebot.types.InlineKeyboardButton('📲Звичайні тарифи', callback_data='default')
            handmade = telebot.types.InlineKeyboardButton('🖐Хендмейд', callback_data='handmade')
            markup.add(default, handmade)
            bot.send_message(chat_id, f'Виберіть тип тарифу.', reply_markup=markup)
        elif call.data == 'default':
            markup = telebot.types.InlineKeyboardMarkup(row_width=5)
            one = telebot.types.InlineKeyboardButton('1️⃣', callback_data='one')
            two = telebot.types.InlineKeyboardButton('2️⃣', callback_data='two')
            three = telebot.types.InlineKeyboardButton('3️⃣', callback_data='three')
            four = telebot.types.InlineKeyboardButton('4️⃣', callback_data='four')
            five = telebot.types.InlineKeyboardButton('5️⃣', callback_data='five')
            six = telebot.types.InlineKeyboardButton('6️⃣', callback_data='six')
            seven = telebot.types.InlineKeyboardButton('7️⃣', callback_data='seven')
            eight = telebot.types.InlineKeyboardButton('8️⃣', callback_data='eight')
            nine = telebot.types.InlineKeyboardButton('9️⃣', callback_data='nine')
            ten = telebot.types.InlineKeyboardButton('🔟', callback_data='ten')
            skip = telebot.types.InlineKeyboardButton('🚫Пропустити', callback_data='skip')
            markup.add(one, two, three, four, five, six, seven, eight, nine, ten, skip)
            bot.send_message(chat_id, f'Скiльки бажаете мiнiмум гiгабайтiв?', reply_markup=markup)
        elif call.data == 'handmade':
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            gigabytes = telebot.types.InlineKeyboardButton('🌐Кількість Гігабайтів', callback_data='gigabytes_for_hand_made')
            minutes = telebot.types.InlineKeyboardButton('⌚Кількість Хвилин', callback_data='minutes_for_hand_made')
            markup.add(gigabytes, minutes)
            bot.send_message(chat_id, f'Виберіть одну з оцій на ваш вибір.', reply_markup=markup)
        elif call.data == 'gigabytes_for_hand_made':
            markup = telebot.types.InlineKeyboardMarkup(row_width=4)
            zero_gigabates = telebot.types.InlineKeyboardButton('0️⃣', callback_data='zero_gigabytes')
            four_gigabates = telebot.types.InlineKeyboardButton('4️⃣', callback_data='four_gigabytes')
            ten_gigabates = telebot.types.InlineKeyboardButton('🔟', callback_data='ten_gigabytes')
            twenty_plus_gigabates = telebot.types.InlineKeyboardButton('2️⃣0️⃣+', callback_data='twenty_plus_gigabytes')
            markup.add(zero_gigabates, four_gigabates, ten_gigabates, twenty_plus_gigabates)
            bot.send_message(chat_id, f'Скільки потребуєте гігабайтів для використання?', reply_markup=markup)
        elif call.data == "minutes_for_hand_made":
            markup = telebot.types.InlineKeyboardMarkup(row_width=4)
            zero_minutes = telebot.types.InlineKeyboardButton('0️⃣', callback_data='zero_minutes')
            hundred_minutes = telebot.types.InlineKeyboardButton('1️⃣0️⃣0️⃣', callback_data='hundred_minutes')
            two_hundred_minutes = telebot.types.InlineKeyboardButton('2️⃣0️⃣0️⃣', callback_data='two_hundred_minutes')
            five_hundred_minutes = telebot.types.InlineKeyboardButton('5️⃣0️⃣0️⃣', callback_data='five_hundred_minutes')
            markup.add(zero_minutes, hundred_minutes, two_hundred_minutes, five_hundred_minutes)
            bot.send_message(chat_id, f'Скільки потребуєте хвилин для використання?', reply_markup=markup)
        elif call.data == 'zero_gigabytes':
            result_gigabytes = 0
            cost_for_hand_made += 0
        elif call.data == 'four_gigabytes':
            result_gigabytes = 4
            cost_for_hand_made += 40
        elif call.data == 'ten_gigabytes':
            result_gigabytes = 10
            cost_for_hand_made += 65
        elif call.data == 'twenty_plus_gigabytes':
            result_gigabytes = '20+'
            cost_for_hand_made += 125
        elif call.data == 'zero_minutes':
            result_minutes = 0
            cost_for_hand_made += 0
        elif call.data == 'hundred_minutes':
            result_minutes = 100
            cost_for_hand_made += 30
        elif call.data == 'two_hundred_minutes':
            result_minutes = 200
            cost_for_hand_made += 50
        elif call.data == 'five_hundred_minutes':
            result_minutes = 500
            cost_for_hand_made += 140
        elif call.data == 'one':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 1]
        elif call.data == 'two':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 2]
        elif call.data == 'three':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 3]
        elif call.data == 'four':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 4]
        elif call.data == 'five':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 5]
        elif call.data == 'six':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 6]
        elif call.data == 'seven':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 7]
        elif call.data == 'eight':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 8]
        elif call.data == 'nine':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 9]
        elif call.data == 'ten':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 10]







bot.infinity_polling()