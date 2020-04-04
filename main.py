import bs4
import requests

url_mlg = 'https://jadwalsholat.pkpu.or.id/?id=142'
response = requests.get(url_mlg)
contents = bs4.BeautifulSoup(response.text, "html.parser") #this parse for BeautifulSoup

datas = contents.find('table', {'class', 'table_adzan'}) #get tabel with table_adzan class
datas=datas.find_all('tr', {'class':['table_light', 'table_dark']}) #get data adzan
for  data in datas:
    print(data)
    for _data in data:
        print(_data)
        print(_data.get_text())
