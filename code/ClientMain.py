import requests
import pandas as pd

# res = requests.get('http://127.0.0.1:5000/')
# print('status_code: ', res.status_code, ', status_msg: ', res.text)

# res = requests.get('http://127.0.0.1:5000/module/v01/functions/actor_list_alchemy_df')
# if res.status_code == 200:
#     res_df = pd.read_json(res.text, orient='records')
#     print(res_df.tail(7))
# else:
#     print('status_code: ', res.status_code, ', status_msg: ', res.text)

# res = requests.get('http://127.0.0.1:5000/module/v01/functions/actor_list_rawsql_pd')
# if res.status_code == 200:
#     res_df = pd.read_json(res.text, orient='records')
#     print(res_df.head(7))
# else:
#     print('status_code: ', res.status_code, ', status_msg: ', res.text)

res = requests.get('http://127.0.0.1:5000/module/v01/functions/actor_list_alchemy_json')
print('status_code: ', res.status_code, ', status_msg: ', res.text)