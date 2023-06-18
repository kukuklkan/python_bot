#   Iмпортування бібліотек
import telebot
from telebot import types
import json

#   Конфігурація бота
TOKEN = '5665735947:AAG0MhcHkPhFxxYtmB1mbdrdHXXXKjpIH90'
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
    if call.message:
        if call.data == 'tariff':
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            default = telebot.types.InlineKeyboardButton('📲Звичайні тарифи', callback_data='default')
            handmade = telebot.types.InlineKeyboardButton('🖐Хендмейд', callback_data='handmade')
            markup.add(default, handmade)
            bot.send_message(chat_id, f'Виберіть тип тарифу.', reply_markup=markup)
        elif call.data == 'default':
            markup = telebot.types.InlineKeyboardMarkup(row_width=3)
            twenty = telebot.types.InlineKeyboardButton('2️⃣0️⃣ та більше', callback_data='twenty')
            ten = telebot.types.InlineKeyboardButton('🔟 та менше', callback_data='ten')
            skip = telebot.types.InlineKeyboardButton('🚫Пропустити', callback_data='skip')
            markup.add(ten, twenty, skip)
            bot.send_message(chat_id, f'🌐Скільки потребуєте стільникового інтернету для користування?', reply_markup=markup)
        elif call.data == 'handmade':
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            start_in_hand_made = telebot.types.InlineKeyboardButton('🚀Почнемо складати ваший перснальний тариф!', callback_data='gigabytes_for_hand_made')
            markup.add(start_in_hand_made)
            bot.send_message(chat_id, f'Виберіть одну з опцій на ваш вибір.', reply_markup=markup)
            with open('gigabytes.json', 'w') as gigabytes_json:
                info_dict = {'cost':0, 'gigabytes':0}
                json.dump(info_dict, gigabytes_json)
            with open('minutes.json', 'w') as gigabytes_json:
                info_dict = {'cost':0, 'gigabytes':0}
                json.dump(info_dict, gigabytes_json)
        # Buttons for Gigabytes
        elif call.data == 'gigabytes_for_hand_made':
            with open('gigabytes.json', 'w') as gigabytes_json:
                info_dict = {'cost':0, 'gigabytes':0}
                json.dump(info_dict, gigabytes_json)
            markup = telebot.types.InlineKeyboardMarkup(row_width=4)
            zero_gigabates = telebot.types.InlineKeyboardButton('0️⃣', callback_data='sub_result_zero')
            four_gigabates = telebot.types.InlineKeyboardButton('4️⃣', callback_data='sub_result_four')
            ten_gigabates = telebot.types.InlineKeyboardButton('🔟', callback_data='sub_result_ten')
            twenty_plus_gigabates = telebot.types.InlineKeyboardButton('2️⃣0️⃣+', callback_data='sub_result_twenty')
            markup.add(zero_gigabates, four_gigabates, ten_gigabates, twenty_plus_gigabates)
            bot.send_message(chat_id, f'Скільки потребуєте гігабайтів для використання?', reply_markup=markup)
        # Sub level in taking gigabytes
        elif call.data == 'sub_result_zero':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('gigabytes.json', 'w') as gigabytes_json:
                info_dict = {'cost':0, 'gigabytes':0}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 0 Гігабайтів для користування!', reply_markup=markup)
        elif call.data == 'sub_result_four':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('gigabytes.json', 'w') as gigabytes_json:
                info_dict = {'cost':40, 'gigabytes':4}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 4 Гігабайтів для користування!', reply_markup=markup)
        elif call.data == 'sub_result_ten':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('gigabytes.json', 'w') as gigabytes_json:
                info_dict = {'cost':45, 'gigabytes':10}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 10 Гігабайтів для користування!', reply_markup=markup)
        elif call.data == 'sub_result_twenty':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('gigabytes.json', 'w') as gigabytes_json:
                info_dict = {'cost':105, 'gigabytes':20}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 20+ Гігабайтів для користування!', reply_markup=markup)
        # Button for Minutes
        elif call.data == "minutes_for_hand_made":
            with open('minutes.json', 'w') as gigabytes_json:
                info_dict = {'cost':0, 'gigabytes':0}
                json.dump(info_dict, gigabytes_json)
            markup = telebot.types.InlineKeyboardMarkup(row_width=4)
            zero_minutes = telebot.types.InlineKeyboardButton('0️⃣', callback_data='sub_result_zero_minutes')
            hundred_minutes = telebot.types.InlineKeyboardButton('1️⃣0️⃣0️⃣', callback_data='sub_result_hundred_minutes')
            two_hundred_minutes = telebot.types.InlineKeyboardButton('2️⃣0️⃣0️⃣', callback_data='sub_result_twohundred_minutes')
            five_hundred_minutes = telebot.types.InlineKeyboardButton('5️⃣0️⃣0️⃣', callback_data='sub_result_fivehundred_minutes')
            markup.add(zero_minutes, hundred_minutes, two_hundred_minutes, five_hundred_minutes)
            bot.send_message(chat_id, f'Скільки потребуєте хвилин для використання?', reply_markup=markup)
        # Sub level of taking minutes
        elif call.data == 'sub_result_zero_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('minutes.json', 'w') as gigabytes_json:
                info_dict = {'cost':0, 'minutes':0}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 0 Хвилин для користування!', reply_markup=markup)
        elif call.data == 'sub_result_hundred_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('minutes.json', 'w') as gigabytes_json:
                info_dict = {'cost':30, 'minutes':100}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 100 Хвилин для користування!', reply_markup=markup)
        elif call.data == 'sub_result_twohundred_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('minutes.json', 'w') as gigabytes_json:
                info_dict = {'cost':50, 'minutes':200}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 200 Хвилин для користування!', reply_markup=markup)
        elif call.data == 'sub_result_fivehundred_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            with open('minutes.json', 'w') as gigabytes_json:
                info_dict = {'cost':140, 'minutes':500}
                json.dump(info_dict, gigabytes_json)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 500 Хвилин для користування!', reply_markup=markup)
        # Result of choosing
        if call.data == 'taryf_for_hand_made':
            with open('minutes.json', 'r') as minutes_json:
                minutes_cost = json.load(minutes_json)
            with open('gigabytes.json', 'r') as gigabytes_json:
                gigabytes_cost = json.load(gigabytes_json)
            result_in_gigabytes = gigabytes_cost['gigabytes']
            result_in_minutes = minutes_cost['minutes']
            result_in_cost = gigabytes_cost['cost'] + minutes_cost['cost'] + 120
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            change_taryf = telebot.types.InlineKeyboardButton('♻️Змінити данні тарифу', callback_data='handmade')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='tariff')
            markup.add(change_taryf, back)
            bot.send_message(chat_id, f'Тариф який ви зібрали:\nГігабайти: {result_in_gigabytes}\nХвилини: {result_in_minutes}\nЦіна вашого тарифу: {result_in_cost}грн.\nДля зміни тарифу натисніть нижче (Змінити данні тарифу) або для вибору тарифу з наявних натисніть (Повернутися назад).', reply_markup = markup)
        elif call.data == 'nine':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 9]
        elif call.data == 'ten':
            filtered_tariffs = [tariff for tariff in tariffs if tariff[list(tariff.keys())[0]]['gigabytes'] >= 10]






bot.infinity_polling()