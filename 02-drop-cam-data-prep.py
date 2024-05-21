import pandas as pd
import os

# Define the CSV files to be loaded
csv_files = [
    'Holmes Reef Biomass Sites December 2022.csv',
    'Lihou Reef Biomass Sites December 2022.csv',
    'Tregrosse Reef Biomass Sites December 2022.csv'
]

# Base path for data files
base_path = 'private-src-data/CS_JCU_Benthic-habitat-drop-cams_Dec2022/derived/'

# Check if all files exist
all_files_exist = all(os.path.exists(os.path.join(base_path, file)) for file in csv_files)

if not all_files_exist:
    print("Extract not possible. The source data files are not found. The rest of the analysis can use the extract shipped with the repository. Please contact Samantha Tol (JCU) if you need the original data.")
else:
    # Load the CSV files, normalize column names, and keep only necessary columns
    data_frames = []
    necessary_columns = ['SITE', 'TEAM', 'SURVEY_NAME', 'SURVEY_DATE', 'DEPTH', 'LATITUDE', 'LONGITUDE', 'VESSEL', 'CAMERA', 'FREE_DIVIN', 'AG_COVER', 'CUSTODIAN', 'UPDATED']
    for file in csv_files:
        file_path = os.path.join(base_path, file)
        df = pd.read_csv(file_path)
        
        # Normalize column names to uppercase
        df.columns = df.columns.str.upper()
        
        # Check if all necessary columns are in the DataFrame
        missing_columns = [col for col in necessary_columns if col not in df.columns]
        if missing_columns:
            print(f"Missing columns in {file}: {missing_columns}")
        else:
            df = df[necessary_columns]  # Retain only the necessary columns
            data_frames.append(df)

    # Combine the data frames into one, if no columns are missing
    if data_frames:
        combined_csv = pd.concat(data_frames, ignore_index=True)
        # Save the combined CSV to a new file
        out_path = 'public-src-data/CS_JCU_Tol_Drop-cam_Validation_Dec-2022.csv'
        combined_csv.to_csv(out_path, index=False)
        print(f"Data extraction complete. Combined CSV file saved as '{out_path}'")
