import os
from PIL import Image
import json

class Texturemaker():
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = self.read_image(self.image_path)
        
    def read_image(self, image_path):
        return Image.open(image_path)
    
    def resize(self):
        self.image = self.image.resize((64, 64))
        
    def save(self, output_name=None):
        if not output_name:
            output_name = os.path.splitext(os.path.basename(self.image_path))[0]
        folder_path = f'./{output_name}'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f'Folder {folder_path} created')
        else:
            print(f'Folder {folder_path} already exists. Overwriting')
        self.image.save(f'{os.path.join(folder_path, output_name)}.png')
        
        # JSON info creation
        texture_json = {
            "traversable": True 
        }
        texture_json_string = json.dumps(texture_json)
        with open(f'{os.path.join(folder_path, output_name)}.json', 'w') as json_file:
                json_file.write(texture_json_string)
        
if __name__ == "__main__":
    pass