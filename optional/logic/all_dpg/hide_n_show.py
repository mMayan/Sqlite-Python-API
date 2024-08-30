import dearpygui.dearpygui as dpg

def hide_all_windows():
    window_tags = [
        'register_window',    
        'login_window',    
        'window_INSERT_products',    
        'window_GET_products',    
        'window_GET_output',    
        'window_get_users',    
        'window_GET_output_users',    
        'window_update_product',    
        'window_update_users',    
        'window_delete_product',    
        'window_delete_user'
    ]
    
    for tag in window_tags:
        if dpg.does_item_exist(tag):
            dpg.hide_item(tag)
