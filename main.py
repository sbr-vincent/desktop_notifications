import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()


def getdata(url):
    r = requests.get(url)
    return r.text


html_data = getdata("https://weather.com/weather/today/l/dfc4e6afa411ece7b590b75451125bd821dba3eb88b10afd5bfd02acff70e278")

soup = BeautifulSoup(html_data, "html.parser")

current_temp = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")
moon_phase = soup.find_all("div", class_="WeatherDetailsListItem--wxData--kK35q")

temp = str(current_temp[0].get_text())
moon = str(moon_phase[-1].get_text())

result = "current_temp " + temp + " in Irvine" + "\n" + "Moon Phase: " + moon

n.show_toast("Weather Update", result, duration=10)