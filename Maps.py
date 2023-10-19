# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:15:15 2023

@author: marqjace
"""

# Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


# Create Dataframe            
df = pd.read_csv('C:/Users/marqjace/slocum_python/DATA - WA Coast Sep 23/osu551-20230907T1717_c3f6_30c0_d795.csv', index_col=False, skiprows=[1])   ### if .xlsx sheet_name = sheet needs to be in ())

# Drop all values except 5m depth
# df = df.drop(df[(df['depth'] > 6)].index)

# Define Variables
latitude = df['latitude']
longitude = df['longitude']
depth = df['depth']
temperature = df['temperature']
salinity = df['salinity']
do = df['dissolved_oxygen']

#%%

# Successful Raw Scatter Plot (Longitude vs Latitude; Less than 6 m)

fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

# cmap
orig_cmap = plt.get_cmap("viridis")  # You can choose a different colormap -- rocket, mako, magma, viridis
# shrunk_cmap = shiftedColorMap(orig_cmap, start=0.0, midpoint=0.15, stop=1, name='shrunk')


# Interpolated Plot

scat = ax.scatter(longitude, latitude, s=50)

# Interpolation Try
# scat = ax.scatter(lon_new, z_new, c=temp_new, cmap=orig_cmap, s=1)

ax.set_ylabel(r'Latitude ($\degree$N)')
ax.set_xlabel(r'Longitude ($\degree$E)')
ax.set_title('Map of Glider Path')

#%%

# from numpy.lib.arraypad import pad
latN = latitude.max()
latS = latitude.min()
lonW = longitude.min()
lonE = longitude.max()
cLat = (latN + latS) / 2
cLon = (lonW + lonE) / 2

projPS = ccrs.PlateCarree(central_longitude=180)

fig = plt.figure(figsize=(10, 5), dpi=300)
ax = plt.subplot(1, 1, 1, projection=projPS)

# ax.set_extent([-125, -124, 40, 41], ccrs.PlateCarree())
ax.set_extent([lonW-1, lonE+1, latS-1, latN+1], ccrs.PlateCarree())
ax.set_facecolor(cartopy.feature.COLORS['water'])
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='--')
ax.add_feature(cartopy.feature.STATES)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.RIVERS)
ax.add_feature(cartopy.feature.LAKES)
ax.coastlines(resolution='10m')
ax.gridlines(draw_labels=True, color='black', alpha=.5, crs=projPS)

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Map of SL551 WA Coast Sep 2023', pad=12.0);

travel_plot = ax.scatter(longitude, latitude, s=1, c='red', transform=ccrs.PlateCarree())

