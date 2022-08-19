import requests
from pprint import pprint


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        pprint(response)
    except requests.exceptions.ConnectionError:
        print("[!] -------- Please, check your connection!")



def main():
    ip = input('Please, enter a target IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
