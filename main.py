import telebot
import os

bot = telebot.TeleBot('1653986362:AAF9EhDJtV7Ucjq1gUrLWY0w-6h204p_NAk')

@bot.channel_post_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio", "video", "location", "document"])
def send(message):

    if message.text:
        bot.send_message("@melltestmain", message.text)

    if message.document:
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            src = '../TeleBotChannels/save/' + file_info.file_path;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.send_document("@melltestmain", downloaded_file, caption=message.caption)
            os.remove('../TeleBotChannels/save/' + file_info.file_path)
        except:
            return 0

    if message.photo:
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src='../TeleBotChannels/save/'+file_info.file_path;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_photo("@melltestmain", downloaded_file, caption=message.caption)
        os.remove('../TeleBotChannels/save/' + file_info.file_path)

    if message.video:
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src='../TeleBotChannels/save/' +file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.send_video("@melltestmain", downloaded_file, caption=message.caption)
        os.remove('../TeleBotChannels/save/' + file_info.file_path)

    if message.audio:
        try:
            file_info = bot.get_file(message.audio.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src='../TeleBotChannels/save/'+file_info.file_path;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.send_audio("@melltestmain", downloaded_file, caption=message.caption)
            os.remove('../TeleBotChannels/save/' + file_info.file_path)
        except:
            return 0

    if message.voice:
        try:
            file_info = bot.get_file(message.voice.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src='../TeleBotChannels/save/'+file_info.file_path;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.send_audio("@melltestmain", downloaded_file, caption=message.caption)
            os.remove('../TeleBotChannels/save/' + file_info.file_path)
        except:
            return 0

    if message.sticker:
        file_info = bot.get_file(message.sticker.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src='../TeleBotChannels/save/'+file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.send_sticker("@melltestmain", downloaded_file)
        os.remove('../TeleBotChannels/save/' + file_info.file_path)

    if message.location:
        file_info = bot.get_file(message.location.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src='../TeleBotChannels/save/'+file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.send_location("@melltestmain", downloaded_file)
        os.remove('../TeleBotChannels/save/' + file_info.file_path)

bot.polling(none_stop=True)