import requests as req
from bs4 import BeautifulSoup
import json, urllib3, pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Getting URLs...")
url = "https://www.daraz.pk/"

resp = req.get(url, verify=False).text

soup = BeautifulSoup(resp, "html.parser")
data = soup.find_all("script", {"class": "J_PageData"})
a = json.loads(data[0].get_text())
for i in a:
	for s in a["nuj"]["product"]:
		urls = s["itemUrl"].replace("//", "")
		with open("daraz_products.txt", "a+") as f:
			f.write(urls + "\n")
print("Done.")