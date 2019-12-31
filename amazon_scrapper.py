import requests
from bs4 import BeautifulSoup

asin = "B07BG4XN2R"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

url = f"https://www.amazon.in/s?k={asin}&ref=nb_sb_noss"

response = requests.get(url, headers=headers)

html = BeautifulSoup(response.text, 'html.parser')

res_t = html.find_all(name="a", attrs={"class": "a-link-normal", "target": "_blank"})

url_list = list()
for i in res_t:
    url_list.append(i.attrs['href'])
final_url = f"https://www.amazon.in/{max(set(url_list), key=url_list.count)}"

res_a = html.find_all(name="span", attrs={"class": "a-price-whole"})
print(res_a[0].string)
