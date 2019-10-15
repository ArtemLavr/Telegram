from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import urllib.request
import textparser
from textparser import Sequence

class Parser(textparser.Parser):
	def token_specs(self):
		return[
		('NUMBER', r'\d+' )

		]

	def grammar(self):
		return Sequence('NUMBER','NUMBER', 'NUMBER')

class Bot(Parser):
	chanels={
	'1':'Chanel1',
	'2':'Chanel2',
	'3':'Chanel3'
	}
	

	def __init__(self):
		
		REQUEST_KWARGS={
		'proxy_url':'socks5://103.240.160.21:6667/'
		}
		updater = Updater('710118530:AAEhsvUrxHKCqgi2Lk9UIc5XGx_-57CUp5Q', request_kwargs=REQUEST_KWARGS)
		dispatcher = updater.dispatcher



		post_command_handler = CommandHandler('post', self.postCommand)
		
		


		dispatcher.add_handler(post_command_handler)
		dispatcher.add_handler(MessageHandler(Filters.text, self.textMessage))
		dispatcher.add_handler(MessageHandler(Filters.photo, self.postMessage))
		dispatcher.add_handler(CallbackQueryHandler(self.postingControl))

		updater.start_polling()
		updater.idle()

	def postCommand(self, bot, update):
		chanel_list = '''
		Send numbers of chanels:
		 '''
		
		for key, value in self.chanels.items():
			item = key + '.' + value+"\n"
			chanel_list += item
			
		bot.send_message(chat_id=update.message.chat_id, 
			text=chanel_list)
		


	def textMessage(self, bot, update):
		print('textMessage')
		chanels_select = Parser().parse(update.message.text)
		bot.send_message(chat_id=update.message.chat_id, 
			text='Please ,create the post')
		
	def build_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
		menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
		if header_buttons:
			menu.insert(0, [header_buttons])
		print(menu)
		return menu

	def postMessage(self, bot, update):
		
		self.Photo = update.message.photo[-1].file_id
		self.Caption = update.message.caption
		print(self.Caption)
		
		bot.send_photo(chat_id=update.message.chat_id, photo = Photo)
		
		button_list = [
		InlineKeyboardButton("Yes", callback_data='yes'),
		InlineKeyboardButton("Not", callback_data='not')
		]
		
		reply_markup = InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))
		bot.send_message(chat_id=update.message.chat_id, text  = "Post it on channels?", reply_markup=reply_markup)

	

	def postingControl(self, bot, update):
		query = update.callback_query

		if query.data == 'yes':
			pass

		bot.send_photo(chat_id='channels chat_id',photo = self.Photo, caption)

		








if __name__ == '__main__':
	Post_control_bot= Bot()






