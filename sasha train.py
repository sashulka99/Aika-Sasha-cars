import requests
import pandas as pd
import codecs

from bs4 import BeautifulSoup

import csv

from multiprocessing import Pool


def get_html(url):
    r = requests.get(url) #response
    return r.text #возвращает html код страницы(url)


def get_all_links(html,arr):

    soup = BeautifulSoup(html, 'lxml').find('div', id='public_page')
    count =0
    for i in soup.find_all('a', href=True):
        count += 1
        if count < 2:
            d = {}
            d['name'] = i.text.strip()
            d['link'] = i['href']
            d['path'] = i.text.strip()
            d['was'] = False
            arr.append(d)
    print(arr)

    p_path = []
    p_name = []
    p_oil_name = []
    p_link = []

    count = 0

    for i in arr:
        if "http" in i["link"]:
            r = requests.get(i['link'])
            print('sasha', i['link'])
        else:
            link = 'http://avtobukvar.ru/' + i['link']
            print(link)
            r = requests.get(link)
            print('aika', link)
        # soup = BeautifulSoup(r.text, 'lxml').find('div', class_="oil_title")
        if BeautifulSoup(r.text, 'lxml').find('div', class_="recommendation_product_title"):
            print("Это конечная страница")
            count += 1
            if count > 20:
                break
            car_title = BeautifulSoup(r.text, 'lxml').find('h4', class_="name_brand_left").text.strip()
            oil_title = BeautifulSoup(r.text, 'lxml').find('div', class_="recommendation_product_title").text.strip()
            oil_title = str(oil_title).encode().decode("cp1251").encode("utf8")
            print(oil_title)
            # oil_title = codecs.ascii_decode(oil_title, "cp1251")
            p_path.append(i["path"])
            p_name.append(car_title)
            p_oil_name.append(oil_title)
            p_link.append(link)
            #print(i["path"],i["link"], "oil title", oil_title)
        else:
            soup = BeautifulSoup(r.text, 'lxml').find('div', id='public_page')
            for k in soup.find_all('a', href=True):
                m = {}
                m['name'] = k.text.strip()
                m['link'] = k['href']
                m["path"] = i["path"] + "," + k.text.strip()
                m['was'] = False
                arr.append(m)
                #print(m)
        i['was'] = True

    df = pd.DataFrame({"path":p_path, "link": p_link, "name":p_name, "oil": p_oil_name})
    df.to_csv("results.csv")
    df.to_excel("results.xls")
    return arr


def main():
    url = 'http://www.avtobukvar.ru/servise/podbor_masla_po_marke_avtomobilya.html'
    links = []
    all_links = get_all_links(get_html(url), links)
    #print(all_links)


if __name__ == '__main__':
    main()