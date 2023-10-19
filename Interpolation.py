# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:55:56 2023

@author: marqjace
"""

# Imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import seaborn as sns



# Create Dataframe   
df3 = pd.read_csv('C:/Users/marqjace/slocum_python/DATA - WA Coast Sep 23/osu551-20230907T1717_c3f6_30c0_d795.csv', index_col=False, skiprows=[1])   ### if .xlsx sheet_name = sheet needs to be in ())

# Drop all values below 6m depth
df3 = df3.drop(df3[(df3['depth'] > 6)].index)

# Define Variables
latitude = df3['latitude'].values
longitude = df3['longitude'].values
depth = df3['depth'].values
temperature = df3['temperature'].values
salinity = df3['salinity'].values
do = df3['dissolved_oxygen'].values

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

# Nearest Neighbor Interpolated PColorMesh Plot (Longitude vs Latitude; Surface measurements only)


# number of grid points:
xn, yn = 100, 20

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 46.82, 47.19

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))



# Interpolate using "nearest" method
Z = griddata(points = (longitude, latitude),
              values = temperature,
              xi = (X, Y),
              method = 'nearest')


# Plot the results
plt.figure(figsize=(12,8), dpi=300)
plt.pcolormesh(X, Y, Z, cmap=plt.cm.jet)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel(r'Latitude ($\degree$N)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.clim(10,17)
plt.title('"Nearest" Interpolated PColorMesh Surface Plot')
plt.text(-124.3, 47.17, '~5m Depth')

#%%

# Linearly Interpolated PColorMesh Plot (Longitude vs Latitude; Surface measurements only)


# number of grid points:
xn, yn = 100, 20

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 46.82, 47.19

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))



# Interpolate using "linear" method
Z = griddata(points = (longitude, latitude),
              values = temperature,
              xi = (X, Y),
              method = 'linear')


# Plot the results
plt.figure(figsize=(12,8), dpi=300)
plt.pcolormesh(X, Y, Z, cmap=plt.cm.jet)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel(r'Latitude ($\degree$N)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.clim(10,17)
plt.title('Linearly Interpolated PColorMesh Surface Plot')
plt.text(-124.3, 47.17, '~5m Depth')

#%%

# Cubic Interpolated PColorMesh Plot (Longitude vs Latitude; Surface measurements only)


# number of grid points:
xn, yn = 20, 20

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 46.82, 47.19

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))



# Interpolate using "nearest" method
Z = griddata(points = (longitude, latitude),
              values = temperature,
              xi = (X, Y),
              method = 'cubic')


# Plot the results
plt.figure(figsize=(12,8), dpi=300)
plt.pcolormesh(X, Y, Z, cmap=plt.cm.jet)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel(r'Latitude ($\degree$N)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.clim(10,17)
plt.title('Cubic Interpolated PColorMesh Surface Plot')
plt.text(-124.3, 47.17, '~5m Depth')

#%%

# Linearly Interpolated Contour Plot (Longitude vs Latitude; Surface measurements only)


# grid sizing

# number of grid points:
xn, yn = 100, 20

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 46.82, 47.19

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude, latitude),
             values = temperature,
             xi = (X, Y),
             method = 'linear')

# Plot the results
plt.figure(figsize=(12,8), dpi=300)
contours = plt.contour(X, Y, Z, s=1, colors='white')
plt.clabel(contours, inline=True, fontsize=15)
grid = plt.contourf(X, Y, Z, cmap='jet')
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel(r'Latitude ($\degree$N)')
plt.colorbar(grid, label=r'Temperature ($\degree$C)')
# plt.clim(10,17)
plt.title('Interpolated Contour Surface Plot')
plt.text(-124.3, 47.17, '~5m Depth')


#%%

# Calculating delta-X in longitude

deltaX = np.diff(longitude, axis=0)
deltaDepth = np.diff(depth, axis=0)


theta = np.polyfit(deltaDepth, deltaX,1)
y_line = theta[1] + theta[0] * deltaX
        

fig, ax = plt.subplots(figsize=(12,8), dpi=300)

deltaplot = ax.scatter(deltaDepth, deltaX)
hor_line = plt.axhline(y = 0, color = 'k', linestyle = '-')
vert_line = plt.axvline(x = 0, color = 'k', linestyle = '-')
best_fit = plt.plot(deltaDepth, y_line, 'r-')
ax.set_xlabel(r'$\Delta$ Z (m)')
ax.set_ylabel(r'$\Delta$ X ($\degree$Longitude)')
ax.set_title('Distribution Between the Difference in Depth of Dive and Distance Between Surfacing')
sns.set_theme(context='notebook', style='whitegrid')


#%%

# Calculating delta-Y in latitude

deltaY = np.diff(latitude, axis=0)
deltaDepth = np.diff(depth, axis=0)


theta = np.polyfit(deltaDepth, deltaY,1)
y_line = theta[1] + theta[0] * deltaY
        

fig, ax = plt.subplots(figsize=(12,8), dpi=300)

deltaplot = ax.scatter(deltaDepth, deltaY)
hor_line = plt.axhline(y = 0, color = 'k', linestyle = '-')
vert_line = plt.axvline(x = 0, color = 'k', linestyle = '-')
best_fit = plt.plot(deltaDepth, y_line, 'r-')
ax.set_xlabel(r'$\Delta$ Z (m)')
ax.set_ylabel(r'$\Delta$ Y ($\degree$Latitude)')
ax.set_title('Distribution Between the Difference in Depth of Dive and Distance Between Surfacing')
sns.set_theme(context = 'notebook', style = 'whitegrid')


