import cv2
import os

class ImageHistory:
    """
    A class to manage undo/redo functionality.
    """
    def __init__(self):
        self.undo_stack = []  # Stack to store previous states
        self.redo_stack = []  # Stack to store reverted states

    def save_state(self, image):
        """
        Save the current state of the image for undo functionality.
        :param image: Current image (numpy array).
        """
        self.undo_stack.append(image.copy())
        self.redo_stack.clear()  # Clear redo stack on new action

    def undo(self):
        """
        Undo the last action, if possible.
        :return: The previous image state (numpy array) or None if stack is empty.
        """
        if self.undo_stack:
            self.redo_stack.append(self.undo_stack.pop())
            return self.undo_stack[-1] if self.undo_stack else None
        return None

    def redo(self):
        """
        Redo the last undone action, if possible.
        :return: The reverted image state (numpy array) or None if stack is empty.
        """
        if self.redo_stack:
            state = self.redo_stack.pop()
            self.undo_stack.append(state)
            return state
        return None

# Utility functions
def load_image(file_path):
    """
    Load an image from the given file path.
    :param file_path: Path to the image file.
    :return: Loaded image (numpy array) or None if loading fails.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return cv2.imread(file_path)

def save_image(image, file_path):
    """
    Save the given image to the specified file path.
    :param image: Image (numpy array) to save.
    :param file_path: Path to save the image file.
    """
    cv2.imwrite(file_path, image)

def is_valid_image(file_path):
    """
    Validate if the file is a valid image.
    :param file_path: Path to the file.
    :return: True if the file is a valid image, otherwise False.
    """
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    return os.path.splitext(file_path)[1].lower() in valid_extensions

def has_unsaved_changes(original_image, current_image):
    """
    Check if there are unsaved changes between the original and current images.
    :param original_image: The original image (numpy array).
    :param current_image: The current image (numpy array).
    :return: True if there are unsaved changes, otherwise False.
    """
    return not (original_image.shape == current_image.shape and (original_image == current_image).all())
