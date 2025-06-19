import pandas as pd
import numpy as np

# Load the CSV (you may need to change this to your actual filename)
filename = 'BCCC-CIC-CSE-IDS2018/Friday-02-03-2018/friday_02_03_2018_benign/friday_02_03_2018_benign.csv'

# Load the first 50 rows
df = pd.read_csv(filename, nrows=100)

# Select the top 5 anomaly-related features
selected_features = [
    'total_payload_bytes',
    'bytes_rate',
    'packets_rate',
    'avg_segment_size',
    'duration',
    'fwd_bytes_rate',
    'bwd_bytes_rate',
    'syn_flag_counts'

]

# Extract the relevant features
features_df = df[selected_features]

# Save as CSV
features_df.to_csv('CSV-100-botnet-benign.csv', index=False)

# # Save as a NumPy array
# features_array = features_df.to_numpy()
# np.save('100-botnet-benign.npy', features_array)
