# Machine Vision Manufacturing Demo
**Author:** Manisha Das Chaity  
**Focus:** Machine Vision • Optical Metrology • Manufacturing Inspection

This repository demonstrates a complete machine vision pipeline for
manufacturing inspection and metrology, aligned with industrial use cases
such as surface defect detection, dimensional measurement, and quality control.

The project mirrors real-world workflows used in manufacturing environments,
including image acquisition, preprocessing, segmentation, defect detection,
measurement calibration, and machine learning-based classification.

## Key Capabilities
- Image preprocessing and noise reduction
- Defect detection using classical computer vision
- Pixel-to-physical dimensional measurement (metrology)
- Feature extraction and ML-based defect classification
- CNN-based defect classification (proof-of-concept)
- Statistical analysis for measurement repeatability

## Project Structure

```
machine-vision-manufacturing-demo/
│
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
│
├── data/
│   ├── raw/
│   │   └── glass_sample.png          # Sample image for testing
│   └── processed/                     # Output directory for processed images
│
├── src/
│   ├── acquisition.py                 # Image acquisition module
│   ├── preprocessing.py               # Image preprocessing and filtering
│   ├── segmentation.py                # Image segmentation logic
│   ├── defect_detection.py            # Defect detection algorithms
│   ├── metrology.py                   # Measurement and calibration
│   ├── feature_extraction.py          # Feature engineering for ML
│   ├── ml_classification.py           # ML-based classification
│   └── utils.py                       # Utility functions
│
├── notebooks/
│   └── exploratory_analysis.ipynb    # Jupyter notebook for exploration
│
├── models/
│   └── cnn_defect_classifier.py      # CNN model implementation
│
└── docs/
    └── system_overview.md             # System architecture and design
```

## Technologies
- Python
- OpenCV
- NumPy
- scikit-learn
- TensorFlow / Keras

## Applications
- Glass and surface inspection
- Manufacturing quality control
- Machine vision metrology
- Production inspection systems

This project is intended as a demonstration of engineering approaches
rather than a production-ready system.
