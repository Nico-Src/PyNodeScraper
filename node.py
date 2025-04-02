import dearpygui.dearpygui as dpg;
from editor import Editor;
from attribute import NodeAttribute;

class Node():
    tag_counter = 0;

    def __init__(self, label, parent, width=200):
        self.label = label;
        self.attributes = [];
        self.data = {};
        self.parent = parent;
        self.width = width;
        self.tag = f'node_{Node.tag_counter}';
        self.popup_tag = f'{self.tag}_popup';
        Node.tag_counter = Node.tag_counter + 1;
        pass

    def remove(self):
        dpg.delete_item(self.tag);
        dpg.configure_item(self.popup_tag, show=False);
    
    def use(self):
        with dpg.node(label=self.label,parent=self.parent,tag=self.tag):
            for attrib in self.attributes:
                attrib.use();
                for child in attrib.children:
                    child.use();
            with dpg.popup(self.tag,tag=self.popup_tag, mousebutton=dpg.mvMouseButton_Right, no_move=True):
                dpg.add_button(tag=f"{self.popup_tag}_delete", label="Delete",width=self.width,callback=self.remove);

    def add_attribute(self,attribute):
        self.attributes.append(attribute);
        Editor.debug_log(f'Added new Attribute: {attribute.tag} (Parent: {self.tag})')


class ScrapeNode(Node):
    def __init__(self, label, parent):
        super().__init__(label, parent);
        urlAttrib = NodeAttribute("URL",self.tag,dpg.mvNode_Attr_Static);
        self.add_attribute(urlAttrib);
        urlAttrib.add_text_input("URL", self.width);
        dataAttrib = NodeAttribute("HTML",self.tag,dpg.mvNode_Attr_Output);
        self.add_attribute(dataAttrib);
        dataAttrib.add_text("HTML");

class ExtractNode(Node):
    def __init__(self, label, parent):
        super().__init__(label, parent);
        dataAttrib = NodeAttribute("Data",self.tag,dpg.mvNode_Attr_Input);
        self.add_attribute(dataAttrib);
        dataAttrib.add_text("Data");