# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:07:16 2023

@author: marqjace
"""

# Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from scipy.interpolate import griddata
from scipy.interpolate import interp2d



# Create Dataframe   
df3 = pd.read_csv('C:/Users/marqjace/slocum_python/DATA - WA Coast Sep 23/osu551-20230907T1717_c3f6_30c0_d795.csv', index_col=False, skiprows=[1])   ### if .xlsx sheet_name = sheet needs to be in ())

# Drop all values below 6m depth
df3 = df3.drop(df3[(df3['depth'] > 6)].index)

# Define Variables
latitude = df3['latitude']
longitude = df3['longitude']
depth = df3['depth']
temperature = df3['temperature']
salinity = df3['salinity']
do = df3['dissolved_oxygen']

#%%

# Raw Scatter Plot (Longitude vs Latitude; Surface measurements only)
fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

# Plot the results
scat = ax.scatter(longitude, latitude, c=temperature, cmap=plt.cm.jet, s=50)
ax.set_ylabel(r'Latitude ($\degree$N)')
ax.set_xlabel(r'Longitude ($\degree$E)')
ax.set_title('Raw Surface Scatter Plot')
fig.colorbar(scat, label=r'Temperature ($\degree$C)')


#%%

# number of grid points:
xn, yn = 20, 20

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 46.82, 47.19

# Generate a regular grid to interpolate the data.
xgrid = np.linspace(xmin, xmax, xn)
ygrid = np.linspace(ymin, ymax, yn)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)

f = interp2d(Xgrid, Ygrid, temperature, kind='linear', fill_value = -1)


# Set up figure
fig, ax = plt.subplots(figsize=(12,8), dpi=300)

ax.plot(f)

#%%

fig, ax = plt.subplots(figsize=(12, 8), dpi=300)


# Gaussian KDE Plot
data = np.vstack((longitude, latitude))
kde = gaussian_kde(data)

# number of grid points:
xn, yn = 100, 20

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 46.82, 47.19

# Generate a regular grid to interpolate the data.
xgrid = np.linspace(xmin, xmax, xn)
ygrid = np.linspace(ymin, ymax, yn)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)

# Interpolate using "linear" method
Z = griddata(points = (longitude, latitude),
              values = temperature,
              xi = (Xgrid, Ygrid),
              method = 'linear')

# KDE Evaluate
# Z = kde.evaluate((np.vstack([Xgrid.ravel(), Ygrid.ravel()])))
# Z = kde.evaluate((np.vstack([data.ravel(), Z2])))


# Plot the results
plt.imshow(Z.reshape(Xgrid.shape),
           interpolation='spline16',
           aspect = 'auto',
           origin = 'lower',
           cmap='jet',
           extent = (xmin, xmax, ymin, ymax))
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel(r'Latitude ($\degree$N)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.title('Linearly Interpolated IMShow Surface Plot')
plt.text(-124.3, 47.17, '~5m Depth')

#%%

# Raw Scatter Plot (Longitude vs Latitude; Surface measurements only)
fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

# Plot the results
scat = ax.plot(data)
xmin, xmax, ymin, ymax = ax.axis([xmin, xmax, ymin, ymax])
ax.set_ylabel(r'Latitude ($\degree$N)')
ax.set_xlabel(r'Longitude ($\degree$E)')
ax.set_title('Raw Surface Scatter Plot')
