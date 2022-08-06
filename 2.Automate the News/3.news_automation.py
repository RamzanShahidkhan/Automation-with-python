from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# application_path = os.path.dirname(sys.executable)
application_path = 'C:/Users/mramz/Desktop/CourseraCourses_updated/Automation with python/2.Automate the News'
now = datetime.now()
month_day_year = now.strftime("%m-%d-%y")     # MMDDYYYY


website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/mramz/Desktop/CourseraCourses_updated/Automation with python/chromedriver"

# headless-mode
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

titles = []
subtitles = []
links = []
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link':links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline--{month_day_year}.csv'
print('apppath: ', application_path)
file_path = os.path.join(application_path, file_name)
df_headlines.to_csv(file_path)

driver.quit()
