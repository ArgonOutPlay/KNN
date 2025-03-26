import os
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from PIL import Image

image_folders = ['train/train_image', 'train/test/ICDAR24-WordArt_testA/test_image', 'train/test/ICDAR24-WordArt_testB/test_image']
resolutions = []

# projde vsechny zadane slozky a da to do resolution (vysku a sirku)
for image_folder in image_folders:
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            img_path = os.path.join(image_folder, filename)
            with Image.open(img_path) as img:
                resolutions.append((img.size[0], img.size[1]))

# prevod na np pole
resolutions = np.array(resolutions)
widths, heights = resolutions[:, 0], resolutions[:, 1]

# odstraneni outlieru
def remove_outliers(data_x, data_y, lower_percentile=5, upper_percentile=95):
    x_low, x_high = np.percentile(data_x, [lower_percentile, upper_percentile])
    y_low, y_high = np.percentile(data_y, [lower_percentile, upper_percentile])
    mask = (data_x >= x_low) & (data_x <= x_high) & (data_y >= y_low) & (data_y <= y_high)
    return data_x[mask], data_y[mask]

# odstraneni outliers
widths, heights = remove_outliers(widths, heights)

# graf s binovanim
plt.figure(figsize=(12, 6))
plt.hist2d(widths, heights, bins=[20, 20], cmap='Blues')
plt.colorbar(label='Počet obrázků')
plt.xlabel('Šířka obrázku')
plt.ylabel('Výška obrázku')
plt.title('Graf zobrazující rozlišení obrázků (bez outlierů)')
plt.show()