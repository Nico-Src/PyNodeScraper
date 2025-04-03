import dearpygui.dearpygui as dpg;
import src.globals as globals;
from win32api import GetSystemMetrics;
import src.node as node;
from src.editor import Editor;

width = GetSystemMetrics(0);
height = GetSystemMetrics(1);

resource_manager = globals.get_resource_manager();
resource_manager.load_image('grid', r'img/grid.png');
resource_manager.load_image('none', r'img/none.jpg');
editor = Editor();
    
dpg.create_context()
dpg.create_viewport(width=width,height=height,x_pos=0,y_pos=0,title="PyNodeScraper")
dpg.set_viewport_small_icon(f'img/small.ico');
dpg.set_viewport_large_icon(f'img/large.ico');
dpg.setup_dearpygui();

accent = (75,168,50);
accent_hover = (57,128,38);
accent_active = (43,97,28);

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvNodeStyleVar_NodeCornerRounding, 10, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_GridLine, (50,50,50), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, accent, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, accent_hover, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, accent_hover, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (70,70,70), category=dpg.mvThemeCat_Nodes);
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, (70,70,70), category=dpg.mvThemeCat_Nodes);
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, (70,70,70), category=dpg.mvThemeCat_Nodes);

dpg.bind_theme(global_theme)

def link_callback(sender, app_data):
    # get aliases for the given linked attributes (tags)
    alias_one = dpg.get_item_alias(app_data[0]);
    alias_two = dpg.get_item_alias(app_data[1]);
    # create link
    tag = dpg.add_node_link(app_data[0], app_data[1], parent=sender)
    # add link to editor
    editor.add_link(tag, alias_one, alias_two);

with dpg.window(width=width,height=height,label="Node Editor",pos=[0,0],no_title_bar=True,no_move=True,no_bring_to_front_on_focus=True):
    with dpg.menu_bar(label='MenuBar'):
        with dpg.menu(label='Add'):
            dpg.add_menu_item(tag='add_node_scrape_url',label='Scrape Url',callback=lambda:editor.add_node(node.ScrapeNode(label="Scrape URL",parent=editor.tag)))
            dpg.add_menu_item(tag='add_node_extract_data',label='Extract Data',callback=lambda:editor.add_node(node.ExtractNode(label="Extract Data",parent=editor.tag)))
        with dpg.menu(label="Run"):
            dpg.add_menu_item(tag='run_scraper',label="Scraper",callback=editor.run_graph)
    dpg.add_node_editor(tag=editor.tag,minimap=True,menubar=False, minimap_location=dpg.mvNodeMiniMap_Location_BottomRight, width=width-15, height=height-55, callback=link_callback);

# register key press handlers
with dpg.handler_registry():
    for hotkey in editor.hotkeys:
        dpg.add_key_press_handler(hotkey.key, callback=hotkey.callback);

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()