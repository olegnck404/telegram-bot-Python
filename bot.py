import telebot
import config



from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	
	item1 = types.KeyboardButton("Инструкции")
	item2 = types.KeyboardButton("Приложения")
	item3 = types.KeyboardButton("Прошивки")
	item4 = types.KeyboardButton("Каналы с прошивками")
	item5 = types.KeyboardButton("YouTube Каналы")
	item6 = types.KeyboardButton("Чаты")
	markup.add(item1, item2, item3, item4, item5, item6)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'dev':
			bot.send_message(message.chat.id,'  @oleqwg ',)
		elif message.text == 'Прошивки':
			bot.send_message(message.chat.id,'  https://t.me/RedmiNote5_By_XTB/887739 '  )
			#instructions
		elif message.text == 'Инструкции':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Остаточное изображение", callback_data='screenburn')
			item2 = types.InlineKeyboardButton("Фикс лаунчера MiUi", callback_data='fml')
			item3 = types.InlineKeyboardButton("ViperFX", callback_data='vfx')
			
			
			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)

			#apps
		elif message.text == 'Приложения':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("YouTube Vanced", callback_data='yt')
			item2 = types.InlineKeyboardButton("Google Camera", callback_data='gcam')
			item3 = types.InlineKeyboardButton("Vtosters", callback_data='vt')
			item4 = types.InlineKeyboardButton("Magisk Manager", callback_data='magisk')


			markup.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)
			#channels
		
		elif message.text == 'Каналы с прошивками':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Whyred Cloud", callback_data='whyc')
			item2 = types.InlineKeyboardButton("Whyred Updates", callback_data='wucc')
			item3 = types.InlineKeyboardButton("Модули Magisk", callback_data='MM')
			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)
			#Ytube
		elif message.text == 'YouTube Каналы':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Xiaomi Techo Blog(RU)", callback_data='xtb')
			item2 = types.InlineKeyboardButton("KTNTECH(ENG)", callback_data='ktn')
			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)
			#chats
		elif message.text == 'Чаты':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("4PDA RN 5 CHAT (RU)", callback_data='4rc')
			item2 = types.InlineKeyboardButton("XTB RN5 CHAT (RU)", callback_data='xtbrn5')
			item3 = types.InlineKeyboardButton("Whyred Cloud Chat (ENG)", callback_data='whych')
			item4 = types.InlineKeyboardButton("Whyred Updates Chat (ENG)", callback_data='whuc')
			
			markup.add(item1, item2, item3, item4)

			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)
			
			#X3
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
#inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'stab':
				bot.send_message(call.message.chat.id, 'https://downloads.sourceforge.net/project/miroom/stable/V11.0/RedmiNote5_MIUI_V11.0.2.0.PEICNXM_MiRoom_9.0.zip?r=https%3A%2F%2Fportal.mi-room.ru%2Froms%2F&ts=1580589124&use_mirror=netix')
			elif call.data == 'screenburn':
				bot.send_message(call.message.chat.id,'  https://telegra.ph/Solve-screen-burn-in-whyred-08-17' )
			elif call.data == 'fml':
				bot.send_message(call.message.chat.id,'  https://youtu.be/a4uIfmZt7GQ' )
			elif call.data == 'magisk':
				bot.send_message(call.message.chat.id,' https://magiskmanager.com/downloading-magisk-manager') 					#apps
			elif call.data == 'yt':
				bot.send_message(call.message.chat.id,'  https://vanced.app/nonroot  ' )
			elif call.data == 'gcam':
				bot.send_message(call.message.chat.id,'  https://t.me/googlecamera_mod/1629 ' )
			elif call.data == 'vt':
				bot.send_message(call.message.chat.id,'  https://t.me/vtosters/1030 ' )
			elif call.data == 'vfx':
				bot.send_message(call.message.chat.id,' https://telegra.ph/Nastrojka-ViperFX-07-04 ')
			
			elif call.data == 'whyc':
				bot.send_message(call.message.chat.id,'  https://t.me/WhyRedCloud  ')
			elif call.data == 'wucc':
				bot.send_message(call.message.chat.id,'   https://t.me/whyredupdates  ')
			elif call.data == 'xtb':
				bot.send_message(call.message.chat.id,'  https://www.youtube.com/channel/UCyvYoGiKx89QAwlyaSRqJog')
			elif call.data == 'ktn':
				bot.send_message(call.message.chat.id,'  https://www.youtube.com/channel/UCITBrtvDaIf0lC-7Ns3dXvA ')
			elif call.data == 'whych':
				bot.send_message(call.message.chat.id,'  https://t.me/rn5pofficial  ')
			elif call.data == 'whuc':
				bot.send_message(call.message.chat.id,'   https://t.me/redminote5proofficial ')
			elif call.data == 'xtbrn5':
				bot.send_message(call.message.chat.id,'  https://t.me/RedmiNote5_By_XTB')
			elif call.data == '4rc':
				bot.send_message(call.message.chat.id,' https://t.me/redminote5pro ')
			elif call.data == 'MM':	
				bot.send_message(call.message.chat.id,' https://t.me/magisk_xtb ')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ссылка",
				reply_markup=None)

			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="ЭТО ТЕСТОВЫЙ БОТ")

	except Exception as e:
		print(repr(e))
#token = os.envior.get('TOKEN')
#bot.run(str(token))
# RUN
bot.polling(none_stop=True)
