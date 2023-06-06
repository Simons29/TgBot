import telebot
from telebot import  types

bot = telebot.TeleBot('6072374525:AAFuKNIZz0rBSjc2Z-We8KWIyCbkycrGKvc')


@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    zakazz = types.KeyboardButton('Сделать заказ')
    markup.add(zakazz)
    bot.send_message(message.chat.id, f'Здравствуйте, <b>{message.from_user.first_name}</b>, я Telegram-Bot Фунтик и помогаю людям делать интернет-заказы! Примерные сроки доставки 21 день! Для начала оформления нажмите кнопку <b>"Сделать заказ"</b>', parse_mode='html', reply_markup=markup)

adm = 647232633

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    klava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    product1 = types.KeyboardButton('Одежда')
    product2 = types.KeyboardButton('Обувь')
    product3 = types.KeyboardButton('Другое')
    klava.add(product1)
    klava.add(product2)
    klava.add(product3)
    choice_product = bot.send_message(message.chat.id, f'Сейчас вам будут предложены категории товаров выберите <b>одну</b> из них для продолжения оформления заказа', parse_mode='html', reply_markup=klava)
    bot.register_next_step_handler(choice_product, choice_size)


def choice_size(message):
    if (message.text == "Одежда"):
        gg = telebot.types.ReplyKeyboardRemove()
        size1 = bot.send_message(message.from_user.id, f'Ведите ваш размер <b>Образец: XS/S/M/L/XL</b>', parse_mode='html', reply_markup=gg)
        bot.register_next_step_handler(size1, send_photo)
    if (message.text == "Обувь"):
        gg = telebot.types.ReplyKeyboardRemove()
        size2 = bot.send_message(message.from_user.id, f'Ведите ваш размер <b>Образец: 8US/9US/10US/11US</b>', parse_mode='html', reply_markup=gg)
        bot.register_next_step_handler(size2, send_photo)
    if (message.text == "Другое"):
        gg = telebot.types.ReplyKeyboardRemove()
        size3 = bot.send_message(message.from_user.id, f'Для того чтобы продолжить заказ напшите <b>Продолжить</b>', parse_mode='html', reply_markup=gg)
        bot.register_next_step_handler(size3, send_photo1)
        

def send_photo1(message):
    
    if (message.text =="Продолжить"):
        msg = bot.send_message(message.from_user.id, f'Отправьте фотографию нужного вам товара', parse_mode='html')
        bot.register_next_step_handler(msg, fio_user)
    else:
        xueta = bot.send_message(message.chat.id, f'<b>Введите продолжить</b>', parse_mode='html')
        bot.register_next_step_handler(xueta, send_photo1)


def fio_user(message):
    print('fio_user')
    print(message.chat.id)
    if message.content_type == 'photo':
        print(message.photo[-1].file_id) 
        bot.send_photo(adm, message.photo[-1].file_id)
        send_fio = bot.send_message(message.chat.id, f'Для дальнейшего офрмления нам понадобится ваше ФИО. Образец:<b>Иванов Иван Иванович</b>', parse_mode='html')
        bot.register_next_step_handler(send_fio, send_address1)
    else:
        zaeblo = bot.send_message(message.chat.id, f'<b>Отправьте фотографию пожалуйста</b>', parse_mode='html')
        bot.send_message(adm, message.text)
        bot.register_next_step_handler(zaeblo, fio_user)


def send_address1(message):
    send_address = bot.send_message(message.chat.id, f'Введите свой адрес. Образец:<b>Москва, Черноморский бульвар, 30К3, кв 51</b>', parse_mode='html')
    global send_fio1
    send_fio1 = message.text
    bot.send_message(adm, send_fio1)
    bot.register_next_step_handler(send_address, check_info1)


def check_info1(message):
        global your_index,  key_yes, key_no
        your_index = message.text
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        key_yes = types.KeyboardButton('Верно') 
        keyboard.add(key_yes)
        key_no= types.KeyboardButton('Не верно')
        keyboard.add(key_no)
        jopa = bot.send_message(message.chat.id, f'Тебя зовут <b>{send_fio1}</b>?, Твой адрес <b>{your_index}</b>?', parse_mode='html', reply_markup=keyboard)
        bot.register_next_step_handler(jopa, check_you)
        bot.send_message(adm, your_index)


def send_photo(message):
    if (message.text == "XS" or message.text =="S" or message.text =="M" or message.text =="L" or message.text =="XL" or message.text =="8US" or message.text =="9US" or message.text =="10US" or message.text =="11US" or message.text =="Продолжить"):
        msg = bot.send_message(message.from_user.id, f'Отправьте фотографию нужного вам товара', parse_mode='html')
        bot.register_next_step_handler(msg, forward_adm)
    else:
        xueta = bot.send_message(message.chat.id, f'<b>Введите размер корректно, как показанно в образце</b>', parse_mode='html')
        bot.register_next_step_handler(xueta, send_photo)
    global your_size
    your_size = message.text
    bot.send_message(adm, your_size)
    
        
def forward_adm(message):
    print('forward_adm')
    print(message.chat.id)
    if message.content_type == 'photo':
        print(message.photo[-1].file_id) 
        bot.send_photo(adm, message.photo[-1].file_id)
        send_fio = bot.send_message(message.chat.id, f'Для дальнейшего офрмления нам понадобится ваше ФИО. Образец:<b>Иванов Иван Иванович</b>', parse_mode='html')
        bot.register_next_step_handler(send_fio, send_address)
    else:
        zaeblo = bot.send_message(message.chat.id, f'<b>Отправьте фотографию пожалуйста</b>', parse_mode='html')
        bot.send_message(adm, message.text)
        bot.register_next_step_handler(zaeblo, forward_adm)
        
        
def send_address(message):
    send_address = bot.send_message(message.chat.id, f'Введите свой адрес. Образец:<b>Москва, Черноморский бульвар, 30К3, кв 51</b>', parse_mode='html')
    global send_fio1
    send_fio1 = message.text
    bot.send_message(adm, send_fio1)
    bot.register_next_step_handler(send_address, check_info)
    
        
def check_info(message):
        global your_index,  key_yes, key_no
        your_index = message.text
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        key_yes = types.KeyboardButton('Верно') 
        keyboard.add(key_yes)
        key_no= types.KeyboardButton('Не верно')
        keyboard.add(key_no)
        jopa = bot.send_message(message.chat.id, f'Тебя зовут <b>{send_fio1}</b>?, Твой адрес <b>{your_index}</b>, Твой размер <b>{your_size}?</b>', parse_mode='html', reply_markup=keyboard)
        bot.register_next_step_handler(jopa, check_you)
        bot.send_message(adm, your_index)


def check_you(message):
    if (message.text == "Верно"):
        de = telebot.types.ReplyKeyboardRemove()
        final = bot.send_message(message.from_user.id, 'Отправьте скриншот с оплатой товара', reply_markup=de)
        bot.register_next_step_handler(final,  pay)
    elif (message.text == "Не верно"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1); 
        key_photo = types.KeyboardButton('Измените свои данные') 
        keyboard.add(key_photo)
        msg3 = bot.send_message(message.from_user.id, 'Вам придётся заполнить анкету сначала', reply_markup=keyboard)
        bot.register_next_step_handler(msg3, modfay_info)

 
def pay(message):
    if message.content_type == 'photo':
        bot.send_photo(adm, message.photo[-1].file_id)
        bot.send_message(message.chat.id, 'Спасибо, что выбрали нашего бота для оформления заказа “Funtik”, примерные сроки доставки 21 день с момента отправления товара, чуть позже мы отправим Вам трек номер для отслеживания вашего заказа, ВСЕГО ДОБРОГО!!!')
    else:
        repeat = bot.send_message(message.chat.id, 'ПЛОТИ БЫСТРО')
        bot.register_next_step_handler(repeat, pay)

def modfay_info(message):
    if (message.text == "Изменить свои данные"):
        de = telebot.types.ReplyKeyboardRemove()
        nadoel =  bot.send_message(message.from_user.id, 'Заполните анкету',  reply_markup=de)
        bot.register_next_step_handler(nadoel, send_welcome)

        
bot.polling(none_stop=True)