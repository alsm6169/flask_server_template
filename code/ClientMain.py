import requests
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

res = requests.get('http://127.0.0.1:5000/')
print('status_code: ', res.status_code, ', status_msg: ', res.text)


res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_list')
if res.status_code == 200:
    res_df = pd.read_json(res.text, orient='records')
    print('------------film_list------------')
    print(res_df.head(7))
else:
    print('status_code: ', res.status_code, ', status_msg: ', res.text)


res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_info?title=Ali Forever')
if res.status_code == 200:
    res_df = pd.read_json(res.text, orient='records')
    print('------------film_info------------')
    print(res_df)
else:
    print('status_code: ', res.status_code, ', status_msg: ', res.text)


res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_actors?title=Ali Forever')
if res.status_code == 200:
    res_df = pd.read_json(res.text, orient='records')
    print('------------film_actors------------')
    print(res_df)
else:
    print('status_code: ', res.status_code, ', status_msg: ', res.text)
