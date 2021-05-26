from PIL import Image

# Image.open() can also open other image types
img = Image.open("ab41977ab188f96f.jpg")
# WIDTH and HEIGHT are integers
resized_img = img.resize((400, 400))
resized_img.save("resized_image.jpg")