import requests
import pandas as pd
import codecs

from bs4 import BeautifulSoup

# import csv

# from multiprocessing import Pool


def get_html(url):
    r = requests.get(url) #response
    return r.text #возвращает html код страницы(url)


def get_all_links(html,arr):

    soup = BeautifulSoup(html, 'html5lib').find('div', class_='block_cars')
    for i in soup.find_all('a', href=True):
        d = {}
        d['name'] = i.text.strip()
        d['link'] = 'https://avto-dvorniki.ru'+i['href']
        d['path'] = i.text.strip()
        d['was'] = False
        arr.append(d)
    print(arr)

    p_path = []
    p_name = []
    p_dvornik_name = []
    p_link = []

    for i in arr:
        if "http" in i["link"]:
            r = requests.get(i['link'])
            print('sasha', i['link'])
        else:
            link = 'https://avto-dvorniki.ru' + i['link']
            print(link)
            r = requests.get(link)
            print('aika', link)
            # soup = BeautifulSoup(r.text, 'html5lib').find('div', class_='block_cars')
        if BeautifulSoup(r.text, 'html5lib').find('td', class_="cennik"):
            print("Это конечная страница")

            car_title = BeautifulSoup(r.text, 'html5lib').find('h1', class_="active").text.strip()
            dvornik_title = BeautifulSoup(r.text, 'html5lib').find('div', class_="positions")
            dvornik_list = ''
            for sa in dvornik_title.find_all('a', class_='name'):
                dvornik_list = dvornik_list + ',' + sa.text.strip()

            print(car_title)
            print(dvornik_list)

            p_path.append(i["path"])
            p_name.append(car_title)
            p_dvornik_name.append(dvornik_list)
            p_link.append(link)
            # print(i["path"],i["link"], "oil title", oil_title)
        else:
            soup = BeautifulSoup(r.text, 'html5lib').find('div', class_='block_cars')
            for k in soup.find_all('a', href=True):
                m = {}
                m['name'] = k.text.strip()
                m['link'] = k['href']
                m["path"] = i["path"] + "," + k.text.strip()
                m['was'] = False
                if m["path"] == i["path"] + ",":
                    pass
                elif '/car/' in m['link']:
                    arr.append(m)
                else:
                    pass
                #print(m)
        i['was'] = True

    df = pd.DataFrame({"path":p_path, "link": p_link, "name": p_name, "dvornik": p_dvornik_name})
    df.to_csv("results-dv.csv")
    df.to_excel("results-dv.xls")
    return arr


def main():
    url = 'https://avto-dvorniki.ru'
    links = []
    all_links = get_all_links(get_html(url), links)
    #print(all_links)


if __name__ == '__main__':
    main()
