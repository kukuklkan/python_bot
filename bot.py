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
    class Holder():
        def set(self, value):
            self.value = value
        def get(self, get_value = 0):
            self.get_value = get_value + self.value
            return self.get_value
def ensure(x):
    if x: yield x        
    msg_id = call.message.message_id
    user_name = call.from_user.first_name
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    profile_link = f'<a href="tg://user?id={user_id}">{user_name}</a>'
    cost_of_handmade = Holder()
    result_minutes = Holder()
    result_gigabytes = Holder()
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
            start_in_hand_made = telebot.types.InlineKeyboardButton('🚀Почнемо складати ваший перснальний тариф!', callback_data='gigabytes_for_hand_made')
            markup.add(start_in_hand_made)
            bot.send_message(chat_id, f'Виберіть одну з опцій на ваш вибір.', reply_markup=markup)
            result_gigabytes.set(0)
            result_minutes.set(0)

        # Buttons for Gigabytes
        elif call.data == 'gigabytes_for_hand_made':
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
            result_gigabytes.set(0)
            cost_of_handmade.set(0)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 0 Гігабайтів для користування!', reply_markup=markup)
        elif call.data == 'sub_result_four':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            result_gigabytes.set(4)
            cost_of_handmade.get(40)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 4 Гігабайтів для користування!', reply_markup=markup)
        elif call.data == 'sub_result_ten':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            result_gigabytes.set(10)
            cost_of_handmade.get(45)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 10 Гігабайтів для користування!', reply_markup=markup)
        elif call.data == 'sub_result_twenty':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            result_gigabytes.set(20)
            cost_of_handmade.get(105)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='minutes_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='gigabytes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 20+ Гігабайтів для користування!', reply_markup=markup)
        # Button for Minutes
        elif call.data == "minutes_for_hand_made":
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
            result_minutes.set(0)
            cost_of_handmade.get(0)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 0 Хвилин для користування!', reply_markup=markup)
        elif call.data == 'sub_result_hundred_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            result_minutes.set(100)
            cost_of_handmade.get(30)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 100 Хвилин для користування!', reply_markup=markup)
        elif call.data == 'sub_result_twohundred_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            result_minutes.set(200)
            cost_of_handmade.get(50)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 200 Хвилин для користування!', reply_markup=markup)
        elif call.data == 'sub_result_fivehundred_minutes':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            result_minutes.set(500)
            cost_of_handmade.get(140)
            sub_result = telebot.types.InlineKeyboardButton('🚀Продовжимо', callback_data='taryf_for_hand_made')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='minutes_for_hand_made')
            markup.add(sub_result, back)
            bot.send_message(chat_id, f'Було вибрано 500 Хвилин для користування!', reply_markup=markup)
        # Result of choosing
        elif call.data == 'taryf_for_hand_made':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            change_taryf = telebot.types.InlineKeyboardButton('♻️Змінити данні тарифу', callback_data='handmade')
            back = telebot.types.InlineKeyboardButton('🔙Повернутися назад', callback_data='tariff')
            markup.add(change_taryf, back)
            print(result_gigabytes.get())
            bot.send_message(chat_id, f'Тариф який ви зібрали:\nГігабайти: {result_gigabytes.get()}\nХвилини: {result_minutes.get()}\nЦіна вашого тарифу: {cost_of_handmade.get()}грн.\nДля зміни тарифу натисніть нижче (Змінити данні тарифу) або для вибору тарифу з наявних натисніть (Повернутися назад).', reply_markup = markup)
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