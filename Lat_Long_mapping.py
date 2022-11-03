import csv
import math
import matplotlib.pyplot as plt

def plot_lat_long(xslice_start_idx, yslice_start_idx, xslice_end_idx, yslice_end_idx):
  # Read csv file at /geometry/calibrated/...
  # Opening the CSV file
  with open('local-path-to-extracted-file/geometry/calibrated/folder-number/csv-file', mode ='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # lat_long_data maps the pixel coordinates with the latitude longitude data
    lat_long_data = {}
    i = 0
    for lines in csvFile:
      # first line of csv file contains headings
      # Use i to skip processing the heading
      if i == 0:
        i += 1
        continue
      pixel_coordinates = tuple([float(lines[3]), float(lines[2])])
      lat_long_data[pixel_coordinates] = [float(lines[1]), float(lines[0])]


  fig, ax = plt.subplots()

  # Scale the axis to 1000 units
  plt.xlim([0, 1000])
  plt.ylim([0, 1000])

  # Keep the origin of the image at top
  ax.xaxis.tick_top()
  ax.invert_yaxis()

  # Add x coordinates
  xtick_data = [lat_long_data[xslice_start_idx, yslice_start_idx][0], lat_long_data[xslice_end_idx, yslice_start_idx][0]]
  plt.xticks([0, 1000], xtick_data)

  # Add y coordinates
  ytick_data = [lat_long_data[xslice_start_idx, yslice_start_idx][1], lat_long_data[xslice_start_idx, yslice_end_idx][1]]
  plt.yticks([0, 1000], ytick_data)

# Mouse event to display the latitude and longitude coordinates
  def onmove(event):
      if event.xdata != None and event.ydata != None:
        # to display the pixel coordinates, shift origin from (0, 0) to (xslice_start_idx, yslice_start_idx)
        x_coor = 100 * math.floor((event.xdata + xslice_start_idx)/100)
        y_coor = 100 * math.floor((event.ydata + yslice_start_idx)/100)
        lat = lat_long_data[x_coor, y_coor][0]
        lon = lat_long_data[x_coor, y_coor][1]
        print( 'x=%d, y=%d, latitude=%f, longitude=%f'%(x_coor, y_coor, lat, lon))

  cid = fig.canvas.mpl_connect('motion_notify_event', onmove)