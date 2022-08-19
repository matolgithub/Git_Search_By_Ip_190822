import requests
from pprint import pprint
from pyfiglet import Figlet
import folium


class MapIpSearcher:
    def __init__(self, ip='127.0.0.1'):
        self.ip = ip

    def get_info_by_ip(self):
        try:
            response = requests.get(url=f"http://ip-api.com/json/{self.ip}").json()
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
            folium.CircleMarker(location=[data['Lat'], data['Lon']], radius=5).add_to(area)
            area.save(f"{data['IP']}_{data['City']}.html")

        except requests.exceptions.ConnectionError:
            print("[!] -------- Please, check your connection!")

    def main(self):
        preview_text = Figlet(font='slant')
        print(preview_text.renderText("IP INFO ON THE MAP!"))
        ip = input('Please, enter a target IP: ')

        MapIpSearcher.get_info_by_ip(MapIpSearcher(ip=ip))


if __name__ == '__main__':
    map_ip_object = MapIpSearcher()
    map_ip_object.main()
