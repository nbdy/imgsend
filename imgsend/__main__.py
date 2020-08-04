from argparse import ArgumentParser

from imgsend import ImageSender


def main():
    ap = ArgumentParser()
    ap.add_argument("-u", "--url", required=True, type=str, help="url with endpoint to send image to")
    ap.add_argument("-r", "--resolution", default="1920x1080", type=str, help="default: '1920x1080'")
    ap.add_argument("-e", "--every-x-seconds", default=30, type=int, help="how often to capture/send an image")
    a = ap.parse_args()

    res = a.resolution.split('x')
    res = (int(res[0]), int(res[1]))

    img_sender = ImageSender(a.url, a.every_x_seconds, res)
    img_sender.start()
    try:
        img_sender.join()
    except KeyboardInterrupt:
        img_sender.stop()


if __name__ == '__main__':
    main()
