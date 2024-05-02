import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import rembg

class Spritemaker():
    def __init__(self, image_path):
        self.image = self.read_image(image_path)
        self.image = self.remove_background(self.image)
        self.rectangles = self.extract_rectangles(self.image)
        self.sprites = []
    
    def read_image(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
        return image

    def remove_background(self, image):
        output_pil = rembg.remove(Image.fromarray(image))
        return np.array(output_pil)

    def extract_rectangles(self, image):
        lower_alpha = np.array([0, 0, 0, 10])
        upper_alpha = np.array([255, 255, 255, 255])

        background_mask = cv2.inRange(image, lower_alpha, upper_alpha)
        contours, _ = cv2.findContours(background_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        rectangles = [cv2.boundingRect(contour) for contour in contours]
        
        # Sort the rectangles from left to right
        rectangles = sorted(rectangles, key=lambda x: x[0])
        return rectangles

    def show_bounding_boxes(self, image, rectangles):
        for rect in rectangles:
            x, y, w, h = rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0, 255), 2)
        plt.imshow(image)
        plt.show()

    def image_from_rect(self, rect):
        x, y, w, h = rect
        return self.image[y:y+h, x:x+w]
    
    def extract_sprites(self):
        for rect in self.rectangles:
            self.sprites.append(self.image_from_rect(rect))
        
    def show(self):
        self.show_bounding_boxes(self.image, self.rectangles)
    
    def show_sprite(self, index):
        # self.show_bounding_boxes(self.sprites[index], self.rectangles[index])
        plt.imshow(self.sprites[index])
        plt.show()
        
if __name__ == "__main__":
    spritemaker = Spritemaker('FSS.png')
    # spritemaker.show()
    spritemaker.extract_sprites()
    # spritemaker.show_sprite(0)
    # spritemaker.show_sprite(1)
    # spritemaker.show_sprite(2)
    # spritemaker.show_sprite(3)
    