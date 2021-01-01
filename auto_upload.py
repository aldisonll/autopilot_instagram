from instabot import Bot
import os

bot = Bot()
bot.login(username=os.environ.get(USERNAME), password=os.environ.get(PASSWORD)) # login to instagram
file = 'photos/' + file # get path of the picture
bot.upload_photo(file, caption="your post caption") # write a caption & upload