import dearpygui.dearpygui as dpg
import requests
# http://192.168.1.26:8000
# https://requests.readthedocs.io/en/latest/

def register_user(): # check dpg!
    url_register = 'http://192.168.1.26:8000/register'
    
    username = dpg.get_value('name_user_register')
    password = dpg.get_value('password_user_register')

    response = requests.post(url_register, json={'username': username, 'password': password})

    if response.status_code == 200:
        dpg.set_value('feedback_register_200', 'cadastro bem sucedido!')



def login_user(): # check dpg!
    url_login = 'http://192.168.1.26:8000/login'


    username = dpg.get_value('name_user_login')
    password = dpg.get_value('password_user_login')


    response = requests.post(url_login, json={'username': username, 'password': password})

    if response.status_code == 200:
        token = response.json().get('access_token')
        # print(f"token de acesso: {token}")
        dpg.set_value('token_feedback_login', token)
    
    else: 
        # print("usuário ou senha incorretos")
        # print('status code: ', response.status_code)
        # print('response body: ', response.text)
        dpg.set_value('feedback_user_pass_incorrect', "usuário ou senha incorretos!")
        dpg.set_value('feedback_status_code', response.status_code)
        dpg.set_value('feedback_response_body', response.text)



def delete_user():
    ask = int(input("digite o id do usuário a ser deletado: "))
    url_delete = f'http://192.168.1.26:8000/login/{ask}'

    confirm_access = str(input("> "))

    auth_header = {
        "Authorization": f'Bearer {confirm_access}'
    }

    response = requests.delete(url_delete, headers=auth_header)

    if response.status_code == 200:
        print('o delete foi feito com sucesso!')
    else:
        print('falhou ao deletar o usuário')
        print('status code: ', response.status_code)
        print('responde body: ', response.text)


def get_all_users():
    url_get_users = 'http://192.168.1.26:8000/userget'
    
    confirm_access = dpg.get_value('token_get_users')

    auth_header = {
        "Authorization": f'Bearer {confirm_access}'
    }

    response = requests.get(url_get_users, headers=auth_header)

    if response.status_code == 200:
        dpg.set_value('output_get_users', "")
        
        for item in response.json():
            dpg.set_value('output_get_users', dpg.get_value('output_get_users') + f'{item}\n')

    else:
        # print('status code: ', response.status_code)
        # print('response body ', response.text)
        dpg.set_value('status_get_users', response.status_code)
        dpg.set_value('text_get_users', response.text)




def up_to_date_users():
    url_update_users = 'http://192.168.1.26:8000/userup'
    
    username = str(input("nome do usuário: "))
    password = str(input("senha: "))

    confirm_access = str(input("> "))

    auth_header = {
        'Authorization': f'Bearer {confirm_access}'
    }

    payload = {
        "username": username,
        "password": password
    }

    response = requests.put(url_update_users, json=payload, headers=auth_header)

    if response.status_code == 200:
        print("atualização concluída!")
    
    else:
        print('status code: ', response.status_code)
        print('responde body: ', response.text)

