import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text



def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    p1 = soup.find_("header", id="masthead").find("p",class_="site-description")
    return p1




def main():
    url = "https://ru.wordpress.org/"
    print(get_data(get_html(url)))