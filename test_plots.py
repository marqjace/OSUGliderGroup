# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:27:19 2023

@author: marqjace
"""

# Imports

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.interpolate import griddata


# Create Dataframe            
df = pd.read_csv('C:/Users/marqjace/slocum_python/DATA - WA Coast Sep 23/osu551-20230907T1717_c3f6_30c0_d795.csv', index_col=False, skiprows=[1])   ### if .xlsx sheet_name = sheet needs to be in ())

# Define Variables
latitude = df['latitude']
longitude = df['longitude']
depth = df['depth']
temperature = df['temperature']
salinity = df['salinity']
do = df['dissolved_oxygen']


# Interpolation

# Set new depth
z_new = np.arange(0, 200, 1)

# Temperature Interpolation with Depth
f = scipy.interpolate.interp1d(depth, temperature, kind='linear', bounds_error=False)
temp_new = f(z_new)

# Longitude Interpolation with Depth
f = scipy.interpolate.interp1d(depth, longitude, kind='linear', bounds_error=False)
lon_new = f(z_new)



#%%

# Raw Scatter Plot (Longitude vs Depth)

fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

scat = ax.scatter(longitude, depth, c=temperature, cmap=plt.cm.jet, s=20)

ax.invert_yaxis()
ax.set_ylabel('Depth (m)')
ax.set_xlabel(r'Longitude ($\degree$E)')
ax.set_title('Raw Scatter Plot')
fig.colorbar(scat, label=r'Temperature ($\degree$C)')


#%%

# Linearly Interpolated PColorMesh Plot (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 100, 50

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 200, 0

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude, depth),
             values = temperature,
             xi = (X, Y),
             method = 'linear')

# Plot the results
plt.figure(figsize=(12,8), dpi=300)
plt.pcolormesh(X, Y, Z, cmap='jet')
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel('Depth (m)')
plt.colorbar(label=r'Temperature ($\degree$C)')
# plt.clim(8,18)
plt.title('Linearly Interpolated PColorMesh Plot')

#%%

# Successful Interpolated Contour Plot (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 100, 50

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 200, 0

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude, depth),
             values = temperature,
             xi = (X, Y),
             method = 'linear')

# Plot the results
plt.figure(figsize=(12,8), dpi=300)
contours = plt.contour(X, Y, Z, s=3, colors='white')
plt.clabel(contours, inline=True, fontsize=15)
plt.contourf(X, Y, Z, cmap=plt.cm.jet)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel('Depth (m)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.title('Interpolated Contour Plot')

#%%

# Successful Interpolated IMShow Plot (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 100, 50

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 0, 200

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude, depth),
             values = temperature,
             xi = (X, Y),
             method = 'linear')

# Plot the results
fig, ax = plt.subplots(figsize=(12,8), dpi=300)
im = ax.imshow(Z, cmap=plt.cm.jet)
ax.set_xlabel(r'Longitude ($\degree$E)')
ax.set_ylabel('Depth (m)')
fig.colorbar(im, label=r'Temperature ($\degree$C)')
ax.set_title('Linearly Interpolated IMShow Plot')

#%%

# Successful Interpolated IMShow Plot (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 100, 50

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 0, 200

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude, depth),
             values = temperature,
             xi = (X, Y),
             method = 'linear')

# Plot the results
fig, ax = plt.subplots(figsize=(12,8), dpi=300)
im = ax.imshow(Z, cmap=plt.cm.jet, interpolation='spline36')
ax.set_xlabel(r'Longitude ($\degree$E)')
ax.set_ylabel('Depth (m)')
fig.colorbar(im, label=r'Temperature ($\degree$C)')
ax.set_title('Linearly Interpolated IMShow Plot')


#%%

# Raw Scatter Plot with Contour Lines (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 25, 25

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 200, 0

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude, depth),
             values = temperature,
             xi = (X, Y),
             method = 'linear')

# Plot the results
plt.figure(figsize=(12,8), dpi=300)
contours = plt.contour(X, Y, Z, s=3, colors='white')
plt.clabel(contours, inline=True, fontsize=15)
plt.scatter(longitude, depth, c=temperature, cmap=plt.cm.jet, s=100)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel('Depth (m)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.title('Raw Scatter Plot with Contour Lines')

#%%


# Set up new dataframe


# New Dataframe where Temp < 12 C
df2 = df.drop(df[(df['depth'] > 15)].index)

# Define Variables
latitude2 = df2['latitude']
longitude2 = df2['longitude']
depth2 = df2['depth']
temperature2 = df2['temperature']
salinity2 = df2['salinity']
do2 = df2['dissolved_oxygen']

#%%

# Successful Raw Scatter Plot (Longitude vs Depth)

fig, ax1 = plt.subplots(figsize=(12, 8), dpi=300)

scat2 = ax1.scatter(longitude2, depth2, c=temperature2, cmap=plt.cm.jet, s=50)


ax1.invert_yaxis()
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel(r'Longitude ($\degree$E)')
ax1.set_title('Raw Scatter Plot')
fig.colorbar(scat2, label=r'Temperature ($\degree$C)')

#%%

# Linearly Interpolated PColorMesh Plot (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 100, 50

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 15, 4

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude2, depth2),
             values = temperature2,
             xi = (X, Y),
             method = 'linear')

# Plot the results
plt.figure(figsize=(12,8), dpi=300)
plt.pcolormesh(X, Y, Z, cmap=plt.cm.jet)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel('Depth (m)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.title('Linearly Interpolated PColorMesh Plot')

#%%

# Unsuccessful Interpolated Contour Plot (Longitude vs Depth)


# grid sizing

# number of grid points:
xn, yn = 100, 50

# grid window
xmin, xmax = -124.9, -124.2
ymin, ymax = 16, 4

# Generate a regular grid to interpolate the data.
X, Y = np.meshgrid(np.linspace(xmin, xmax, xn), 
                   np.linspace(ymin, ymax, yn))

# Interpolate using "cubic" method
Z = griddata(points = (longitude2, depth2),
             values = temperature2,
             xi = (X, Y),
             method = 'linear')

# Plot the results
plt.figure(figsize=(12,8), dpi=300)
contours = plt.contour(X, Y, Z, s=3, colors='white')
plt.clabel(contours, inline=True, fontsize=15)
plt.contourf(X, Y, Z, cmap=plt.cm.jet)
plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel(r'Longitude ($\degree$E)')
plt.ylabel('Depth (m)')
plt.colorbar(label=r'Temperature ($\degree$C)')
plt.title('Linearly Interpolated Contour Plot')