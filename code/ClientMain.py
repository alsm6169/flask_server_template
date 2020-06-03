import sys
import json
import requests
import pandas as pd

res = requests.get('http://127.0.0.1:5000/')
print('status_code: ', res.status_code, ', status_msg: ', res.text)

res = requests.get('http://127.0.0.1:5000/module/v01/functions/whatisthere')
print('status_code: ', res.status_code, ', status_msg: ', res.text)