import requests
import loguru
import os

logger = loguru.logger


def get_status_web(url):

    ok_codes = ["200", "301", "302"]

    try:
        print("start")
        get_url = requests.head(f"https://{url}", timeout=10)
        if get_url.status_code in ok_codes:
            return 0
    except requests.exceptions.Timeout as e:
        logger.error("Timeout")
    except requests.exceptions.TooManyRedirects as e:
        logger.error("TooManyRedirects")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_status_ping(host):
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")

    return response
