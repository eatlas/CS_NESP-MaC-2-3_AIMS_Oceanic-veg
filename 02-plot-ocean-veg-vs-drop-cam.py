"""
Eric Lawrey
This script performs a comparison between the vegetation density determined
from the satellite mapping with drop camera surveys conducted by JCU. The
JCU data is not yet published and so is not included in this dataset. This
analysis was completed as verification that the satellite mapping was producing
sensible data corresponding to the actual marine vegetation.

This analysis was also performed on preliminary data from JCU.
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV files
csv_files = [
    'Holmes Reef Biomass Sites December 2022.csv',
    'Lihou Reef Biomass Sites December 2022.csv',
    'Tregrosse Reef Biomass Sites December 2022.csv'
]

# Note this data is not yet available: private-src-data/CS_JCU_Benthic-habitat-drop-cams_Dec2022
data_frames = [pd.read_csv(f'private-src-data/CS_JCU_Benthic-habitat-drop-cams_Dec2022/derived/{file}') for file in csv_files]

# Combine CSV files into one DataFrame
combined_csv = pd.concat(data_frames, ignore_index=True)

# Convert the combined DataFrame to a GeoDataFrame
gdf_points = gpd.GeoDataFrame(
    combined_csv,
    geometry=gpd.points_from_xy(combined_csv.Longitude, combined_csv.Latitude)
)

# Load reef boundaries shapefile
reef_boundaries = gpd.read_file('working/data-cache/CS_AIMS_Features-boundaries/CS_AIMS_Coral-Sea-Features_Reef-boundaries_Stage12_2.shp')

# Spatial join to find points within reef boundaries
gdf_with_reef = gpd.sjoin(
    gdf_points,
    reef_boundaries,
    how="left",
    op='intersects'
)
gdf_with_reef['IN_REEF'] = gdf_with_reef.index_right.notnull()

# Load oceanic vegetation shapefile
oceanic_vegetation = gpd.read_file('CS_NESP-MaC-2-3_AIMS_Oceanic-veg.shp')


# Join the density value from the oceanic vegetation
gdf_final = gpd.sjoin(
    gdf_with_reef, 
    oceanic_vegetation[['Density', 'geometry']], 
    how="left", 
    op='intersects', 
    lsuffix='_left', 
    rsuffix='_right')

# Assign 'None' to points outside oceanic vegetation areas
gdf_final['Density'] = gdf_final['Density'].fillna('None')

# Save intermediate GeoDataFrame as GeoJSON for inspection
gdf_final.to_file("output_geojson_file.geojson", driver='GeoJSON')

# Filter out points that are in the reef for the plot
gdf_for_plot = gdf_final[gdf_final['IN_REEF'] == False]

# Define the order for the density categories
density_order = ['None', 'Low', 'Medium', 'High']

# Sort the data by 'Density' according to the specified order
gdf_for_plot['Density'] = pd.Categorical(gdf_for_plot['Density'], categories=density_order, ordered=True)
sorted_gdf = gdf_for_plot.sort_values(by='Density')

VARIABLE = 'AG_COVER'
VAR_TITLE = 'Algae Cover'

# Combine 'Low' and 'Medium' into 'Low-Medium'
# We do this because there is only 2 survey locations overlapping
# the Low category and so this doesn't represent a good representation
# of the distribution.
sorted_gdf['Density'] = sorted_gdf['Density'].replace(['Low', 'Medium'], 'Low-Medium')

# Calculate the number of points in each category
counts = sorted_gdf.groupby('Density')[VARIABLE].count()

# Create new labels with counts, e.g., 'None (n=56)'
new_labels = [f'{label}, n={counts[label]}' for label in counts.index]

# Plot BENTH_COVER as a function of vegetation density
fig, ax = plt.subplots()
sorted_gdf.boxplot(column=VARIABLE, by='Density', ax=ax)
ax.set_title(f'{VAR_TITLE} vs Vegetation Density (Excluding In-Reef Points)')
# Set the new labels on the x-axis
ax.set_xticklabels(new_labels)
ax.set_xlabel('Vegetation Density')
ax.set_ylabel(VAR_TITLE)
plt.suptitle('')
plt.show()

