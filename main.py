import dearpygui.dearpygui as dpg;
from win32api import GetSystemMetrics;
import node;
from editor import Editor;

width = GetSystemMetrics(0);
height = GetSystemMetrics(1);

editorObj = Editor();
    
dpg.create_context()
dpg.create_viewport(width=width,height=height,x_pos=0,y_pos=0)
dpg.setup_dearpygui();

def link_callback(sender, app_data):
    # get aliases for the given linked attributes (tags)
    aliasOne = dpg.get_item_alias(app_data[0]);
    aliasTwo = dpg.get_item_alias(app_data[1]);
    # create link
    tag = dpg.add_node_link(app_data[0], app_data[1], parent=sender)
    # add link to editor
    editorObj.add_link(tag, aliasOne, aliasTwo);

with dpg.window(width=width,height=height,label="Node Editor",pos=[0,0],no_title_bar=True,no_move=True,no_bring_to_front_on_focus=True):
    with dpg.menu_bar(label='MenuBar'):
        with dpg.menu(label='Add'):
            dpg.add_menu_item(tag='add_node_scrape_url',label='Scrape Url',callback=lambda:editorObj.add_node(node.ScrapeNode(label="Scrape URL",parent=editorObj.tag)))
            dpg.add_menu_item(tag='add_node_extract_data',label='Extract Data',callback=lambda:editorObj.add_node(node.ExtractNode(label="Extract Data",parent=editorObj.tag)))
    dpg.add_node_editor(tag=editorObj.tag,minimap=True,menubar=False, minimap_location=dpg.mvNodeMiniMap_Location_BottomRight, width=width-15, height=height-55, callback=link_callback);

# register key press handlers
with dpg.handler_registry():
    for hotkey in editorObj.hotkeys:
        dpg.add_key_press_handler(hotkey.key, callback=hotkey.callback);

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()