import random
import telebot
from telebot.types import Message
bot = telebot.TeleBot('7244470047:AAHMLi-Fz3b703NeRlTw3MB6fknZlZgK_jQ')
@bot.message_handler(commands=['start'])
def cmd_start(message: Message):
    bot.reply_to(message, 'Привет!')

@bot.message_handler(commands=['coin'])
def cmd_coins(message: Message):
    x = random.randint(1, 2)
    if x == 1:
        bot.reply_to(message, 'Выпал орёл')
    else:
        bot.reply_to(message, 'Выпала решка')

@bot.message_handler(commands=['math'])
def cmd_math(message: Message):
    bot.reply_to(message, '2 + 2 = 4')




@bot.message_handler(commands=['password'])
def cmd_password(message: Message):
   sogl = 'qwrtpsdfghjklzxcvbnmQWRTOPSDFGHJKLZXCVBNM'
   glas = 'aeyuioAEYUIO'
   numbers = '1234567890'
   symbols = '@#%&*'
   lenght = 12
   password = ''
   for i in range(random.randint(3, 4)):
    password += random.choice(sogl) + random.choice(glas)

   for i in range(random.randint(2, 4)):
    password += random.choice(numbers)

   for i in range(random.randint(2, 4)):
    password += random.choice(symbols)
   bot.reply_to(message, 'ваш пароль:' + password)

@bot.message_handler(commands=['name'])
def cmd_name(message: Message):
   bot.reply_to(message, 'Как вас зовут?')
   bot.register_next_step_handler(message, get_name)

def get_name(message: Message):
   name = message.text
   bot.reply_to(message, 'Ваше имя: ' + name)

@bot.message_handler(commands=['RPC'])
def cmd_RPC(message: Message):
   bot.reply_to(message, 'выберите один из трёх вариантов и напишите его: Камень, ножницы, бумага')
   bot.register_next_step_handler(message, get_RPC)

def get_RPC(message: Message):
   player = message.text
   comp = random.choice(['камень','ножницы','бумага'])
   if player == comp:
      bot.reply_to(message, 'Ничья!')
   elif player == 'камень' and comp == 'ножницы':
        bot.reply_to(message, 'Вы победили!')
   elif player == 'ножницы' and comp == 'бумага':
        bot.reply_to(message, 'Вы победили!')
   elif player == 'бумага' and comp == 'камень':
        bot.reply_to(message, 'Вы победили!')
   else:
        bot.reply_to(message, 'Вы проиграли!')

@bot.message_handler(commands=['animals'])
def cmd_animals(message: Message):
   animals = random.choice(['Собака', 'Кошка', 'Рыбка', 'Кролик', 'Морская свинка', 'Хорёк', 'Попугай', 'Хомяк', 'Шиншилла'])
   bot.reply_to(message, animals)


@bot.message_handler(commands=['challenge'])
def cmd_challenge(message: Message):
   challenge = random.choice(['сделай 5 отжиманий', 'нарисуй ровный круг от руки', 'уберись в доме'])
   bot.reply_to(message, challenge)
bot.polling()    
