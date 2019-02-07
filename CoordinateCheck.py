
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import sched, time

z=0
try:

    while z < 1:
        z += 1
        time.sleep(2)
        coordinates = []
        acoordinates = []
        chrome_path = r"C:\Users\Ericlameguy\Desktop\chromedriver_win32 (1)\chromedriver.exe"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_path, chrome_options=options)
        driver.get("https://geoguessr.com/world/play")
        html = driver.execute_script("return document.documentElement.innerHTML;")

        newhtml = html.split("https://maps.google.com/maps/@", 1)[1]
        coordinates.append(float(newhtml.split(',')[0]))
        coordinates.append(float(newhtml.split(',')[1]))

        print(newhtml[:40])
        print(coordinates)
        print(html)

except IndexError:
    print("I N D E X  E R R O R!!!!!!!!!!!!!!")
    print(html)