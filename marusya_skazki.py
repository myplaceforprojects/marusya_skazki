import selenium
import pandas as pd
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()

url = 'https://marusia.vk.com/skill/tales'
browser.get(url)

# прожимаем нужное количество раз на кнопку "загрузить ещё", чтобу отобразить список всех досутпных сказок
for page in range (33):
    try:
        knopka = browser.find_element(By.CLASS_NAME, 'load-more__button').click()
    except NoSuchElementException:
        browser.forward()
    sleep(2)
sleep(5)

# находим все сказки
skazki = browser.find_elements(By.CLASS_NAME, 'tab-table__item')
# print(skazki)

data = []

# проходимся по каждой записи (сказке) и сохраняем её данные
for skazka in skazki:
    name = skazka.find_elements(By.CLASS_NAME, 'tab-table__item-value')[0].text
    author = skazka.find_elements(By.CLASS_NAME, 'tab-table__item-value')[1].text
    dlina = skazka.find_elements(By.CLASS_NAME, 'tab-table__item-value')[2].text
 
    print(name, author, dlina)

    data.append([name, author, dlina])

print(data)


# для выгрузки соствляем заголовок в таблицу, и записываем данные в таблицу
handler = ['Название сказки', 'Авторство', 'Продолжительность']

df = pd.DataFrame(data, columns=handler)
df.to_csv('C:/Users/tsman/skazki_alisa.csv', sep=';', encoding='utf-8-sig')


