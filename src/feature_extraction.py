from skimage.feature import local_binary_pattern
import numpy as np

def extract_texture_features(image):
    lbp = local_binary_pattern(image, P=8, R=1)
    return np.histogram(lbp, bins=256)[0]
