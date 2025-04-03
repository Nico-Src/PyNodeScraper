import dearpygui.dearpygui as dpg;
from src.attribute import NodeAttribute;
import src.globals as globals;

class Node():
    tag_counter = 0;

    def __init__(self, label, parent, width=200):
        self.label = label;
        self.attributes = {};
        self.data = {};
        self.links = {};
        self.parent = parent;
        self.width = width;
        self.tag = f'node_{Node.tag_counter}';
        self.popup_tag = f'{self.tag}_popup';
        Node.tag_counter = Node.tag_counter + 1;
        pass

    # remove node (and hide popup)
    def remove(self):
        dpg.delete_item(self.tag);
        dpg.configure_item(self.popup_tag, show=False);
    
    # add node to ui context
    def use(self):
        with dpg.node(label=self.label,parent=self.parent,tag=self.tag):
            for attrib in self.attributes.values():
                attrib.use();
                for child in attrib.children:
                    child.use();
            with dpg.popup(self.tag,tag=self.popup_tag, mousebutton=dpg.mvMouseButton_Right, no_move=True):
                dpg.add_button(tag=f"{self.popup_tag}_delete", label="Delete",width=200,callback=self.remove);

    # add attribute to node
    def add_attribute(self,name,attribute):
        self.attributes[name] = attribute;


class ScrapeNode(Node):
    def __init__(self, label, parent):
        super().__init__(label, parent, 400);
        self.screen_counter = 0;
        urlAttrib = NodeAttribute("URL",self.tag,dpg.mvNode_Attr_Static);
        self.add_attribute("url",urlAttrib);
        urlAttrib.add_text_input("URL", self.width);
        dataAttrib = NodeAttribute("HTML",self.tag,dpg.mvNode_Attr_Output);
        self.add_attribute("html",dataAttrib);
        dataAttrib.add_text("HTML Data");
        imageAttrib = NodeAttribute("Image",self.tag,dpg.mvNode_Attr_Static);
        self.add_attribute("screen",imageAttrib);
        imageAttrib.add_spacer(20);
        imageAttrib.add_image("none",self.width);

    # remove screen image
    def removeScreen(self):
        self.attributes["screen"].remove();

    # add screen image back in
    def addScreen(self):
        resourceManager = globals.getResourceManager();
        resourceManager.loadImage(f"screen_{self.screen_counter}", f'img/screen.jpg');
        imageAttrib = NodeAttribute("Image",self.tag,dpg.mvNode_Attr_Static);
        self.add_attribute("screen",imageAttrib);
        imageAttrib.add_spacer(20);
        imageAttrib.add_image(f"screen_{self.screen_counter}",self.width);
        imageAttrib.use();
        for child in imageAttrib.children:
            child.use();
        self.screen_counter = self.screen_counter + 1;

class ExtractNode(Node):
    def __init__(self, label, parent):
        super().__init__(label, parent);
        dataAttrib = NodeAttribute("Data",self.tag,dpg.mvNode_Attr_Input);
        self.add_attribute("data",dataAttrib);
        dataAttrib.add_text("Data");