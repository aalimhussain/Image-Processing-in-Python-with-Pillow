from PIL import Image

#Image Object
image = Image.open('image.jpg')
image.show()
# The format is of the input file i.e JPEG
print(image.format)
# The pixel format used by the image.
print(image.mode)
# Image size, in pixels.
print(image.size)
# Colour palette table, if any.
print(image.palette)

#Changing Image Type
image = Image.open('image.jpg')
image.save('new_image.png')

#Resizing Images
image = Image.open('image.jpg')
new_image = image.resize((32, 32))
new_image.save('image_32.jpg')
print(image.size)
print(new_image.size)

image = Image.open('image.jpg')
image.thumbnail((32, 32))
image.save('image_thumbnail.jpg')
print(image.size)
image.show()

#Cropping
image = Image.open('image.jpg')
box = (20, 50, 200, 200)
cropped_image = image.crop(box)
cropped_image.save('cropped_image.jpg')


#Pasting an Image onto Another Image
image = Image.open('image.jpg')
logo = Image.open('logo.png')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('pasted_image.jpg')
image_copy.show()


#Rotating Images
image = Image.open('image.jpg')
image_rot_90 = image.rotate(90)
image_rot_90.save('image_rot_90.jpg')
image_rot_180 = image.rotate(180)
image_rot_180.save('image_rot_180.jpg')

image.rotate(18).save('image_rot_18.jpg')

image.rotate(18, expand=True).save('image_rot_18.jpg')

#Flipping Images
image = Image.open('image.jpg')
image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
image_flip.save('image_flip.jpg')

#Drawing on Images
from PIL import Image, ImageDraw

blank_image = Image.new('RGB', (400, 300), 'white')
img_draw = ImageDraw.Draw(blank_image)
img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
img_draw.text((70, 250), 'Hello Python!', fill='green')
blank_image.save('drawn_image.jpg')

#Color Transforms
image = Image.open('image.jpg')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')
greyscale_image.show()