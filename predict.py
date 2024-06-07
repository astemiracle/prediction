import random
import telebot

sleeptoken = 'YOUR_BOT_TOKEN'

predictions = [
    "Вас, @{}, ждет успех в ближайшее время!",
    "@{}, сегодня вам улыбнется удача.",
    "Скоро, @{}, вы встретите интересного человека.",
    "@{}, ваши финансовые дела пойдут в гору.",
    "Вас, @{}, ждут перемены к лучшему.",
    #накинуть еще
]

bot = telebot.TeleBot(sleeptoken)

@bot.message_handler(commands=['prediction'])
def send_prediction(message):
    chat_members = bot.get_chat_members(message.chat.id)
    random_member = random.choice([m for m in chat_members if not m.user.is_bot])
    prediction = random.choice(predictions).format(random_member.user.username)
    bot.reply_to(message, prediction)


bot.polling()