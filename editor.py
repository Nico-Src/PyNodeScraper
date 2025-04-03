import dearpygui.dearpygui as dpg;

class Editor():
    def __init__(self):
        self.tag = "node_editor";
        self.nodes = {};
        self.links = {};
        self.hotkeys = [
            Hotkey(dpg.mvKey_Delete, self.remove_node_key)
        ];
        pass;

    def add_node(self, node):
        # create node with attributes and inputs / other stuff
        self.nodes[node.tag] = node;
        node.use();

    # key handler for the delete key
    def remove_node_key(self):
        # delete all selected nodes
        for node in dpg.get_selected_nodes(self.tag):
            dpg.delete_item(node);
        # delete all selected links
        for link in dpg.get_selected_links(self.tag):
            self.remove_link(link);
            dpg.delete_item(link);

    # remove specific node
    def remove_node(self, sender):
        # cut away the _popup_delete part (13 characters)
        node_tag = sender[:-13];
        popup_tag = sender[:-7];
        dpg.delete_item(node_tag);
        dpg.configure_item(popup_tag, show=False);

    # add link to link dictionary (with attribute tags as references)
    def add_link(self, link_tag, attrib_one, attrib_two):
        self.links[link_tag] = {"from":attrib_one,"to":attrib_two}
        
        # add link to node
        nodeRefOne = self.nodes[self.getNodeTagFromAttribute(attrib_one)];
        nodeRefOne.links[attrib_one] = attrib_two;

    # remove link from link dictionary
    def remove_link(self, link_tag):
        link = self.links[link_tag];
        nodeRef = self.nodes[self.getNodeTagFromAttribute(link['from'])];
        del nodeRef.links[link['from']];
        print(len(nodeRef.links));
        del self.links[link_tag];

    # get node tag from attribute tag
    def getNodeTagFromAttribute(self, attrib_tag):
        return attrib_tag.split(';')[0]

class Hotkey():
    def __init__(self, key:int, callback):
        self.key = key;
        self.callback = callback;
        pass;