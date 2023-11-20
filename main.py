import bs4
import pandas as pd
import pyautogui
import requests

if __name__ == '__main__':
    domain = 'https://www.blognone.com'

    page = 1
    name_list = []
    price_list = []

    while page <= 5:
        uri = f'/node'
        if page != 1:
            uri += f'?page={page}'
        data = requests.get(f'{domain}{uri}')
        soup = bs4.BeautifulSoup(data.text, features="html.parser")

        for c in soup.findAll('div', {'class': 'node clearfix'}):
            name_list.append(c.find('a').text)

        page += 1

    # print(len(name_list))
    count = 1
    for name in name_list:
        print(f'[{count}] {name}')
        count += 1

    table = pd.DataFrame([name_list]).transpose()
    table.columns = ['name']
    table.set_index('name')
    table.to_excel('Blognone.xlsx', engine='openpyxl')

    print(pyautogui.size())
    print(pyautogui.position())
    pyautogui.moveTo(1000, 1000, duration=1)

    print(pyautogui.position())

    print('completed')
