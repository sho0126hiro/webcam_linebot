# cron 
import requests,datetime
import subprocess,os
import TOKEN
from time import sleep
url = "https://notify-api.line.me/api/notify"

def get_picture(img_name):
    cheese=['fswebcam','-p','MJPEG','-r','1280x1024','--no-banner','-D','1',img_name]
    try:
        subprocess.check_call(cheese)
        print ("Command finished.")
    except:
        return "Command envailed."
    return "Success"

def get_now_time():
    d = datetime.datetime.today()
    print(d.strftime("%Y-%m-%d %H:%M:%S"), '\n')
    return str(d.strftime("%Y-%m-%d %H:%M:%S"))

def post(img_name):
    sleep(30)
    headers = {"Authorization" : "Bearer "+ TOKEN.LINE_TOKEN}
    payload = {"message" : get_now_time()}
    files = {"imageFile": open(img_name, "rb")}
    res = requests.post(url,headers=headers,params=payload,files=files)
    os.remove('./'+img_name)

img_name = get_now_time() + '.jpg'
get_picture(img_name)
# print(get_now_time())
post(img_name)
