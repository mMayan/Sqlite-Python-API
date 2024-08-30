import dearpygui.dearpygui as dpg
import logic.all_dpg.dpg_callbacks as cbk

dpg.create_context()
dpg.create_viewport(title='API interaction', width=900, height=500)

with dpg.viewport_menu_bar():
    
    with dpg.menu(label="acesso"):
        dpg.add_menu_item(label="cadastro e login", callback=cbk.login_register)

    with dpg.menu(label='visualização'):
        dpg.add_menu_item(label='produtos', callback=cbk.get_products)
        dpg.add_menu_item(label='usuários', callback=cbk.get_users)

    with dpg.menu(label='inserção'):
        dpg.add_menu_item(label="produtos", callback=cbk.add_dpg_product)

    with dpg.menu(label='atualização'):
        dpg.add_menu_item(label='produtos e usuários', callback=cbk.update_products_users)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
