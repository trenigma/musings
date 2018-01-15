
## Your unique URL is http://py4e-data.dr-chuck.net/comments_16873.html
## The sample URL is http://py4e-data.dr-chuck.net/comments_42.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
span_texts = soup('span')

nums = []

for span in span_texts:
    nums.append(int(span.string))
    print(sum(nums))