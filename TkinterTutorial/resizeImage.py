from PIL import ImageTk, Image

image = Image.open('TkinterTutorial\\Images\\photo6.jpg')
new_image = image.resize((500, 500))
new_image.save('photo6_500.jpg')