# Coral Sea Oceanic Vegetation  (NESP MaC 2.3, AIMS)
This dataset is a vector shapefile mapping the deep vegetation on the bottom of the coral atoll lagoons in the Coral Sea within the Australian EEZ. This mapped vegetation predominantly corresponds to erect macroalgae, erect calcifying algae and filamentus algae, with an average algae benthic cover of approximately 40%. Marine vegetation on shallow reef areas were excluded due to the difficulty in distinguishing algae from coral. This dataset instead focuses on the vegetation growing on the soft sediments between the reefs in the lagoons.

This dataset was mapped from constrast enhanced Sentinel 2 composite imagery (Lawrey and Hammerton, 2022, https://doi.org/10.26274/NH77-ZW79). Most of the mapped atoll lagoon areas were 45 - 70 m deep. Mapping at such depths from satellite imagery is difficult and ambiguous due to only having a single useful colour band (Blue B2), satellite sensor noise, cloud artefacts, water clarity change, sun glint, and detector brightness shifts. To help compensate for some of these anomalies the benthic mapping was digitised manually using visual cues, focusing on locations where there were clear transitions between sandy areas (with a high benthic reflectance) and vegetation areas (with a low reflectance). These contrast transitions helped to determine the local image contrast between light and dark substrates. Many of patch reefs in the lagoons have a clear grazing halo of bare sand around their perimeter. These is often surrounded by a intensely dark halo, presumably from a high cover of algae. These concentric rings of light and dark substrate provided local references for the image brightness corresponding to high and low benthic cover.

Validation: 

The benthic reflectance was directly estimated for North Flinders Reefs and Holmes Reefs from a combination of the satellite imagery any matching high resolution bathymetry (Lawrey, 2024, https://doi.org/10.26274/s2a8-nw72). These areas then acted as a reference for developing visual techniques to estimate benthic reflectance from just the satellite imagery. These 
visual techniques were then used to map the rest of the Coral Sea where high resolution bathymetry was not available. 

The final mapped areas in Tregrosse and Lihou Reefs were validated against a drop camera survey conducted by JCU in 2022. From this 219 survey locations overlapped the atoll lagoons. Preliminary analysis indicates areas mapped has having benthic vegetation typically have 15 - 70% (average 42%) algal benthic cover, typically as a mix of erect macroalgae, erect calcarious algae (halimeda) and filamentus algae. Lagoonal areas that were mapped as sand (i.e. areas outside the mapped vegetation, but not on a reef) typically have a much lower algal benthic cover of 0 - 22% with an average of 4%. These areas were also typically turf algae. 

Limitations:

This dataset was mapped at a scale of 1:400k, with our goal being to limit the maximum boundary error to 400 m. Where the imagery was clear enough the boundary accuracy is likely to be significantly better than this threshold. For Ashmore reef the poor water visibility prevented our ability to see the benthos of 80% of the lagoon, and so we would expect a large error in the vegetation boundary for Ashmore Reef. In general the spacing of the digitisations was adjusted based on the confidence of the digitised boundary. In areas where the visibility was good the features were digitsed at a GIS screen scale of 1:25k, with a typical spacing between vertices of 100 - 200 m. In high uncertainty areas the digitised distance was increased to 500 - 1000 m. The likely error in the boundary is approximately equal vertex spacing. In many areas there is fine scale variations in the benthic cover, with fine scale variations at the scale of 100 - 300 m. Variations were only digitised if the alterations in the boundary, or the inclusion of a hole in the polygon would improve the map by at least 200 m in boundary accuracy.

The vegetation areas were categorised into three levels of vegetation density (Low, Medium and High) based on how dark the substrate appeared, relative to the nearby reference indicators (dark halos around reefs, and clear patches of presumably bare sand). In practice the accuracy of this categorisation is low, as the ambigity in the imagery made it difficult to  

This dataset was developed for inclusion into the Natural Values Ecosystem national habitat map used by Parks Australia. 

Th bottom of coral reef atolls is dominated by soft sediment accumulated from the surrounding reefs and the calcifying algae, such as halimeda that grows on the bottom of many parts of coral atoll lagoons. When viewed from satellite imagery bare sand appears appears paler than those areas that are covered in algae and coral reef hard substrate. In this dataset we focus on mapping areas that are covered in vegetation (most likely halimeda) growing on soft sediment areas. We exclude areas that correspond to exposed hard coral reef substrate. 

Challenges of mapping deep vegetation:

The contrast between substrates that have a high (sand) and low (vegetation, reef substrate) benthic reflectance reduces with depth. Below 40 m deep this difference is typically less than 0.5% of the full brightness range of the image, meaning that even small shifts in scene brightness of visual noise can make it difficult to interpret the benthic cover. 

Most of the mapped atoll lagoon areas were 45 - 70 m deep. At this depth only blue light penetrates far enough for any details of the benthos to be visible. In some cases UV light (B1 for Sentinel 2) can also penetrate to a similar depth, but it is far more sensitive to water clarity issues due to scattering in the water column, it has greater sensor noise, and its resolution is much lower (UV B1 60 m vs Blue B2 10 m). This limits the utility of using the UV channel of Sentinel 2. The green channel (B3) has a maximum visible depth of 30 m, making it unsuitable for mapping of deep vegetation. For these reasons we map the lagoonal vegetation using the Sentinel 2 blue channel.

In any one satellite image there is significant fine scale visual noise due to reflections off the surface of the water due to waves (sun glint), sensor noise, clouds and their shadows. There are also significant large and small scale shifts in brightness due to changes the relative angle of the sun, the differences in the characteristics of the staggered detectors in the satellite, plumes of colour dissolved organic matter increasing the attenutation of light through the water, and suspended sediments increasing the level of scatter light. All of these contribute to local and large scale shifts in image brightness that make estimating the absolute brightness of the reflected substrate very difficult. 

Some of these effects can be partly compensated for by incorporating additional information sources. Sun glint can be significantly corrected for using the infrared bands of the satellite images. Large scale brightness shifts and depth effects can be compensated for with matching bathymetry data and calibration sampling points with known benthic reflectance, see [Estimation of benthic reflectance from satellite imagery and bathmetry](https://doi.org/10.26274/s2a8-nw72)


# Method
The vegetation areas were mapped from Sentinel 2 composite imagery sourced from the [Coral Sea Features satellite imagery dataset](https://doi.org/10.26274/NH77-ZW79). This imagery was optimised for high depth visibility in the marine environment. This imagery allows visibility of benthic features from 40 - 60 m in the clear waters of the Coral Sea. It was produced by manually reviewing all the available low cloud cover Sentinel 2 imagery from 2015 - 2021, looking for images with low cloud cover (particularly over atoll areas), low sunglint, low waves and high water clarity. For each scene the imagery was manually ranked based on the image clarity. The clearest images were divided into two sets (each containing containing typically 2 - 6 images). The R1 set corresponded to the best images and R2 set corresponded to the next best imagery. 

Each image in the collection was corrected for sun glint by subtracting a scaled version of the infrared (B8) channel. A cloud and cloud shadow mask was applied to the image to reduce the influence of clouds. The images were converted to a composite image by forming an image stack then performing statistical median to each stack of pixels. The image processing was performed using the Google Earth Engine.

To allow the deep benthic features to be seen the blue channel of the image composites was greatly contrast enhanced to show the very faint differences in brightness due to changes in the benthos. The amount of contrast enhancement, and thus the maximum depth that could be analysed was limited by the visual anomalies in the imagery and the magnified variations in brightess across the images due to the following:
- Remanent patches from masked clouds.
- Remanent patches from cloud shadows that were not fully masked.
- Sentinel 2 MSI detector brightness offsets. 
- Uncorrected tonal change across the full Sentinel swath (western side is brighter than the eastern side).
- Coloured Dissolved Organic Matter in the water increases the light attenuation, making areas darker than they would appear in clear water. This tends to occur in areas with low water flushing.
- Sensor noise in the imagery.
- Remanent sun glint correction due to surface waves.   

The benthic cover (vegetation, coral or sand) was determined by manual inspection of the contrast enhanced imagery, looking for the following visual cues:
- Grazing halos around patch reefs: pale ring corresponding to bare sand surrounding a textured dark, rounded feature. The grazing halo is typically at a similar depth to the surrounding area and so serves as a local brightness reference for a high benthic reflectance substrate. Often the grazing halo will be surrounded by a dark halo of extra dense vegetation. This dark ring provides a brightness reference for high density vegetation. These brightness thresholds are then used to assess the density of the more distance area around the reef. If the area is close in darkness to the dark ring around the reef then it is considered high density vegetation. If it is closer to the grazing halo bare sand then it is considered to be free of vegetation.
-  Reefs without grazing halos: In some cases the patch reefs do not have a pale grazing halo around them.  In these cases we identify the reef by its pale circular shape, combined with evidence that it is a tall structure, by checking if it is visible in the green channel (B3), indicating that it reaches within 30 m of the surface or the available bathymetry indicates the vertical nature of the reef. These patch reefs also typically have a dark halo around them, often darker than the surrounding flat lagoonal areas. These dark rings are used as an indication of the brightness level corresponding to high density vegetation. 
- Low relief flat reefs: In the western side of Tregrosse Reefs platform there are quite a few dark round features that according to the bathymetry have only a limited relief of less than 8 m. These often have a small grazing halo around their border. It is unclear what the exact nature is of these reefs are, however we assume they are reefal in nature and so we exclude them from the vegetation mapping.
- On the atoll plains, particularly on the western side of Tregrosse Reefs platform there are large patches of dark substrate that have clearly blank sandy patches, unrelated to the presence of reefs. In these cases the pale patches are assumed to be blank sand and serve as a high benthic reflectance guide.


In practice at depth only sandy areas are visible as they reflect enough light to be visible above the surrounding visual noise. These sandy areas create a negative space around reefs and patches of dark vegetation. Most areas of the coral atoll lagoons are gently sloping meaning that sudden changes in visual brightness are likely due to changes in benthic reflectance, rather than changes in depth. We use this fact to find the visual edge of regions of low benthic reflectance. Scattered across most lagoons are hundreds of patch coral reefs. These rise up from lagoonal floor and are typically surrounded by a grazing halo of bare sand surrounding the perimeter of the reef. This makes them relatively easy to spot and the grazing halos provide a visual reference for the brightness of bare sand. Often the grazing halo is surrounded by a second darker ring of dense vegetation, making the reefs appear as a bulls eye. We confirmed that these dark rings are likely to be dark vegetation, rather than a deep ring, by looking at transects of bathymetry across these features on North Flinders Reefs, where high resolution bathymetry (Beaman, 2017) was available. These transects show that the dark rings surrounding the grazing halos are unfact shallower then the bare sand, indicating that they are raised, likely due to the accumulation of halimeda sediment.

[Diagram showing transect across reef features with grazing halo]


It was very difficult to determine the extent of the vegetation in the lagoon of Ashmore Reef. The lagoon appears to have a low flushing rate and a high amount of CDOM accumulates in the lagoon, reducing the visibility to the point were most of the benthos of most of the lagoon is not visible. To help map this reef the full series of Sentinel 2 images was carefully reviewed for tonal differences that indicate the areas of sand and vegetation. Only 20% of the boundary of the vegetation could be accurately determined, the rest of the mapped boundary is speculative. 

Most of Tregrosse Reefs platform is 60 to 70 m deep, which is right at visible limit for the satellite imagery.  


# References
Lawrey, E., & Hammerton, M. (2022). Coral Sea features satellite imagery and raw depth contours (Sentinel 2 and Landsat 8) 2015 – 2021 (AIMS) [Data set]. eAtlas. https://doi.org/10.26274/NH77-ZW79

Lawrey, E. (2024). Estimating benthic reflectance of deep coral atoll lagoons from satellite imagery and bathymetry - Analysis code and case studies (NESP MaC 2.3, AIMS) [Data set]. eAtlas. https://doi.org/10.26274/s2a8-nw72

# Source data
The following datasets were used in the development of this datasets. These are provided here for provenance reasons and to allow the dataset to be reproduced, noting that the imagery was hand digitised.

These large source datasets are not bundled with this data package to minimise the size of this dataset.

The `01-download-src-data.py` is a Python script that downloads the datasets that are not bundled with this dataset. See the script comments as to how to run this script. This download the source datasets.

This section also describes the origin of each of the datasets in case the download script doesn't work.

## GBR_GA_Great-Barrier-Reef-Bathy-30m_2020
- **Citation:** Beaman, R.J. 2017. High-resolution depth model for the Great Barrier Reef - 30 m. 
  Geoscience Australia, Canberra. http://dx.doi.org/10.4225/25/5a207b36022d2
- **Licence:** Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/
- **Metadata:** http://pid.geoscience.gov.au/dataset/ga/115066 additional information https://www.deepreef.org/2018/03/05/gbr-grid/
- **Direct download:** https://files.ausseabed.gov.au/survey/Great%20Barrier%20Reef%20Bathymetry%202020%2030m.zip
- **Second download:** 
    - https://ausseabed-public-warehouse-bathymetry.s3.ap-southeast-2.amazonaws.com/L3/0b9ad3f3-7ade-40a7-ae70-f7c6c0f3ae2e/Great_Barrier_Reef_A_2020_30m_MSL_cog.tif
    - https://ausseabed-public-warehouse-bathymetry.s3.ap-southeast-2.amazonaws.com/L3/4a6e7365-d7b1-45f9-a576-2be8ff8cd755/Great_Barrier_Reef_B_2020_30m_MSL_cog.tif
    - https://ausseabed-public-warehouse-bathymetry.s3.ap-southeast-2.amazonaws.com/L3/3b171f8d-9248-4aeb-8b32-0737babba3c2/Great_Barrier_Reef_C_2020_30m_MSL_cog.tif
    - https://ausseabed-public-warehouse-bathymetry.s3.ap-southeast-2.amazonaws.com/L3/7168f130-f903-4f2b-948b-78508aad8020/Great_Barrier_Reef_D_2020_30m_MSL_cog.tif

## GBR_GA_Great-Barrier-Reef-Bathy-100m_2020
- **Citation**: Beaman, R.J. 2020. High-resolution depth model for the Great Barrier Reef and Coral Sea - 100 m. 
  Geoscience Australia, Canberra. http://dx.doi.org/10.26186/5e2f8bb629d07
- **Licence:** Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/
- **Metadata:** http://pid.geoscience.gov.au/dataset/ga/133163
- **Direct download:** https://files.ausseabed.gov.au/survey/Great%20Barrier%20Reef%20Bathymetry%202020%20100m.zip
- **Second download:** https://ausseabed-public-warehouse-bathymetry.s3.ap-southeast-2.amazonaws.com/L3/de1e648f-b45a-4b34-821f-e421d7670fa7/Great_Barrier_Reef_2020_100m_MSL_cog.tif


## CS_AIMS_Coral-Sea-Features_Img
- **Citation:** Lawrey, E., & Hammerton, M. (2022). Coral Sea features satellite imagery and raw depth contours (Sentinel 2 and Landsat 8) 2015 – 2021 (AIMS) [Data set]. eAtlas. https://doi.org/10.26274/NH77-ZW79
- **Licence:** Creative Commons Attribution 4.0 International Licence http://creativecommons.org/licenses/
- **Metadata:** https://doi.org/10.26274/NH77-ZW79
- **Download folder:** https://nextcloud.eatlas.org.au/apps/sharealias/a/cs-aims-coral-sea-features-img
- **Direct downloads:** 
    - https://nextcloud.eatlas.org.au/s/NjbyWRxPoBDDzWg/download?path=%2Flossless%2FCoral-Sea&files=S2_R2_DeepFalse
    - https://nextcloud.eatlas.org.au/s/NjbyWRxPoBDDzWg/download?path=%2Flossless%2FCoral-Sea&files=S2_R1_DeepFalse
    - https://nextcloud.eatlas.org.au/s/NjbyWRxPoBDDzWg/download?path=%2Flossless%2FCoral-Sea&files=L8_R1_DeepFalse
Only the following portions of this dataset were download: S2_R2_DeepFalse, S2_R1_DeepFalse, L8_R1_DeepFalse for the Coral Sea.


## Additional imagery
For several reefs the imagery that was available of the Google Earth Engine was limited and thus the image available from the CS_AIMS_Coral-Sea-Features_Img dataset is not sufficient to map the vegetation accurately. To supplement this imagery we obtain and process imagery from Geoscience Australia with the data hosted on NCI. 

## GA Landsat 8 OLI/TIRS Analysis Ready Data Collection 3
https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/132317

We use SentinelHub EO browser to find the dates with clear imagery.

https://apps.sentinel-hub.com/eo-browser/?zoom=12&lat=-21.19225&lng=155.68777&themeId=DEFAULT-THEME&visualizationUrl=https%3A%2F%2Fservices.sentinel-hub.com%2Fogc%2Fwms%2Fe35192fe-33a1-41f3-b798-b755e771c5a5&evalscript=Ly9WRVJTSU9OPTMKZnVuY3Rpb24gc2V0dXAoKSB7CiAgcmV0dXJuIHsKICAgIGlucHV0OiBbIkIwMiIsIkIwNyIsICJkYXRhTWFzayJdLAogICAgb3V0cHV0OiB7IGJhbmRzOiA0IH0KICB9Owp9CgpmdW5jdGlvbiBldmFsdWF0ZVBpeGVsKHNhbXBsZSkgewogIHMyID0gNCooc2FtcGxlLkIwMiAtIHNhbXBsZS5CMDcpLTAuMzYKICByZXR1cm4gW3MyLCBzMiwgczIsIHNhbXBsZS5kYXRhTWFza107Cn0%3D&datasetId=AWS_LOTL1&fromTime=2023-01-10T00%3A00%3A00.000Z&toTime=2023-01-10T23%3A59%3A59.999Z&gamma=0.3&demSource3D=%22MAPZEN%22#custom-script

```
//VERSION=3
function setup() {
  return {
    input: ["B02","B07", "dataMask"],
    output: { bands: 4 }
  };
}
function evaluatePixel(sample) {
  s2 = 4*(sample.B02 - sample.B07)-0.36
  return [s2, s2, s2, sample.dataMask];
}
```
We then worked out the matching images in the NCI catalogue for downloading since it is not possible to directly download the imagery from Sentinel Hub. It should be noted that the time slider on EO Browser does not indicate if the image is from Landsat 8 or Landsat 9. They are combined into a single time series.

The following is the root of the Landsat 8 and Landsat 9 imagery.
https://dapds00.nci.org.au/thredds/catalog/xu18/catalog.html

### Ashmore Reef
Band 2 and Band 7
Download page: https://dapds00.nci.org.au/thredds/catalog/xu18/ga_ls9c_ard_3/097/067/2022/09/28/catalog.html
Download links: 
https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls9c_ard_3/097/067/2022/09/28/ga_ls9c_nbar_3-2-1_097067_2022-09-28_final_band02.tif
https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls9c_ard_3/097/067/2022/09/28/ga_ls9c_nbar_3-2-1_097067_2022-09-28_final_band07.tif
https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls8c_ard_3/097/067/2022/09/04/ga_ls8c_nbar_3-2-1_097067_2022-09-04_final_band02.tif
https://dapds00.nci.org.au/thredds/fileServer/xu18/ga_ls8c_ard_3/097/067/2022/09/04/ga_ls8c_nbar_3-2-1_097067_2022-09-04_final_band07.tif


### Kenn Reef
088/075 - GA doesn't have imagery for this location

`data-cache`: This contains datasets that are downloaded by 01-get-source-data. These are generally large source datasets and so are not distributed with this project. This are in their own folder to allow then to be deleted prior to publishing this data package.