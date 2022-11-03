import pds4_tools
import cv2
import math
import matplotlib.pyplot as plt
import Lat_Long_mapping

# Read the file
struct_list = pds4_tools.read('local-path-to-extracted-file/data/calibrated/folder-number/xml-file')

# Extract the image from the file
im = struct_list[0].data

# extract image shape
image_shape = im.shape

# start: pixel coordinates of top left corner and end: pixel coordinates of the bottom right corner
x_start = 100000
y_start = 10000
x_end = 101000
y_end = 11000

# round down the coordinates of the slicing indices to nearest 100
# Reason : csv file of latitude and longitude data consists of pixel coordinates in the scale of 100s
xslice_start_idx = 100 * math.floor((x_start)/100)
yslice_start_idx = 100 * math.floor((y_start)/100)
xslice_end_idx = 100 * math.floor((x_end)/100)
yslice_end_idx = 100 * math.floor((y_end)/100)

# Slice part of the image array
image_slice = im[xslice_start_idx : xslice_end_idx, yslice_start_idx : yslice_end_idx]

# Convert from BGR format to RGB format
image = cv2.cvtColor(image_slice, cv2.COLOR_BGR2RGB)

# Plots latitude and longitude and uses a mouse event to display them
Lat_Long_mapping.plot_lat_long(xslice_start_idx, yslice_start_idx, xslice_end_idx, yslice_end_idx)

# display the image
plt.imshow(image)
plt.show()