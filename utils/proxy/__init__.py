import os
from termcolor import colored
from time import sleep
from random import choice
import requests
from selenium import webdriver


def init_proxy(path):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    driver.get("https://www.sslproxies.org/")
    tbody = driver.find_element_by_tag_name("tbody")
    cell = tbody.find_elements_by_tag_name("tr")
    
    proxy_list = []
    for column in cell:
        column = column.text.split(" ")
        proxy = column[0]+":"+column[1]
        print(colored(proxy,'yellow'))
        proxy_list.append(proxy)

    driver.quit()
    print("")

    os.system('clear')
    os.system('cls')

    # Proxy Connection

    print(colored('Getting Proxies from graber...','green'))
    sleep(2)
    os.system('clear')
    os.system('cls')
    target_proxy = choice(proxy_list)
    proxy = {"http": "http://"+ target_proxy}
    url = 'https://mobile.facebook.com/login'
    r = requests.get(url,  proxies=proxy)
    print("")
    print(colored('Connecting using proxy' ,'green'))
    print("")
    sts = r.status_code

    print(colored(f'Proxy: {target_proxy} \nStatus: {sts}' ,'green'))
    if sts == 200:
        return target_proxy
