import cv2
import numpy as np

def segment(image):
    """
    Adaptive thresholding for uneven illumination.
    """
    binary = cv2.adaptiveThreshold(
        image, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2
    )

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    clean = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    return clean
