from selenium import webdriver
import time


def GeoCoordinates(URL):
    z = 0
    try:
        while z <= 10:
            z += 1
            coordinates = []
            acoordinates = []
            chrome_path = r"C:\Users\Ericlameguy\Desktop\chromedriver_win32 (1)\chromedriver.exe"
            driver = webdriver.Chrome(chrome_path)
            driver.get(URL)
            html = driver.execute_script("return document.documentElement.innerHTML;")

            newhtml = html.split("https://maps.google.com/maps/@", 1)[1]
            coordinates.append(float(newhtml.split(',')[0]))
            coordinates.append(float(newhtml.split(',')[1]))


            print(coordinates)
    except IndexError:
        print("I N D E X  ERROR !!! ")
        time.sleep(100)



GeoCoordinates("https://geoguessr.com/world/play")