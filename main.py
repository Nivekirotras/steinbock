from use_google_drive import uploadImage
from use_camera import takeImage, show_preview
#from use_remote_stream import start_stream
from time import sleep
import datetime

print('Start main!')
#image_name = takeImage()
#uploadImage(image_name)

#print("File " + image_name + " uploaded")
#start_stream()

#show_preview(5)

def timelapse(seconds, times):
    for f in range(times):
        image_name = takeImage()
        uploadImage(image_name)
        sleep(seconds)
     
#print('Start!')
timelapse(60, 420)

#start_stream()
print('Done!')