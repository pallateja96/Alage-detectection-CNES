import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
colors = np.array([[0, 191, 255],  # blue water
                   [0, 255, 0],  # green algae 1st class
                   [51, 153, 51],  # green algae 2nd class
                   [255, 255, 0],  # yellow algae 3rd class
                   [255, 153, 0],  # orange algae 4th class
                   [255, 51, 0],  # red algae 5th class
                   [204, 0, 204],  # purple saturated pixel
                   [0, 0, 102],  # black blue borders
                   [153, 102, 51],  # brown land
                   [255, 255, 255],  # white clouds
                   [102, 102, 51],  # browngreen mixed class
                   [128, 128, 128]  # gray no data
                   ]) / 255

# Define the class labels
class_labels = ['Water', 'Algae_1', 'Algae_2', 'Algae_3', 'Algae_4',
                'Algae_5', 'Saturated_pixel', 'Borders', 'Land', 'Cloud', 'Mixed', 'No_data']

# Load the one-hot encoded mask from the binary file
one_hot_mask = np.load(
    "Dataset/WesternLake/encodedmask/mask_36.npy", allow_pickle=True)


cmap = colors[one_hot_mask.argmax(axis=-1)]

# Display the one-hot encoded image
plt.imshow(cmap)
# Create the legend

# Create a legend

plt.legend(class_labels)

plt.show()
