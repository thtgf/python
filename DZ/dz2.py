import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text



def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("div", class_="plugin-card")
    for el in elements:
        try:
            name = el.find("h3", class="entry-title").text
        except AttributeError:
            name =""


        try:
            url =el.find"h3",class_="entry-title").find('a').get("href")
        except AttributeError:
            url = ""
        print(name)




def main():
    url = "https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()