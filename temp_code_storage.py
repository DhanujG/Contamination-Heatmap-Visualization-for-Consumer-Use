#!/usr/bin/env python

#/mnt/c/Users/dhanu/Documents/EcoData
#source env/bin/activate


import pandas as pd
import numpy as np


data_1 = pd.read_csv("/mnt/c/Users/dhanu/Documents/EcoData/data/UMCR4_All_MichiganOnlyData.csv")

data_2 = pd.read_csv("/mnt/c/Users/dhanu/Documents/EcoData/data/UCMR3_MichiganDataOnly.csv")

data_1['Report'] = 'UCMR3'
data_2['Report'] = 'ToBeDetr'

connect_bois = [data_1, data_2]

data_3 = pd.concat(connect_bois)

counts = data_3.groupby(['Report']).count()

data_3.to_csv('UCMR3Test.csv')
counts.to_csv('UCMR3TestCounts.csv')



# Read in ZIP code boundaries for California
d = read_ascii_boundary('/mnt/c/Users/dhanu/Documents/EcoData/input/zt26_d00')

# Read in data for number of births by ZIP code in California
#f = csv.reader(open('/mnt/c/Users/dhanu/Documents/EcoData/CA_2007_births_by_ZIP.txt', 'rt'))
f = csv.reader(open('/mnt/c/Users/dhanu/Documents/EcoData/output/chem_files/4-androstene-3,17-dione_2014_Michigan_UCMR3.txt', 'rt'))
vals = {}
# Skip header line
next(f)
# Add data for each ZIP code
for row in f:
    #zipcode, resultvalue = row
    number, date, zipcode, resultvalue = row
    vals[zipcode] = float(resultvalue)
max_vals = max(vals.values())

# Create figure and two axes: one to hold the map and one to hold
# the colorbar
figure(figsize=(20, 20), dpi=100)
#map_axis = axes([0.0, 0.0, 8, 9])
#cb_axis = axes([8.3, 1, 0.3, 6])

#figure(figsize=(5, 5), dpi=30)
map_axis = axes([0.0, 0.0, 0.9, 0.9])
cb_axis = axes([0.83, 0.1, 0.03, 0.6])

# Define colormap to color the ZIP codes.
# You can try changing this to cm.Blues or any other colormap
# to get a different effect
cmap = cm.PuRd

# Create the map axis
axes(map_axis)
axis([-90, -80, 40, 50])
gca().set_axis_off()

# Loop over the ZIP codes in the boundary file

for polygon_id in d:
    polygon_data = array(d[polygon_id]['polygon'])
    zipcode = d[polygon_id]['name']
    num_vals = vals[zipcode] if zipcode in vals else 0.
    # Define the color for the ZIP code
    fc = cmap(num_vals / max_vals)
    # Draw the ZIP code
    patch = Polygon(array(polygon_data), facecolor=fc,
        edgecolor=(.3, .3, .3, 1), linewidth=.2)
    gca().add_patch(patch)
title('Above minimum reporting levels in Michigan for 1,1-dichloroethane(2013)', fontsize=30)

# Draw colorbar
cb = mpl.colorbar.ColorbarBase(cb_axis, cmap=cmap,
    norm = mpl.colors.Normalize(vmin=0, vmax=max_vals))
cb.set_label('Critical Value Level', fontsize=40)

# Change all fonts to Arial
for o in gcf().findobj(matplotlib.text.Text):
    o.set_fontname('DeJavu Sans')


for file in os.listdir("/mnt/c/Users/dhanu/Documents/EcoData/output/chem_files/"):
     print(file)
     chunks = file.split("_")
     print (chunks[0])
     print (chunks[1])


# Export figure to bitmap
savefig('/mnt/c/Users/dhanu/Documents/EcoData/output/maps/4-androstene-3,17-dione_2014_map.png')

