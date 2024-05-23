#problem 4 of task 2 which is application health checker

import requests
import time


def check_application_status(url, check_interval=60):

    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{time.ctime()}: The application is up.")
            else:
                print(f"{time.ctime()}: The application is down. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{time.ctime()}: The application is down. Error: {e}")

        time.sleep(check_interval)


if __name__ == "__main__":
    application_url = "https://www.flipkart.com/"
    check_interval_seconds = 30

    check_application_status(application_url, check_interval_seconds)
