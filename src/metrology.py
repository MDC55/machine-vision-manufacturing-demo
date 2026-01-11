MM_PER_PIXEL = 0.02  # calibration factor

def measure_defects(defects):
    """
    Convert pixel measurements to physical units.
    """
    measurements = []
    for d in defects:
        width_mm = d[2] * MM_PER_PIXEL
        height_mm = d[3] * MM_PER_PIXEL
        measurements.append((width_mm, height_mm))
    return measurements
