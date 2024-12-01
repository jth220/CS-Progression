#Image Operations are all done in this module

import cv2



import cv2
import numpy as np

def rotate_image(current_image, angle):
    """
    Rotate an image by a specified angle without cropping.

    :param current_image: Input image (numpy array).
    :param angle: Rotation angle in degrees (positive for counter-clockwise).
    :return: Rotated image with adjusted dimensions.
    """
    # Get the dimensions of the image
    (height, width) = current_image.shape[:2]

    # Calculate the center of the image
    center = (width // 2, height // 2)

    # Get the rotation matrix for the given angle
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Calculate the new bounding dimensions of the image
    abs_cos = abs(rotation_matrix[0, 0])  # Cosine of the rotation angle
    abs_sin = abs(rotation_matrix[0, 1])  # Sine of the rotation angle

    # Compute the new width and height of the rotated image
    new_width = int((height * abs_sin) + (width * abs_cos))
    new_height = int((height * abs_cos) + (width * abs_sin))

    # Adjust the rotation matrix to account for translation
    rotation_matrix[0, 2] += (new_width / 2) - center[0]
    rotation_matrix[1, 2] += (new_height / 2) - center[1]

    # Perform the rotation with the new dimensions
    rotated_image = cv2.warpAffine(current_image, rotation_matrix, (new_width, new_height))

    return rotated_image


def flip_image(current_image, flip_code):
    """
    Flip an image horizontally, vertically, or both.

    :param image: Input image (numpy array).
    :param flip_code: Flip axis (0 for vertical, 1 for horizontal, -1 for both).
    :return: Flipped image.
    """

    flipped_image = cv2.flip(current_image, flip_code)
    return flipped_image




def resize_image(current_image, width=None, height=None, interpolation=cv2.INTER_LINEAR):
    """
    Resize an image to the specified width and/or height.

    :param image: Input image (numpy array).
    :param width: Desired width (optional).
    :param height: Desired height (optional).
    :param interpolation: Interpolation method for resizing (default: cv2.INTER_LINEAR).
    :return: Resized image.
    """
    # Original dimensions
    (original_height, original_width) = current_image.shape[:2]

    # If no dimensions are provided, return the original image
    if not width and not height:
        return current_image

    # Calculate aspect ratio and dimensions if one is missing
    if width and not height:
        # Scale height to maintain aspect ratio
        height = int((width / original_width) * original_height)
    elif height and not width:
        # Scale width to maintain aspect ratio
        width = int((height / original_height) * original_width)

    resized_image = cv2.resize(current_image, (width, height), interpolation)
    # Resize the image
    return resized_image