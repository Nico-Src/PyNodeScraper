import dearpygui.dearpygui as dpg;

class ResourceManager():
    def __init__(self):
        self.images = {};
        self.textures = {};

    # load image and add to dictionary
    def load_image(self, name, path):
        image = dpg.load_image(path);
        if image is not None:
            self.images[name] = ResourceImage(image[0], image[1], image[2], image[3]);
    
    # add texture to dictionary
    def add_texture(self, image, texture):
        self.textures[image] = texture;

    # get image from dictionary
    def get_image(self, name):
        if name in self.images:
            return self.images[name];
        else:
            return None;

class ResourceImage():
    def __init__(self, width, height, channels, data):
        self.width = width;
        self.height = height;
        self.channels = channels;
        self.data = data;

    # return scaled dimensions for self with given width
    def scale_for_width(self, width):
        ratio = self.width / self.height;
        return {"width":width, "height":width / ratio};

    # return scaled dimensions for self with given heights
    def scale_for_height(self,height):
        ratio = self.width / self.height;
        return {"width":height*ratio,"height":height};