import telebot
import wikipedia

bot = telebot.TeleBot("1791221286:AAGDHeqryK2Rrt-mBisJS_3UHJ27fLh4lO0")

@bot.message_handler(commands = ['start'])
def xush_kelibsiz(message):
	matn = f"<b>Assalomu alaykum {message.from_user.first_name}</b>"
	matn += "<i>\n\nMeni @turdibekdev va @pythonpractic kanallari sizga hizmat qilishim uchun yaratishdi.</i>"
	matn += "\nMen sizga Wikipedia onlayn ensiklopediyasidan malumot olib beraman. Marhamat menga mavzu jonating..."
	bot.send_message(message.chat.id, matn, parse_mode = "HTML")


@bot.message_handler(func=lambda message: True)	
def wikipedia_search(wiki):
	try:
		mavzu = wiki.text
		wikipedia.set_lang("uz")
		natija = wikipedia.summary(mavzu)
		natija += "\n@turdibekdev - @pythonpractic"
		bot.send_message(wiki.chat.id, natija)
	except:
		matn = "Menimcha bu mavzuni topa olmayman..."
		bot.send_message(wiki.chat.id, matn)
bot.polling(True)