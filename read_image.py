import pds4_tools
from PIL import Image

# Read the file
struct_list = pds4_tools.read('local-path-to-extracted-file/data/calibrated/20220129/ch2_ohr_ncp_20220129T0150171705_d_img_d18.xml')
# Extract the image from the file
im = struct_list[0].data
# Slice part of the image array
image_slice = im[100000:, 11000:]
# Display the array
img = Image.fromarray(image_slice)
img.save('sample.png')
img.show()



