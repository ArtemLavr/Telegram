from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json, requests
import urllib.request

class Bot:
    def __init__(self):
        proxy = {'https':'socks5h://103.111.183.17:1080'}
        REQUEST_KWARGS={
        'proxy_url': 'socks5h://103.111.183.17:1080',
        
        
        }
        updater = Updater('') # Токен API к Telegram
        dispatcher = updater.dispatcher
        # Обработка команд
        
        # Хендлеры
        start_command_handler = CommandHandler('start', self.startCommand)
        text_message_handler = MessageHandler(Filters.text, self.textMessage)
        voice_message_handler = MessageHandler(Filters.voice, self.voiceMessage)
        # Добавляем хендлеры в диспетчер
        dispatcher.add_handler(start_command_handler)
        dispatcher.add_handler(text_message_handler)
        dispatcher.add_handler(voice_message_handler)
        # Начинаем поиск обновлений
        updater.start_polling(poll_interval=2, timeout=123)
        # Останавливаем бота, если были нажаты Ctrl + C
        updater.idle()

    def startCommand(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
    def textMessage(self, bot, update):
        response = 'Получил Ваше сообщение: ' + update.message.text
        bot.send_message(chat_id=update.message.chat_id, text=response)

    def voiceMessage(self, bot, update):   
        print('voiceMessage')
        FOLDER_ID = "b1g0r7o8n7g5616iikbm"

        key = "AQVN3iHuwi2rXwYnmJpWeeA-FTXW-5uTL1d9g0Vy"
        
        file_info = update.message.voice.file_id
        print(file_info)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format('971150956:AAGsjiYTJ6CGCe-mdnyEJM_EgTlm7aqmpUQ', bot.get_file(file_info).file_path))
        print(file.content)

        params = "&".join([
            "topic=general",
            "folderId=%s" % FOLDER_ID,
            "lang=ru-RU"
        ])

        url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=file.content)
        url.add_header("Authorization", "Api-Key %s" % key)

        responseData = urllib.request.urlopen(url).read().decode('UTF-8')
        decodedData = json.loads(responseData)
        
        if decodedData.get("error_code") is None:
            bot.send_message(chat_id=update.message.chat_id, text=decodedData.get("result"))





if __name__ == '__main__':
    Lavrbot= Bot()
