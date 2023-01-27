import os

# Define the path to the images and masks
image_path = 'Dataset/WesternLake/image'
mask_path = 'Dataset/WesternLake/mask'
# Define the new annotation
new_annotation = 'image'

# Get the list of images and masks in the folder
image_list = os.listdir(image_path)
mask_list = os.listdir(mask_path)
i = 0
# Loop through the images
for image in image_list:
    # Extract the base name of the image (without the file extension)
    base_name = os.path.splitext(image)[0]
    # Define the new name for the image
    new_image_name = f'image_{i+1}.tif'
    # Define the full paths for the old and new images
    old_image_path = os.path.join(image_path, image)
    new_image_path = os.path.join(image_path, new_image_name)
    # Rename the image
    os.rename(old_image_path, new_image_path)

    expected_mask_name = f'{base_name}_mask.tif'
    if expected_mask_name in mask_list:
        new_mask_name = f'mask_{i+1}.tif'
        old_mask_path = os.path.join(mask_path, expected_mask_name)
        new_mask_path = os.path.join(mask_path, new_mask_name)
        os.rename(old_mask_path, new_mask_path)

    i += 1
