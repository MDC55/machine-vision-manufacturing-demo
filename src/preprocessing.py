import cv2

def preprocess(image):
    """
    Noise reduction and contrast normalization.
    """
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred
