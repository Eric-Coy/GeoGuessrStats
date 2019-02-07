from selenium import webdriver
from pygeocoder import Geocoder
from selenium.webdriver.chrome.options import Options
import pickle
import operator
import sched, time
timed = sched.scheduler(time.time, time.sleep)
def GeoCoordinates(URL):
    z = 0
    Country_Dictionary = pickle.load(open("Countries_.p", "rb"))
    while z < 10:
        z += 1
        time.sleep(2)
        coordinates = []
        acoordinates = []
        chrome_path = r"C:\Users\Ericlameguy\Desktop\chromedriver_win32 (1)\chromedriver.exe"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_path, chrome_options=options)
        driver.get(URL)
        html = driver.execute_script("return document.documentElement.innerHTML;")

        newhtml = html.split("https://maps.google.com/maps/@",1)[1]
        coordinates.append(float(newhtml.split(',')[0]))
        coordinates.append(float(newhtml.split(',')[1]))

        acoordinates.append(coordinates)
        result = Geocoder.reverse_geocode(*acoordinates[0])

        Country = result.country

        driver.quit()
        if Country not in Country_Dictionary:
            Country_Dictionary[Country] = 1
        elif Country in Country_Dictionary:
            Country_Dictionary[Country] += 1

    for key, value in sorted(Country_Dictionary.items(), key=operator.itemgetter(0)):
        print(key, value)

    pickle.dump(Country_Dictionary, open("Countries_.p","wb"))


GeoCoordinates("https://geoguessr.com/world/play")

