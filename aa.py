from PIL import Image

image = Image.open('static/images/7bb6dd1d43c3c2b3.jpg')
output = (200,350)
img = image.resize(output)
img.save('aaa.jpg', quality=100)

# image_file = Image.open('aaa.jpg')
#
# # the default
# image_file.save("image_name.jpg", quality=100)
#
# # Changing the image resolution using quality parameter
# # Example-1
# image_file.save("image_name2.jpg", quality=25)
#
# # Example-2
# image_file.save("image_name3.jpg", quality=1)













# lis = [1,2,3,4,5,8,2,3,9,6]
# lis1=[]
# while True:
#     for l in lis[0:3]:
#         lis1.append(l)
#         lis.remove(l)
#         print(l)
#     user = input('Enter y to continue: ')
#     if user == 'y':
#         continue
#     else:
#         break


# aa = 'My name is harish'
# aaa = ''
# revs = ''
# for a in aa:
#     if a != " ":
#         aaa += a
#     # else:
#     #     revs += aaa[::-1]
# print(aaa)