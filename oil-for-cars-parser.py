import requests
import pandas as pd
# import codecs

from bs4 import BeautifulSoup

# import csv
# from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html, arr):
    soup = BeautifulSoup(html, 'html5lib')
    public_page = soup.find('div', id='public_page')
    for i in public_page.find_all('a', href=True):
        d = {}
        d['name'] = i.text.strip()
        print(d['name'])
        d['link'] = i['href']
        d['path'] = i.text.strip()
        d['was'] = False
        arr.append(d)
    print(arr)
    p_path = []
    p_name = []
    p_oil_name = []
    p_link = []

    for i in arr:
        if 'http' in i['link']:
            r = requests.get(i['link'])
            print('sasha', i['link'])
        else:
            link = 'http://avtobukvar.ru/' + i['link']
            print(link)
            r = requests.get(link)
            print('aika', link)
        if BeautifulSoup(r.text, 'html5lib').find('div', class_="recommendation_product_title"):
            print("Это конечная страница")

            car_title = BeautifulSoup(r.text, 'html5lib').find('h4', class_="name_brand_left").text.strip()
            oil_title = BeautifulSoup(r.text, 'html5lib').find('div', class_="recommendation_product_title").text.strip()
            oil_title = str(oil_title)
            print(oil_title)
            p_path.append(i['path'])
            p_name.append(car_title)
            p_oil_name.append(oil_title)
            p_link.append(link)
        else:
            soup = BeautifulSoup(r.text, 'html5lib').find('div', id='public_page')
            for k in soup.find_all('a', href=True):
                m = {}
                m['name'] = k.text.strip()
                m['link'] = k['href']
                m['path'] = i['path'] + ',' + k.text.strip()
                m['was'] = False
                arr.append(m)
        i['was'] = True

    df = pd.DataFrame({"path": p_path, "link": p_link, "name": p_name, "oil": p_oil_name})
    df.to_csv("results.csv")
    df.to_excel("results.xls")
    return arr


def main():
    url = 'http://www.avtobukvar.ru/servise/podbor_masla_po_marke_avtomobilya.html'
    links = []
    all_links = get_all_links(get_html(url), links)
    # print(all_links)


if __name__ == '__main__':
    main()