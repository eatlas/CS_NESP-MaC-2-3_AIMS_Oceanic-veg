from data_downloader import DataDownloader
import os

# Create an instance of the DataDownloader class
downloader = DataDownloader(download_path="working/data-cache")


print("Downloading source data files. This will take a while ...")



# --------------------------------------------------------
# CS_AIMS_Coral-Sea-Features_Img
# Citation: Lawrey, E., & Hammerton, M. (2022). Coral Sea features satellite imagery and raw depth contours (Sentinel 2 and Landsat 8) 2015 – 2021 (AIMS) [Data set]. eAtlas. https://doi.org/10.26274/NH77-ZW79
# Licence: Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/
# Metadata: https://doi.org/10.26274/NH77-ZW79
# Download folder: https://nextcloud.eatlas.org.au/apps/sharealias/a/cs-aims-coral-sea-features-img
# DeepFalse R1 and R2 styling
dataset_path = os.path.join(downloader.download_path,"CS_AIMS_Coral-Sea-Features_Img")

# The download includes subfolders 'S2_R2_DeepFalse' so when we unpack the zip
# the data will go into that folder. To know if we have already done this download and unpack we
# need to look for this final folder.

# Unpack all the projects such as S2_R2_DeepFalse, into the dataset folder without the original
# full path of lossless/Coral-Sea/S2_R2_DeepFalse. This was done to reduce the path lengths as
# I got maximum path length errors in Windows.

def download_sat_product(sat_product):
    if os.path.exists(os.path.join(dataset_path, sat_product)):
        print(f"Skipping download and unzip of '{sat_product}' as folder already exists")
    else:
        zip_path = os.path.join(downloader.tmp_path, f"{sat_product}.zip")
        downloader.download(f'https://nextcloud.eatlas.org.au/s/NjbyWRxPoBDDzWg/download?path=%2Flossless%2FCoral-Sea&files={sat_product}', zip_path)
        downloader.unzip(zip_path,dataset_path, sat_product) 
      

# Download the true colour image of North Flinders Reef. This is our reference
# reef and we want to demonstrate what it looks like in TrueColour.
#downloader.download(f'https://nextcloud.eatlas.org.au/s/NjbyWRxPoBDDzWg/download?path=%2Flossless%2FCoral-Sea%2FS2_R1_TrueColour&files=#CS_AIMS_Coral-Sea-Features_Img_S2_R1_TrueColour_55KFA.tif', #f'{dataset_path}/S2_R1_TrueColour/CS_AIMS_Coral-Sea-Features_Img_S2_R1_TrueColour_55KFA.tif')


# Download indivdual satellite provides as we don't want the entire dataset
download_sat_product('S2_R2_DeepFalse')
download_sat_product('S2_R1_DeepFalse')
download_sat_product('L8_R1_DeepFalse')

		

    
# ----------------------------------------------------------------------
#    Landsat and Sentinel imagery from Geoscience Australia, via NCI
#dataset_path = os.path.join(DOWNLOAD_PATH,"AU_GA_Landsat-8-OLI_Collection-3","raw")
#Path(dataset_path).mkdir(parents=True, exist_ok=True)
#download('https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls9c_ard_3/097/067/2022/09/28/ga_ls9c_nbar_3-2-1_097067_2022-09-28_final_band02.tif', \
#        os.path.join(dataset_path, "ga_ls9c_nbar_3-2-1_097067_2022-09-28_final_band02.tif"))
#download('https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls9c_ard_3/097/067/2022/09/28/ga_ls9c_nbar_3-2-1_097067_2022-09-28_final_band07.tif', \
#        os.path.join(dataset_path, "ga_ls9c_nbar_3-2-1_097067_2022-09-28_final_band07.tif"))
#        
#download('https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls8c_ard_3/097/067/2022/09/04/ga_ls8c_nbar_3-2-1_097067_2022-09-04_final_band02.tif', \
#        os.path.join(dataset_path, "ga_ls8c_nbar_3-2-1_097067_2022-09-04_final_band02.tif"))
#download('https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls8c_ard_3/097/067/2022/09/04/ga_ls8c_nbar_3-2-1_097067_2022-09-04_final_band07.tif', \
#        os.path.join(dataset_path, "ga_ls8c_nbar_3-2-1_097067_2022-09-04_final_band07.tif"))


#----------------------------------------------------
# Lawrey, E., Hammerton, M. (2024). Marine satellite imagery test collections (AIMS) [Data set]. eAtlas.
# https://doi.org/10.26274/zq26-a956


direct_download_url = 'https://nextcloud.eatlas.org.au/s/orNy3H9Cp5ZBQjQ/download?path=%2F%2F55KFA-8'
downloader.download_and_unzip(direct_download_url, 'CS_NESP-MaC-2-3_AIMS_Benth-Reflect')

#direct_download_url = #'https://nextcloud.eatlas.org.au/apps/sharealias/a/9tbZP8Rbk5FxiQ6/download?path=%2FCS_NESP-MaC-2-3_AIMS_Oceanic-veg'
#downloader.download_and_unzip(direct_download_url, 'Wld_AIMS_Marine-sat-img_Oceanic-veg')

#----------------------------------------------------
# Lawrey, E., Hammerton, M. (2024). Marine satellite imagery test collections (AIMS) [Data set]. eAtlas.
# https://doi.org/10.26274/zq26-a956
direct_download_url = 'https://nextcloud.eatlas.org.au/s/9tbZP8Rbk5FxiQ6/download?path=%2FCS_NESP-MaC-2-3_AIMS_Oceanic-veg'
# Define the patterns to search for
patterns = [
    'CS_NESP-MaC-2-3_AIMS_Oceanic-veg/*',
]
# Use this approach as the zip file contains an internal CS_NESP-MaC-2-3_AIMS_Benthic-reflectance/ that makes
# the overall paths too long. 
downloader.download_unzip_keep_subset(direct_download_url, patterns, 'Wld_AIMS_Marine-sat-img_Oceanic-veg')

        
