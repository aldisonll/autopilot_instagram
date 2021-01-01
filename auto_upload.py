from instabot import Bot
import os, time

arr = os.listdir('./photos')

bot = Bot() 
bot.login(username=None, password=None) # login to instagram

print(f'{len(arr)} Images Are Founded')
for file in arr:
    if file[-4:] == ".jpg": # check if file name is .jpg
        img_path = 'photos/' + str(file) # get path of the picture
        print(img_path)
        bot.upload_photo(img_path, caption="#programming") # write a caption & upload
        time.sleep(60*60*4) # wait 4 hour