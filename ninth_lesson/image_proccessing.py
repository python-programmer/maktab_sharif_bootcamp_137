from PIL import Image
import numpy

image = Image.open("simpson.jpg")

image_array = numpy.array(image)

counter = 1
is_ended = False

for row in image_array:
    for col in row:
        counter += 1
        print(col)

        if counter > 100:
            is_ended
            break
    if is_ended:
         break


image_gray = image.convert("L")
image_gray.save("simpson-gray.jpg")