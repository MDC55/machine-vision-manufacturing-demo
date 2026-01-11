import cv2

def acquire_image(path: str):
    """
    Simulates image acquisition from an industrial camera.
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError("Image not found")
    return image
