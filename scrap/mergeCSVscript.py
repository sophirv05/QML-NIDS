import pandas as pd

CHUNK_SIZE = 50000
csv_file_list = ["BCCC-CIC-CSE-IDS2018/Thursday_15_02_2018/thursday_15_02_2018_benign/thursday_15_02_2018_benign.csv", "BCCC-CIC-CSE-IDS2018/Thursday_15_02_2018/thursday_15_02_2018_DoS_Golden_Eye/thursday_15_02_2018_DoS_Golden_Eye.csv"]
output_file = "mergedDoSGoldenEye.csv"

first_one = True
for csv_file_name in csv_file_list:

    if not first_one: # if it is not the first csv file then skip the header row (row 0) of that file
        skip_row = [0]
    else:
        skip_row = []

    chunk_container = pd.read_csv(csv_file_name, chunksize=CHUNK_SIZE, skiprows = skip_row, header=None)
    for chunk in chunk_container:
        chunk.to_csv(output_file, mode="a", index=False, header=False)
    first_one = False
