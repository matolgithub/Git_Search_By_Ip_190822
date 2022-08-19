import requests
from pprint import pprint
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        pprint(response)

        data = {
            'IP': response.get('query'),
            'Coutry': response.get('country'),
            'Region': response.get('regionName'),
            'City': response.get('city'),
            'Provider': response.get('isp'),
            'Lat': response.get('lat'),
            'Lon': response.get('lon')
        }

        for k, v in data.items():
            print(f"{k} : {v}")

        area = folium.Map(location=[data['Lat'], data['Lon']])
        area.save(f"{data['IP']}_{data['City']}.html")

    except requests.exceptions.ConnectionError:
        print("[!] -------- Please, check your connection!")


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText("IP INFO"))
    ip = input('Please, enter a target IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
