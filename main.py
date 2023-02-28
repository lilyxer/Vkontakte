import requests
import time
from datetime import datetime

def pars_name_and_bdate(res):
    """Смотрим есть ли дата рождения у юзера, если есть - возвращаем кортеж из имени и даты"""
    time.sleep(1)
    reg_f = r'%d.%m.%Y'
    reg_l = r'%d.%m'
    for i in res.json()['response']:
        if 'bdate' in i:
            date = (datetime.strptime(i['bdate'], reg_f) if len(i['bdate']) > 
                    5 else datetime.strptime(i['bdate'], reg_l))
            return date.strftime('%d.%b'), i['first_name'], i['last_name']
        
token =  input('Input token: ')
id_group = input('Input name or id group: ')  # 'presny_moscow'
method = 'groups.getMembers' # choice method
version_vk = 5.131 # 28/02/2023

param = {'access_token': token,
         'v': version_vk, 
         'group_id': id_group}

answer_of_get = requests.get(url=f'https://api.vk.com/method/{method}', params=param)
print('получаем ответ от группы...')
if answer_of_get.status_code == 200:
    data = answer_of_get.json()
    print('Бежим по айдишникам...')
    for users in data['response']['items']:
        user_id = {'access_token': token,
                'v': version_vk, 
                'user_ids': users,
                'fields': 'bdate'}
        r_user = pars_name_and_bdate(
            res = requests.get(url=f'https://api.vk.com/method/users.get', params=user_id))
        if r_user:
            print(*r_user)
            

