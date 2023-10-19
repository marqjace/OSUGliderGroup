# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:48:36 2023

@author: marqjace
"""

# Imports

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# Create Dataframe            
df = pd.read_csv('C:/Users/marqjace/slocum_python/DATA - WA Coast Sep 23/osu551-20230907T1717_c3f6_30c0_d795.csv', index_col=False, skiprows=[1])   ### if .xlsx sheet_name = sheet needs to be in ())


# Define Variables (Raw)
latitude = df['latitude']
longitude = df['longitude']
depth = df['depth']
temperature = df['temperature']
salinity = df['salinity']
do = df['dissolved_oxygen']


# # Drop all values except top right corner where glider turned
df1 = df.drop(df[(df['longitude'] < -124.3)].index)
df1 = df.drop(df[(df['latitude'] < 47.10)].index)


# Define Variables (Top Right Corner)
latitude1 = df1['latitude']
longitude1 = df1['longitude']
depth1 = df1['depth']
temperature1 = df1['temperature']
salinity1 = df1['salinity']
do1 = df1['dissolved_oxygen']


# # Drop all values except bottom left corner where glider turned
df2 = df.drop(df[(df['longitude'] > -124.85)].index)


# Define Variables (Botoom Left Corner)
latitude2 = df2['latitude']
longitude2 = df2['longitude']
depth2 = df2['depth']
temperature2 = df2['temperature']
salinity2 = df2['salinity']
do2 = df2['dissolved_oxygen']


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

# (Raw Scatter Plot (Depth vs Temperature, c=Salinity); Top Right Turn of Glider Path)

fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

plot1 = ax.scatter(temperature1, depth1, c=salinity1, cmap=plt.cm.jet)

ax.set_ylabel('Depth (m)')
ax.set_xlabel(r'Temperature ($\degree$C)')
ax.set_title('Temperature Profiles of Top Right Turn of Glider Path')
ax.invert_yaxis()
plt.colorbar(plot1, label='Salinity (PSU)')


#%%

# Raw Scatter Plot (Depth vs Temperature, c=Salinity); Bottom Left Turn of Glider Path)

fig, ax = plt.subplots(figsize=(12, 8), dpi=300)

plot2 = ax.scatter(temperature2, depth2, c=salinity2, cmap=plt.cm.jet)

ax.set_ylabel('Depth (m)')
ax.set_xlabel(r'Temperature ($\degree$C)')
ax.set_title('Temperature Profiles of Bottom Left Turn of Glider Path')
ax.invert_yaxis()
norm = mpl.colors.Normalize(vmin=29, vmax=36)
plt.colorbar(plot2, norm=norm, label='Salinity (PSU)')

