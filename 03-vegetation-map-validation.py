# Script: analyze_data.py
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the combined CSV file
combined_csv = pd.read_csv('public-src-data/CS_JCU_Tol_Drop-cam_Validation_Dec-2022.csv')

# Convert the combined DataFrame to a GeoDataFrame
gdf_points = gpd.GeoDataFrame(
    combined_csv,
    geometry=gpd.points_from_xy(combined_csv.LONGITUDE, combined_csv.LATITUDE)
)

# Load reef boundaries shapefile
reef_boundaries = gpd.read_file('working/data-cache/CS_AIMS_Coral-Sea-Features_2024/CS_AIMS_Coral-Sea-Features_2024_Reef-boundaries.shp')

# Spatial join to find points within reef boundaries
gdf_with_reef = gpd.sjoin(
    gdf_points,
    reef_boundaries,
    how="left",
    op='intersects'
)
gdf_with_reef['IN_REEF'] = gdf_with_reef.index_right.notnull()

# Load oceanic vegetation shapefile
oceanic_vegetation = gpd.read_file('public/CS_NESP-MaC-2-3_AIMS_Oceanic-veg.shp')

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

# Save final DataFrame as CSV for GIS usage
gdf_final[['LATITUDE', 'LONGITUDE', 'AG_COVER', 'IN_REEF', 'Density']].to_csv('public/CS_JCU_Tol_Drop-cam-Dec-2022_Validation.csv', index=False)

# Filter out points that are in the reef for the plot
gdf_for_plot = gdf_final[gdf_final['IN_REEF'] == False]

# Define the order for the density categories
density_order = ['None', 'Low', 'Medium', 'High']

# Sort the data by 'Density' according to the specified order
gdf_for_plot['Density'] = pd.Categorical(gdf_for_plot['Density'], categories=density_order, ordered=True)
sorted_gdf = gdf_for_plot.sort_values(by='Density')

VARIABLE = 'AG_COVER'
VAR_TITLE = 'Drop Camera Algae Cover'

# Combine 'Low' and 'Medium' into 'Low-Medium'
sorted_gdf['Density'] = sorted_gdf['Density'].replace(['Low', 'Medium'], 'Low-Medium')

# Calculate the number of points in each category
counts = sorted_gdf.groupby('Density')[VARIABLE].count()

# Create new labels with counts, e.g., 'None (n=56)'
new_labels = [f'{label}, n={counts[label]}' for label in counts.index]

# Plot AG_COVER as a function of vegetation density
fig, ax = plt.subplots(figsize=(9, 6))  # Width, Height in inches
sorted_gdf.boxplot(column=VARIABLE, by='Density', ax=ax)
ax.set_title(f'Drop Camera Algae Cover vs Satellite Estimated Vegetation Density\nExcluding locations within reef boundaries', fontsize=14)
#fig.suptitle('Excluding locations within reef boundaries', fontsize=10, color='gray')
ax.set_xticklabels(new_labels, fontsize=10)
ax.set_xlabel('Vegetation Density', fontsize=12)
ax.set_ylabel('Drop Camera Algae Cover (%)', fontsize=12)

# Adjust the layout to reduce padding and prevent label overlap
plt.subplots_adjust(left=0.08, right=0.95, top=0.9, bottom=0.1)

plt.suptitle('')

# Save the plot to a PNG file
plt.savefig('public/CS_JCU_Tol_Drop-cam-Dec-2022_Validation.png', dpi=300)

plt.show()
