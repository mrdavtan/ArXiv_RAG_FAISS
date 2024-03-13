import os

# Get the size of the file in bytes
file_size_bytes = os.path.getsize('compressed_array.npz')

# Convert bytes to megabytes
file_size_mb = file_size_bytes / (1024 * 1024)

print("File size:", file_size_mb, "MB")


# How to load the saved array

# Load the compressed array
loaded_embeddings = np.load('compressed_array.npz')

# Access the array by the name you specified ('my_array' in this case)
loaded_embeddings = loaded_embeddings['array_data']

loaded_embeddings.shape

# Save the DataFrame in compressed format
df_data.to_csv('compressed_dataframe.csv.gz', compression='gzip', index=False)




