import dearpygui.dearpygui as dpg;
from src.node import ScrapeNode;
import src.globals as globals;
from src.attribute import NodeAttribute;

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
        node_ref_one = self.nodes[self.get_node_tag_from_attribute(attrib_one)];
        node_ref_one.links[attrib_one] = attrib_two;

    # remove link from link dictionary
    def remove_link(self, link_tag):
        link = self.links[link_tag];
        node_ref = self.nodes[self.get_node_tag_from_attribute(link['from'])];
        del node_ref.links[link['from']];
        del self.links[link_tag];

    # get node tag from attribute tag
    def get_node_tag_from_attribute(self, attrib_tag):
        return attrib_tag.split(';')[0];

    # run node graph (from scrapeNode onwards)
    def run_graph(self):
        # there can always only be one scrape node
        scrape_nodes = [node for node in self.nodes.values() if isinstance(node, ScrapeNode)];
        num_scrape_nodes = len(scrape_nodes);
        if num_scrape_nodes == 0 or num_scrape_nodes > 1: return None;
        scrape_node = scrape_nodes[0];
        url = dpg.get_value(scrape_node.attributes["url"].children[0].tag);
        scraper = globals.get_scraper();
        scraper.scrape_url(url, self.scrape_callback);
        pass

    # callback from scraper
    def scrape_callback(self, data):
        scrape_node = [node for node in self.nodes.values() if isinstance(node, ScrapeNode)][0];
        scrape_node.removeScreen();
        scrape_node.addScreen();

class Hotkey():
    def __init__(self, key:int, callback):
        self.key = key;
        self.callback = callback;
        pass;