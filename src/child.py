from enum import Enum
import src.globals as globals;
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
        resourceManager = globals.getResourceManager();
        # based on child type add child (text, text_input, ...)
        match self.type:
            case NodeChildType.SPACE:
                dpg.add_spacer(height=self.data['height'],parent=self.parent);
            case NodeChildType.TEXT:
                dpg.add_text(self.data['text'],label=self.label,tag=self.tag,parent=self.parent);
            case NodeChildType.TEXT_INPUT:
                dpg.add_input_text(label=self.label,tag=self.tag,parent=self.parent,width=self.data['width']);
            case NodeChildType.IMAGE:
                image_tag = self.data['image'];
                image = resourceManager.getImage(image_tag);
                with dpg.texture_registry() as reg_id:
                    tex_id = dpg.add_static_texture(width=image.width,height=image.height,default_value=image.data,tag=f"{image_tag}_tex",parent=reg_id);
                    resourceManager.addTexture(image_tag, tex_id);
                scaled = image.scaleForWidth(self.data['width']);
                dpg.add_image(tex_id,parent=self.parent,width=scaled['width'],height=scaled['height'],tag=f'{image_tag}_img');

    # remove child
    def remove(self):
        dpg.delete_item(self.tag);

class NodeChildType(Enum):
    SPACE=-1,
    TEXT=0,
    TEXT_INPUT=1
    IMAGE=2