from PIL import Image
import os

image1 = Image.open('static/samuel-scrimshaw-KeUKM5N-e_g-unsplash.jpg')

# change image extantion
# image1.save('img/aa.png')

size = (480,640)
new = image1.resize(size)
path = 'static/13.jpg'
new.save(path)
print(new.size)