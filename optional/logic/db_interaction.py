import dearpygui.dearpygui as dpg
import requests
# http://192.168.1.26:8000
# https://requests.readthedocs.io/en/latest/

def print_products(): #check dpg!
    url_get_products = 'http://192.168.1.26:8000/produtos'

    confirm_access = dpg.get_value('token_get_products')

    auth_header = {
        'Authorization': f'Bearer {confirm_access}'
    }

    response = requests.get(url_get_products, headers=auth_header)
    if response.status_code == 200:
        dpg.set_value('output_get_products', "")
        
        for item in response.json():
            dpg.set_value('output_get_products', dpg.get_value('output_get_products') + f'{item}\n')

    else:
        # print('status code: ', response.status_code)
        # print('responde body: ', response.text)
        dpg.set_value('feedback_status_get_p', response.status_code)
        dpg.set_value('feedback_text_get_p', response.text)
# print_products()


def add_product(): # check dpg!
    url_add_product = 'http://192.168.1.26:8000/produto'

    produto = dpg.get_value('name_product_add')
    valor = dpg.get_value('valueF_product_add')
    estoque = dpg.get_value('valueI_product_add')

    confirm_access = dpg.get_value('auth_token_insert')

    auth_header = {
        'Authorization': f'Bearer {confirm_access}'
    }
    payload = {
        "produto": produto,
        "valor": valor,
        "estoque": estoque
    }

    response = requests.post(url_add_product, json=payload, headers=auth_header)
    
    if response.status_code == 200:
        # print("adição concluída!")
        dpg.set_value('feedback_200_insert', 'adição concluída!')
    
    else:
        # print('status code: ', response.status_code)
        # print('responde body: ', response.text)
        dpg.set_value('status_code_insert', response.status_code)
        dpg.set_value('response_text_insert', response.text)
# add_product()


def up_to_date_products(): #check dpg!
    url_update_product = 'http://192.168.1.26:8000/produto'

    produto = dpg.get_value('name_product_update')
    valor = dpg.get_value('valueF_product_update')
    estoque = dpg.get_value('valueI_product_update')

    confirm_access = dpg.get_value('auth_product_update')

    auth_header = {
        'Authorization': f'Bearer {confirm_access}'
    }
    payload = {
        "produto": produto,
        "valor": valor,
        "estoque": estoque
    }

    response = requests.put(url_update_product, json=payload, headers=auth_header)
    
    if response.status_code == 200:
        # print("atualização concluída!")
        dpg.set_value('feedback_p_update', 'atualização concluída!')
    
    else:
        # print('status code: ', response.status_code)
        # print('responde body: ', response.text)
        dpg.set_value('feedback_status_code_up', response.status_code)
        dpg.set_value('feedback_text_up', response.text)

# up_to_date_products()


def get_rid_of_product():
    ask = int(input("digite o id do produto a ser deletado: "))
    url_delete_product = f'http://192.168.1.26:8000/produto/{ask}'

    confirm_access = str(input("> "))

    auth_header = {
        'Authorization': f'Bearer {confirm_access}'
    }

    response = requests.delete(url_delete_product, headers=auth_header)

    if response.status_code == 200:
        print("atualização concluída!")
    
    else:
        print('status code: ', response.status_code)
        print('responde body: ', response.text)

# get_rid_of_product()