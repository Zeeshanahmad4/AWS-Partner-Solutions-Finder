# coding: utf-8
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import unicodecsv as csv


def link_assembler(file_path, name):
    fieldnames = ['Grade']

    with open(file_path, "ab") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Grade": name,
        })



options = Options()
options.headless = False
#PROXY = "36.67.23.117:8888" # IP:PORT or HOST:PORT
#options.add_argument('--proxy-server=%s' % PROXY)
driver = selenium.webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(10000)
e = 100
d = 7900
for i in range(80):
    d += e
    driver.get("https://aws.amazon.com/partners/find/results/?size=100&start={}&sort=Relevance&view=Grid".format(d))
    sleep(20)
    zpath = driver.find_element_by_xpath("//*[@id='psf-search-results-da-wrapper']/div[2]/div[3]/div[1]")
    child_elements = zpath.find_elements_by_class_name("psf-partner-name")
    for i in child_elements:
        b = i.find_element_by_tag_name("a")
        c = b.get_attribute("href")
        link_assembler("links.csv",c)
        print("done till {}".format(d))


