import cv2
import numpy as np
from pdf2image import convert_from_path
import os

pdf_path = r'./Donnie-Creek-EvacOrder5_Map_20230530.pdf'
def pdf_to_image():
    print("------------------")
    current_directory = os.getcwd()
    print(current_directory)
    print("------------------")
    print(os.sys.path)


    # Convert the PDF to a list of imagess
    images = convert_from_path(pdf_path, dpi=300)  # Adjust dpi as needed

    # Save the first image (assuming it's a single-page PDF)
    #/images[0].save(output_path, 'JPEG')
    cv2.imshow(images[0])

def extract_boundary():
    pdf_url = r'C:\Users\krtzx\PycharmProjects\pythonProjects\Projects\Donnie-Creek-EvacOrder5_Map_20230530.pdf'

    # Convert the PDF to images
    images = convert_from_path(pdf_url, dpi=300)

    # Load the first page of the PDF as an image
    image = np.array(images[0])

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow(gray)

    # # Apply Gaussian blur to reduce noise (optional)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    #
    # # Apply Canny edge detection
    # edges = cv2.Canny(blurred, 50, 150)  # Adjust the thresholds as needed
    #
    # # Find contours in the edge image
    # contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    # # Find the largest contour
    # largest_contour = max(contours, key=cv2.contourArea)
    #
    # # Create an empty mask image
    # mask = np.zeros_like(image)
    #
    # # Draw the largest contour on the mask
    # cv2.drawContours(mask, [largest_contour], 0, (255, 255, 255), thickness=cv2.FILLED)
    #
    # # Apply the mask to the original image
    # boundary = cv2.bitwise_and(image, mask)
    #
    # # Save the extracted boundary image
    # cv2.imwrite(output_path, boundary)

    print('Boundary image extracted successfully!')

"""
//pdf_url = 'https://prrd.bc.ca/wp-content/uploads/post/donnie-creek-tommy-lakes-evacuation-order-5/Donnie-Creek-Evac-Order-5-May-30-2023.pdf'
"""
# pdf_url = 'C:\Users\krtzx\PycharmProjects\pythonProjects\Projects\Donnie-Creek-EvacOrder5_Map_20230530.pdf'
# output_path = './output/boundary.jpg'

#extract_boundary(pdf_url, output_path)
pdf_to_image()