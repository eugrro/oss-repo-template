from PIL import Image, ImageOps

# creating an og_image object
og_image = Image.open("./3.jpg")

# applying grayscale method
gray_image = ImageOps.grayscale(og_image)
resized_img = gray_image.resize((28, 28))
invertedImage = ImageOps.invert(resized_img)
invertedImage.save('3a.png')
