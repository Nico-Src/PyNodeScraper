import dearpygui.dearpygui as dpg;
from src.child import NodeChild, NodeChildType;

class NodeAttribute():
    tag_counter = 0;

    def __init__(self, label, parent, attrib_type):
        self.label = label;
        self.data = {};
        self.parent = parent;
        self.children = [];
        self.attrib_type = attrib_type;
        self.tag = f'{parent};node_attribute_{NodeAttribute.tag_counter}';
        NodeAttribute.tag_counter = NodeAttribute.tag_counter + 1;

    # add to ui context
    def use(self):
        with dpg.node_attribute(label=self.label,parent=self.parent,tag=self.tag,attribute_type=self.attrib_type): pass;

    # remove self
    def remove(self):
        for child in self.children:
            child.remove();
        dpg.delete_item(self.tag);
    
    def add_spacer(self, height):
        data = {"height":height};
        child = NodeChild(data, "", self.tag, NodeChildType.SPACE);
        self.children.append(child);

    # add text child
    def add_text(self, text, label=""):
        data = {"text": text};
        child = NodeChild(data, label, self.tag, NodeChildType.TEXT);
        self.children.append(child);
    
    # add text input child
    def add_text_input(self, label="", width=200):
        data = {"width":width};
        child = NodeChild(data, label, self.tag, NodeChildType.TEXT_INPUT);
        self.children.append(child);

    # add image to attribute
    def add_image(self, image, width=200, label=""):
        data = {"image":image,"width":width};
        child = NodeChild(data, label, self.tag, NodeChildType.IMAGE);
        self.children.append(child);