import os

# Define the path to the images and masks
image_path = 'Dataset/WesternLake/image'
mask_path = 'Dataset/WesternLake/mask'

# Get the list of images and masks in the folder
image_list = os.listdir(image_path)
mask_list = os.listdir(mask_path)

# Loop through the images
for image in image_list:
    # Extract the base name of the image (without the file extension)
    base_name = os.path.splitext(image)[0]
    # Define the expected name for the corresponding mask
    expected_mask_name = f'{base_name}_mask.tif'
    # Check if the expected mask exists in the mask folder
    if expected_mask_name not in mask_list:
        print(
            f'Warning: corresponding mask for image {image} not found in {mask_path}')
    else:
        print(f'Found corresponding mask for image {image}')
