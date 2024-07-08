Python Code.txt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset
file_path = 'C:\\Users\\iTee\\Downloads\\YOBE CLUSTER DATA.xlsx'
data = pd.read_excel(file_path)

# Assuming your dataset has 'Latitude' and 'Longitude' columns
lat_long = data[['Latitude', 'Longitude']].dropna()

# Convert DataFrame to NumPy array
lat_long_np = lat_long.to_numpy()

# Define the number of clusters
num_clusters = 6

# Perform K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(lat_long_np)

# Add the cluster labels to the original data
lat_long['cluster'] = kmeans.labels_

# Adding cluster labels back to the main dataframe
data = data.dropna(subset=['Latitude', 'Longitude'])
data['cluster'] = kmeans.labels_

# Columns to check for outliers
columns_to_check = ['APC', 'LP', 'PDP', 'NNPP']  # Replace 'Column1' and 'Column2' with actual column names

# Calculate Z-scores for the specified columns
for column in columns_to_check:
    data[f'zscore_{column}'] = zscore(data[column])

# Determine outliers based on Z-score threshold
zscore_threshold = 3
data['outlier'] = (np.abs(data['zscore_APC']) > zscore_threshold) | \
                  (np.abs(data['zscore_LP']) > zscore_threshold) | \
                  (np.abs(data['zscore_PDP']) > zscore_threshold) | \
                  (np.abs(data['zscore_NNPP']) > zscore_threshold)

# Save the dataset with outliers flagged
output_file_path = 'C:\\Users\\iTee\\Downloads\\HNG_WITH_OUTLIERS_DATA.csv'
data.to_csv(output_file_path, index=False)

#print("CSV file with outliers has been saved successfully.")

# Optional: Print outliers
outliers = data[data['outlier'] == True]
print("Outliers found:\n", outliers)

# Visualization of clusters
plt.figure(figsize=(10, 8))
plt.scatter(data['Longitude'], data['Latitude'], c=data['cluster'], cmap='viridis', s=100, alpha=0.8, edgecolors='k', label='Cluster')

# Highlight outliers
outlier_data = data[data['outlier']]
plt.scatter(outlier_data['Longitude'], outlier_data['Latitude'], c='red', s=100, alpha=0.8, edgecolors='k', label='Outlier')

plt.title('K-means Clustering of Election Data with Outliers Highlighted')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='Cluster')
plt.legend()
plt.grid(True)

# Save the plot to a file
plot_file_path = 'C:\\Users\\iTee\\Downloads\\Outlier_plot.png'
plt.savefig(plot_file_path)
print(f"Cluster plot saved to '{plot_file_path}'.")

# Show the plot
plt.show()

# Export the clustered data to an Excel file
output_excel_file_path = 'C:\\Users\\iTee\\Downloads\\YOBE_CLUSTERED_DATA.xlsx'
data.to_excel(output_excel_file_path, index=False)
print(f"Clustered data exported to '{output_excel_file_path}'.")
