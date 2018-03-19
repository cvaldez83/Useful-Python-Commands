import bs4
import requests

URL = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1521309704&sr=8-1&keywords=automate+the+boring+stuff+with+python'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
res = requests.get(URL,headers=headers)
res.raise_for_status()
print('status code: ' + str(res.status_code))

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

# return elems[0].text.strip()

