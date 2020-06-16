import requests
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def display_results(result, url):
    if result.status_code == 200:
        res_df = pd.read_json(result.text, orient='records')
        print(f'------------{url}------------')
        print(res_df.head(7))
    else:
        print('status_code: ', result.status_code, ', status_msg: ', result.text)


# res = requests.get('http://127.0.0.1:5000/')
# print('status_code: ', res.status_code, ', status_msg: ', res.text)

'''RAW SQL based queries'''
res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_list')
display_results(res,'film_list_rawsql')

# res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_info?title=Ali Forever')
# display_results(res,'film_info_rawsql')
#
# res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_actors?title=Ali Forever')
# display_results(res,'film_actors_rawsql')

# '''ORM Object based queries'''
res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_list_orm')
display_results(res,'film_list_orm')

res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_info_orm?title=Alaska Phantom')
display_results(res,'film_info_orm')

res = requests.get('http://127.0.0.1:5000/module/v01/functions/film_actors_orm?title=Alaska Phantom')
display_results(res,'film_actors_orm')

#res = requests.get('http://127.0.0.1:5000/module/v01/functions')
res = requests.get('http://127.0.0.1:5000')
print('status_code: ', res.status_code, ', status_msg: ', res.text)
