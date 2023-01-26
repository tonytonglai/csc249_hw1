# the package i'm using for imports...
from PIL import Image
import matplotlib.pyplot as plt

# file i/o
light_image = Image.open("cup_light.jpg")
dark_image = Image.open("cup_dark.jpg")

# storing in a list, for ease of use!
images = [light_image, dark_image]
names = ["light_bw.jpeg", "dark_bw.jpeg"]
# iterating through the images...
for image in images:
    print(image.format, image.size, image.mode)

# to programatically save the images as greyscale...
# for i in range(len(images)):
#     tmp_img_greyscale = images[i].convert("L")
#     tmp_img_greyscale.save(names[i],'jpeg',icc_profile=tmp_img_greyscale.info.get('icc_profile'))

# converts the images to greyscale manually...
light_image_bw = images[0].convert("L")
dark_image_bw = images[1].convert("L")

# getting the dimensions to easily adjust resizing
image_size = light_image_bw.size # this is a tuple
IMWIDTH = image_size[0]
IMHEIGHT = image_size[1]

left = int(IMWIDTH * 0.33)
up = int(IMHEIGHT * 0.53)
right = int(IMWIDTH * 0.55)
down = int(IMHEIGHT* 0.71)
size_tuple = (left, up, right, down) # referencing the documentation
light_image_bw_zoom = light_image_bw.crop(size_tuple)
dark_image_bw_zoom = dark_image_bw.crop(size_tuple)
print(light_image_bw_zoom.size)

# plt.plot(light_image_bw_zoom.histogram())
# plt.title("Bright Greyscale Histogram")
# plt.show()
#
# plt.plot(dark_image_bw_zoom.histogram())
# plt.title("Low Light Greyscale Histogram")
# plt.show()
# saving the images manually...
# light_image_bw_zoom.save("light_bw_zoom.jpeg",'jpeg',icc_profile=light_image_bw_zoom.info.get('icc_profile'))
# dark_image_bw_zoom.save("dark_bw_zoom.jpeg", 'jpeg',icc_profile=dark_image_bw_zoom.info.get('icc_profile'))

# light_image_bw_zoom.show()
# dark_image_bw_zoom.show()

light_histogram = light_image_bw_zoom.histogram()
max_val_light = max(light_histogram)
split_val_light = 0
for i in range(len(light_histogram)):
    if light_histogram[i] == max_val_light:
        split_val_light = i

dark_histogram = dark_image_bw_zoom.histogram()
max_val_dark = max(dark_histogram)
split_val_dark = 0
for i in range(len(dark_histogram)):
    if dark_histogram[i] == max_val_dark:
        split_val_dark = i

print(f'index of most pixels for light:{split_val_light}\nvalue:{max_val_light}')
print("")
print(f'index of most pixels for dark:{split_val_dark}\nvalue:{max_val_dark}')

fin_light = light_image_bw_zoom.point(lambda i: i > split_val_light and 255)
fin_dark = dark_image_bw_zoom.point(lambda i: i > split_val_dark and 255)

plt.plot(fin_light.histogram())
plt.title("Bright Contrast Histogram")
plt.show()

plt.plot(fin_dark.histogram())
plt.title("Low Lighting Contrast Histogram")
plt.show()

fin_light.save("contrast_light.jpeg",'jpeg',icc_profile=fin_light.info.get('icc_profile'))
fin_dark.save("contrast_dark.jpeg",'jpeg',icc_profile=fin_dark.info.get('icc_profile'))



# light_image.point(lambda i: print(i))

# r, g, b = light_image.split()
#
# new_light = light_image.convert("L")
#
# new_light.show()
# plt.plot(new_light.histogram())
# plt.title("B/W Default Histogram")
# plt.show()
#
# # print("Source: ", source)
# fin_img = new_light.point(lambda i: i > 120 and 255)
#
# plt.plot(fin_img.histogram())
# plt.title("High Contrast Histogram")
# plt.show()
#
# fin_img.show()
#
# print("getcolors: ", light_image.getcolors())
# print("getdata: ", light_image.getdata(0))
# print("getpixel: ", light_image.getpixel((0,0)))
#
# print("\nLINEBREAK\n")
# maxHeight = max(light_image.histogram())
#
# newList = [i/maxHeight for i in light_image.histogram()]

# let's do a check where we basically store the MAX of where there are
# the most pixels, then we use that as the split, and make binary
# off of that, as well as a binary of 0 or 1 on 120.

# to identify these peaks for each of these images, we can
# just iterate in a loop, using pointers, and keep a tempVar on what
# the max value is.