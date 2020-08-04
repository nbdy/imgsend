## imgsend
send an image from your picamera to an api endpoint every x seconds

### how to..
#### ... install
```shell script
sudo pip3 install https://github.com/smthnspcl/imgsend
```
#### ... use from cli
```shell script
usage: imgsend [-h] -u URL [-r RESOLUTION] [-e EVERY_X_SECONDS]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     url with endpoint to send image to
  -r RESOLUTION, --resolution RESOLUTION
                        default: '1920x1080'
  -e EVERY_X_SECONDS, --every-x-seconds EVERY_X_SECONDS
                        how often to capture/send an image

ex.: imgsend -u https://eberlein.io/api/image_collector -r 800x600 -e 5
                  \> url to send to                         \         \> every 5 seconds
                                                             \> resoultion
```
#### ... use from code
```python
from imgsend import ImageSender
sender = ImageSender("https://eberlein.io/api/image_collector", 5, (800, 600))
sender.start()
```