from PIL import Image

class imgprinter():
    def printimg(path, width, height):
        
        original_image = Image.open(path)
        resized_image = original_image.resize((width, height))

        for y in range(height):
            for x in range(width):
                color = resized_image.getpixel((x, y))
                r, g, b = color[:3]
    
                print("\033[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m", end=" ")
            print("\033[0m")