import cv2

def detect_defects(binary_image, min_area=100):
    """
    Blob analysis for defect detection.
    """
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image)

    defects = []
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area >= min_area:
            defects.append(stats[i])

    return defects
