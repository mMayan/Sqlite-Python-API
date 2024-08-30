import dearpygui.dearpygui as dpg
import logic.user_interaction as user_inte
import logic.db_interaction as db_inte

def login_register(): # user
    if not dpg.does_item_exist('register_window'):
        # função register
        with dpg.window(label='register', width=300, height=500, tag='register_window'):
            dpg.add_text("insira os dados para cadastro:", indent=29)

            dpg.add_spacer(height=6)
            dpg.add_input_text(hint='nome', tag='name_user_register', indent=31)

            dpg.add_spacer(height=6)
            dpg.add_input_text(hint='senha', tag='password_user_register', password=True, indent=31)

            dpg.add_spacer(height=6)
            dpg.add_button(label='enviar', callback=user_inte.register_user, indent=98)

            dpg.add_spacer(height=6)
            dpg.add_text("", tag='feedback_register_200', indent=31)
    else:
        dpg.show_item('register_window')

    if not dpg.does_item_exist('login_window'):
        # função login
        with dpg.window(label='login', width=300, height=500, pos=[300], tag='login_window'):
            dpg.add_text("insira os dados para login:", indent=42)

            dpg.add_spacer(height=6)
            dpg.add_input_text(hint='nome', tag='name_user_login', indent=38)

            dpg.add_spacer(height=6)
            dpg.add_input_text(hint='senha', tag='password_user_login', password=True, indent=38)

            dpg.add_spacer(height=6)
            dpg.add_button(label='enviar', callback=user_inte.login_user, indent=111)
       
            dpg.add_spacer(height=8)
            dpg.add_text("token gerado:", indent=38)
            dpg.add_input_text(tag='token_feedback_login', default_value=dpg.get_value('token_feedback_login'), indent=38)

            # feedback de senha ou nome incorretos
            dpg.add_spacer(height=6)
            dpg.add_text("", tag='feedback_user_pass_incorrect')
            dpg.add_text("", tag='feedback_status_code')
            dpg.add_text("", tag='feedback_response_body')
    else:
        dpg.show_item('login_window')

def add_dpg_product(): # database
    if not dpg.does_item_exist('window_INSERT_products'):
        with dpg.window(label='insert', width=300, height=500, tag='window_INSERT_products'):
            dpg.add_text("insira os dados do produto", indent=42)

            dpg.add_spacer(height=6)
            dpg.add_input_text(hint='nome do produto', tag='name_product_add', indent=38)

            dpg.add_spacer(height=5)
            dpg.add_text('valor do produto:', indent=38)
            dpg.add_input_double(tag='valueF_product_add', indent=38)


            dpg.add_spacer(height=5)
            dpg.add_text("quantidade de estoque:", indent=38)
            dpg.add_input_int(tag='valueI_product_add', indent=38)


            dpg.add_spacer(height=7)
            dpg.add_input_text(hint='token de autorização', tag='auth_token_insert', indent=38)

            dpg.add_spacer(height=7)
            dpg.add_button(label='enviar', indent=100, callback=db_inte.add_product)

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_200_insert', indent=43)

            dpg.add_text("", tag='status_code_insert')
            dpg.add_text("", tag='response_text_insert')
    else:
        dpg.show_item('window_INSERT_products')

def get_products():
    if not dpg.does_item_exist('window_GET_products'):
        
        with dpg.window(label='produtos', tag='window_GET_products', width=300, height=500):
            dpg.add_spacer(height=7)
            dpg.add_text("clique abaixo para visualizar os produtos")

            dpg.add_spacer(height=7)
            dpg.add_input_text(hint='token de verificação', tag='token_get_products', indent=38)

            dpg.add_spacer(height=7)
            dpg.add_button(label='visualizar', callback=db_inte.print_products,  indent=100)

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_status_get_p')

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_text_get_p')

    else:
        dpg.show_item('window_GET_products')

    if not dpg.does_item_exist('window_GET_output'):
        with dpg.window(label='output', tag='window_GET_output', width=300, height=500, pos=[300]):
            dpg.add_text("", tag='output_get_products')
    else:
        dpg.show_item('window_GET_output')

def get_users():
    if not dpg.does_item_exist('window_get_users'):
        with dpg.window(label='usuários', tag='window_get_users', width=300, height=500):
            dpg.add_spacer(height=7)
            dpg.add_text("clique abaixo para visualizar os usuários")

            dpg.add_spacer(height=7)
            dpg.add_input_text(hint='token de verificação', tag='token_get_users', indent=38)

            dpg.add_spacer(height=7)
            dpg.add_button(label='visualizar', callback=user_inte.get_all_users,  indent=100)

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='status_get_users')

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='text_get_users')
    
    else:
        dpg.show_item('window_get_users')

    if not dpg.does_item_exist('window_GET_output_users'):
        with dpg.window(label='output', tag='window_GET_output_users', width=300, height=500, pos=[300]):
            dpg.add_text("", tag='output_get_users')

    else:
        dpg.show_item('window_GET_output_users')


def update_products_users():
    if not dpg.does_item_exist('window_update_product'):
        with dpg.window(label='produtos', width=300, height=500, tag='window_update_product'):
            dpg.add_text("insira os dados do produto para atualizar")

            dpg.add_spacer(height=6)
            dpg.add_input_text(hint='nome do produto', tag='name_product_update', indent=38)

            dpg.add_spacer(height=5)
            dpg.add_text('valor do produto:', indent=38)
            dpg.add_input_double(tag='valueF_product_update', indent=38)

            dpg.add_spacer(height=5)
            dpg.add_text("quantidade de estoque:", indent=38)
            dpg.add_input_int(tag='valueI_product_update', indent=38)

            dpg.add_spacer(height=8)
            dpg.add_input_text(hint='token de autorização', tag='auth_product_update', indent=38)

            dpg.add_spacer(height=7)
            dpg.add_button(label='enviar', indent=100, callback=db_inte.up_to_date_products)

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_p_update', indent=48)

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_status_code_up')

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_text_up')
    else:
        dpg.show_item('window_update_product')
    
    if not dpg.does_item_exist('window_update_users'):
        with dpg.window(label='usuários', width=300, height=500, pos=[300], tag='window_update_users'):
            dpg.add_text("insira o usuário para alterar a senha", indent=18)

            dpg.add_spacer(height=7)
            dpg.add_input_text(hint='usuário', indent=38, tag='user_name_update')

            dpg.add_spacer(height=7)
            dpg.add_input_text(hint='senha', password=True, indent=38, tag='user_password_update')

            dpg.add_spacer(height=7)
            dpg.add_input_text(hint='token de autorização', indent=38, tag='auth_user_update')

            dpg.add_spacer(height=7)
            dpg.add_button(label='enviar', indent=100, callback=user_inte.up_to_date_users)
            
            dpg.add_spacer(height=7)
            dpg.add_text("", tag='feedback_update_user', indent=48)

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='status_code_u_up')

            dpg.add_spacer(height=7)
            dpg.add_text("", tag='text_u_up')

    else:
        dpg.show_item('window_update_users')