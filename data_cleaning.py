import glob
import os
import fnmatch
import re

parent_folder_path = 'Dataset'

# Get a list of all subfolders in the parent folder
#subfolders = [f.path for f in os.scandir(parent_folder_path) if f.is_dir()]

# folder = "Dataset/WesternLake"

# for filename in os.listdir(folder):
#     if filename.endswith("CI-CIcyano.tif"):
#         os.remove(os.path.join(folder, filename))
#         print(f"{filename} removed from {folder}.")


image_folder = "Dataset/WesternLake/image/"
mask_folder = "Dataset/WesternLake/mask"

images = os.listdir(image_folder)
masks = os.listdir(mask_folder)

for mask in masks:
    found = False
    for repmask in masks:
        if re.search(mask[0:28], repmask) != None:
            found = True
            break
    if found == False:
        print(mask)
