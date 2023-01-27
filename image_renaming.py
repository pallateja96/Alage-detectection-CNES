import os

# Define the path to the images
image_path = 'Dataset/WesternLake/mask'

# Get the list of images in the folder
image_list = os.listdir(image_path)

# Loop through the images
for image in image_list:
    # Extract the new base name of the image (keep just the first 28 characters)
    base_name = image[:28]
    # Define the new name for the image
    new_image_name = f'{base_name}_mask.tif'
    # Define the full paths for the old and new images
    old_image_path = os.path.join(image_path, image)
    new_image_path = os.path.join(image_path, new_image_name)
    # Rename the image
    os.rename(old_image_path, new_image_path)
