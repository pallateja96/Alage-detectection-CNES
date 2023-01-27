import numpy as np
import os
from PIL import Image
mask_path = 'Dataset/WesternLake/mask/'

mask_list = os.listdir(mask_path)
# Loop through the images
for mask_file in mask_list:
    # Extract the base name of the image (without the file extension)
    
    base_name = os.path.splitext(mask_file)[0]
    if base_name != '.DS_Store':
        # Load the mask image
        mask = np.array(Image.open(mask_path+base_name+".tif"))
        # mask = np.expand_dims(mask, axis=-1)
        # Create an empty array to store the one-hot encoded mask
        one_hot_mask = np.zeros((mask.shape[0], mask.shape[1], 12), dtype=np.uint8)
        print(mask_file)
        mask = mask.reshape(
            mask.shape[0], mask.shape[1])
        # Creating the one-hot encoded mask with 1s at the positions corresponding to the pixel values in the original mask
        one_hot_mask[:, :, 0] = np.where(mask == 0, 1, 0)  # Water class
        # Algae class 1 = 20.000 cells/ml Very Low
        one_hot_mask[:, :, 1] = np.where((mask >= 1) & (mask <= 49), 1, 0)
        # Algae class 2 = 100.000 cells/ml Low
        one_hot_mask[:, :, 2] = np.where((mask >= 50) & (mask <= 99), 1, 0)

        # Algae class 3 = 1 000.000 cells/ml Moderate
        one_hot_mask[:, :, 3] = np.where((mask >= 100) & (mask <= 149), 1, 0)

        # Algae class 4 = 3 000.000 cells/ml High
        one_hot_mask[:, :, 4] = np.where((mask >= 150) & (mask <= 199), 1, 0)

        # Algae class 5 = 7 000.000 cells/ml Very High
        one_hot_mask[:, :, 5] = np.where((mask >= 200) & (mask <= 249), 1, 0)

       # Saturated pixel class
        one_hot_mask[:, :, 6] = np.where(mask == 250, 1, 0)   
         # Borders class
        one_hot_mask[:, :, 7] = np.where(mask == 251, 1, 0)  
         # Land class
        one_hot_mask[:, :, 8] = np.where(mask == 252, 1, 0)
       # Cloud class
        one_hot_mask[:, :, 9] = np.where(mask == 253, 1, 0) 
          # Mixed class
        one_hot_mask[:, :, 10] = np.where(mask == 254, 1, 0) 
         # No data class
        one_hot_mask[:, :, 11] = np.where(mask == 255, 1, 0) 

        # Save the one-hot encoded mask as a binary file
        np.save(
            "Dataset/WesternLake/encodedmask/"f'{base_name}.npy', one_hot_mask)
        