import pyperclip, requests, json
from win10toast import ToastNotifier
toaster = ToastNotifier()

headers = {'authority': 'www.instagram.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?0','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'en-US,en;q=0.9',}
recent_value = ""

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        if recent_value[0:28] == "https://www.instagram.com/p/": # check if copied value is a image from instagram
           print("Copied Image Url: "+recent_value)
           print("Downloading The Image...")
           try:
                postApi = requests.get(url=recent_value, params = (('__a', '1'),), headers = headers) # get the image source
                response = requests.get(url=json.loads(postApi.text)["graphql"]["shortcode_media"]["display_url"]) # get image link source
                with open("photos/" + str(recent_value[29:39]) + ".jpg", "wb") as f: # downloading image to /photos folder
                    f.write(response.content)
                    toaster.show_toast("Instagram AutoPilot 1.0", "Image Downloaded: " + str("https://www.instagram.com/" + recent_value[29:39]), icon_path="logo.ico",)
                    print("Image Downloaded Successfuly")
           except:
               print("Somthing's Wrong")         
                