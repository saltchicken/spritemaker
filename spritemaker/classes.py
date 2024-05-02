import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image
import rembg

class Spritemaker():
    def __init__(self, image_path):
        self.image = self.read_image(image_path)
        self.image = self.remove_background(self.image)
        self.rectangles = self.extract_rectangles(self.image)
        self.sprites = []
        self.extract_sprites()
    
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
        
    def animate_sprites(self):
        fig, ax = plt.subplots()
        plt.axis('off')
        blank = np.zeros(self.sprites[0].shape)[:, :, :3]
        im = plt.imshow(blank, cmap='gray')
        
        def update(frame):
            frame_image = self.sprites[frame]
            frame_image = frame_image[:, :, :3]
            im.set_array(frame_image)
            return im,
        
        ani = FuncAnimation(fig, update, frames=range(len(self.sprites)), interval=200, blit=True)
        
        plt.show()

    def create_sprite_sheet(self):
        image = Image.new("RGBA", (512, 128))
        for i in range(4):
            sprite = Image.fromarray(self.sprites[i])
            scale = sprite.width / 64
            sprite = sprite.resize((int(sprite.width / scale), int(sprite.height / scale)))
            x_padding = (128 - sprite.width) // 2
            y_padding = (128 - sprite.height) // 2
            Image.Image.paste(image, sprite, (i * 128 + x_padding, y_padding))
        return image
        
if __name__ == "__main__":
    spritemaker = Spritemaker('FSS.png')
    spritemaker.animate_sprites()
    # image = spritemaker.create_sprite_sheet()
    # image.save('saved.png')
    # plt.imshow(image)
    # plt.show()
    # spritemaker.show()
    
    # spritemaker.show_sprite(0)
    # spritemaker.show_sprite(1)
    # spritemaker.show_sprite(2)
    # spritemaker.show_sprite(3)
    