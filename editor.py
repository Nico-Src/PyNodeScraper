import dearpygui.dearpygui as dpg;

class Editor():
    def __init__(self):
        self.tag = "node_editor";
        self.nodes = [];
        self.hotkeys = [
            Hotkey(dpg.mvKey_Delete, self.remove_node_key)
        ];
        pass;

    def add_node(self, node):
        # create node with attributes and inputs / other stuff
        self.nodes.append(node);
        self.debug_log(f'Added new Node: {node.tag}');
        node.use();

    def remove_node_key(self):
        # delete all selected nodes
        for node in dpg.get_selected_nodes(self.tag):
            dpg.delete_item(node);
        for link in dpg.get_selected_links(self.tag):
            dpg.delete_item(link);

    def remove_node(self, sender):
        # cut away the _popup_delete part (13 characters)
        node_tag = sender[:-13];
        popup_tag = sender[:-7];
        dpg.delete_item(node_tag);
        dpg.configure_item(popup_tag, show=False);

class Hotkey():
    def __init__(self, key:int, callback):
        self.key = key;
        self.callback = callback;
        pass;