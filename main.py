import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now!!",
            message="it is beneficial for you",
            app_icon="icon.ico",
            timeout=10
        )
        time.sleep(60*60)