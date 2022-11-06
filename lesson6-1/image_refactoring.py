"""
Look at the image salvador-result.jpeg. You need to update the code from the lesson,
so your new file is simmilar to what is drawn in salvador-result.jpeg

Use dataclasses to represent coordinates of rectangle and text
Make the code as configurable as possible
Achieve the result. The final image must be in PNG format
"""

from curses.textpad import rectangle
import os

from PIL import Image, ImageDraw, ImageFont
from my_data_classes import Point, Rectangle


class ImageUpdater:
    
    def __init__(self, file_name = str) -> None:
        self.__source_file_name: str = file_name
        self.source_image: Image = None
        
    def __enter__(self) -> "ImageUpdater":
        self.source_image = Image.open(self.__source_file_name).convert("RGBA")
        return self
        
    def __exit__(self, type, value, tb) -> None:
        self.source_image.close()
        
    def draw_watermark(self, rect: Rectangle, text_to_draw: str, background_color: str = "black",
                  text_color: str = "white") -> None:
        font = ImageFont.truetype(os.path.join("assets", "fonts", "OpenSans-Bold.ttf"), size=16)        
        draw = ImageDraw.Draw(self.source_image)
        draw.rectangle(xy=rect.to_tuple(), fill=background_color)

        horPadding = rect.width // 10 # rectangle horizontal padding
        verPadding = rect.height // 3 # rectangle vertical padding
        x0 = rect.xy.x + horPadding
        y0 = rect.xy.y + verPadding
        position = Point(x0, y0) # position of rectangle inner text
        draw.text(position.to_tuple(), text_to_draw, fill=text_color, font=font)
        
    def save_changes(self, output_file_name: str) -> None:
        self.source_image.save(output_file_name, "PNG")        

if __name__ == "__main__":
    output_file_name = "salvador-student-result.png"
    input_file_name = os.path.join("assets", "images", "salvador.jpeg")
    text = "We are learning\nPython"
    width = 160 # rectangle width
    height = 125 # rectangle height
    horz_space = 60 # horizontal distance between top tow rectangles
    ver_space = horz_space // 2 # vertical distancle between top and lower rectangles
    left = 30 # distance from x-axis
    top = 10 # distance from y-axis

    # draw rectangles on the image
    with ImageUpdater(file_name=input_file_name) as some_file:
        # draw a black rectangle with white text
        xy = Point(left, top)
        rect1 = Rectangle(xy=xy, width=width, height=height)
        some_file.draw_watermark(rect=rect1, text_to_draw=text)

        # draw a yellow rectangle with black text
        xy = Point(left + width + horz_space, top)
        rect2 = Rectangle(xy=xy, width=width, height=height)
        some_file.draw_watermark(rect=rect2, text_to_draw=text, text_color="black", background_color="yellow")

        # draw a blue rectangle with white text
        xy = Point((rect2.to_tuple()[1][0] - left) // 2 - width // 2 + left, top + height + ver_space)
        rect3 = Rectangle(xy=xy, width=width, height=height)
        some_file.draw_watermark(rect=rect3, text_to_draw=text, text_color="white", background_color="blue")

        some_file.save_changes(output_file_name=output_file_name)
