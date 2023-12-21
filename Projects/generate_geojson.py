import os
from pdf2image import convert_from_path
import cv2
import numpy as np
import json

def generate_geojson(pdf_path, output_path):
    # Convert the PDF to an image
    images = convert_from_path(pdf_path, dpi=300)  # Adjust dpi if needed
    image = images[0]  # Assuming the map is on the first page

    # Convert the image to a NumPy array
    image_np = np.array(image)

    # Perform image processing to identify the map boundaries and generate the GeoJSON
    # ...
    image_cv = cv2.imread(image)
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise (optional)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold1, threshold2)
    # Write the generated GeoJSON to a file
    with open(output_path, 'w') as f:
        json.dump(geojson, f, indent=2)
    print('Map GeoJSON file created successfully!')

"""
pdf_path = './data/Donnie-Creek-EvacOrder5_Map_20230530.pdf'
output_path = './output/map.geojson'

generate_geojson(pdf_path, output_path)
"""
pdf_path = './data/Donnie-Creek-EvacOrder5_Map_20230530.pdf'
output_path = './output/map.geojson'

generate_geojson(pdf_path, output_path)