# coding: utf-8

import requests

url = "http://localhost:20000"
params = {
	'email': 'a@b.c'		
}

headers = {
	'User-agent': 'none/ofyourbusiness',
	'Spam': 'Eggs'
}

resp = requests.post(url, data=params, headers=headers)
text = resp.text

print(text)
