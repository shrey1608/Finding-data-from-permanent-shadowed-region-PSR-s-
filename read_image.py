import pds4_tools
from PIL import Image

# Read the file
struct_list = pds4_tools.read('local-path-to-extracted-file/data/calibrated/folder-number/xml-file')
# Extract the image from the file
im = struct_list[0].data
# Slice part of the image array
image_slice = im[100000:, 11000:]
# Display the array
img = Image.fromarray(image_slice)
img.save('sample.png')
img.show()



