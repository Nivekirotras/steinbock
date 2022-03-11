from picamera import PiCamera
from time import sleep
import datetime

def takeImage():
    print('Start taking image')
    camera = PiCamera()
    camera.start_preview()
    camera.rotation = 180
    sleep(1)
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    camera.annotate_text = date
    camera.capture('/home/pi/PycharmProjects/Steinbock/Images/picture_'+ date +'.jpg')
    print(f"I took picture_{date}.jpg")
    camera.stop_preview()
    camera.close()
    sleep(1)
    return 'picture_'+ date +'.jpg'


def show_preview(seconds):
    camera = PiCamera()
    camera.rotation = 180
    
    camera.start_preview()
    sleep(seconds)
    camera.stop_preview()

