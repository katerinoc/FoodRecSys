
#pip install pytelegrambotapi

import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('5333132728:AAFR8-xyVUa5KLWD8FK4MghEBw4osIOP9Rs')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text","photo"])
def handle_text(message):
    if message.content_type == 'text':
      bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    elif message.content_type == 'photo':
      raw = message.photo[2].file_id
      name = raw+".jpg"
      file_info = bot.get_file(raw)
      downloaded_file = bot.download_file(file_info.file_path)
      with open(name,'wb') as new_file:
            new_file.write(downloaded_file)
      res = open(name, 'rb')
      # Отправка фото в ответ
      bot.send_photo(message.chat.id, res)

# Запускаем бота
bot.polling(none_stop=True, interval=0)