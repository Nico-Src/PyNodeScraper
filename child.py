from enum import Enum
import dearpygui.dearpygui as dpg;

class NodeChild():
    tag_counter = 0;

    def __init__(self, data, label, parent, type):
        self.label = label;
        self.data = data;
        self.parent = parent;
        self.type = type;
        self.tag = f'{parent};node_child_{NodeChild.tag_counter}';
        NodeChild.tag_counter = NodeChild.tag_counter + 1;
    
    # add to ui context
    def use(self):
        # based on child type add child (text, text_input, ...)
        match self.type:
            case NodeChildType.TEXT:
                dpg.add_text(self.data['text'],label=self.label,tag=self.tag,parent=self.parent);
            case NodeChildType.TEXT_INPUT:
                dpg.add_input_text(label=self.label,tag=self.tag,parent=self.parent,width=self.data['width']);

    def remove(self):
        dpg.delete_item(self.tag);

class NodeChildType(Enum):
    TEXT=0,
    TEXT_INPUT=1