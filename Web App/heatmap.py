import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def generate_heatmap(coords, image_shape, output_path):
    heatmap = np.zeros((image_shape[0], image_shape[1]))

    for (x1, y1, x2, y2) in coords:
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
        if 0 <= cy < heatmap.shape[0] and 0 <= cx < heatmap.shape[1]:
            heatmap[cy, cx] += 1

    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap, cmap='inferno', cbar=True)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()