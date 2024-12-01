import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from utils import load_image, save_image, ImageHistory
from image_operations import rotate_image, resize_image, flip_image


class ImageEditorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")
        self.original_image = None


        # Image variables
        self.current_image = None
        self.image_history = ImageHistory()

        # Set up UI components
        self.setup_ui()

    def setup_ui(self):
        # Canvas to display the image
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="gray")
        self.canvas.pack()

        # Frame for buttons and slider
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(fill=tk.X)

        # Buttons
        tk.Button(controls_frame, text="Open", command=self.open_image).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(controls_frame, text="Save", command=self.save_image).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(controls_frame, text="Flip Horizontal", command=self.flip_horizontal).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(controls_frame, text="Undo", command=self.undo).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(controls_frame, text="Redo", command=self.redo).pack(side=tk.LEFT, padx=5, pady=5)

        # Rotation Slider
        tk.Label(controls_frame, text="Rotation Angle:").pack(side=tk.LEFT, padx=5)
        self.rotation_slider = tk.Scale(
            controls_frame, from_=-180, to=180, orient=tk.HORIZONTAL, command=self.rotate_with_slider
        )
        self.rotation_slider.pack(side=tk.LEFT, padx=5, pady=5)

        # Resize Button
        tk.Button(controls_frame, text="Resize", command=self.resize_image).pack(side=tk.LEFT, padx=5, pady=5)

    def open_image(self):
     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
     if file_path:
        self.original_image = load_image(file_path)  # Store the original image
        self.current_image = self.original_image.copy()  # Work with a copy
        self.image_history.save_state(self.current_image)
        self.display_image_on_canvas()


    def save_image(self):
        if self.current_image is None:
            messagebox.showerror("Error", "No image to save.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if file_path:
            save_image(self.current_image, file_path)
            messagebox.showinfo("Success", "Image saved successfully.")

    def rotate_with_slider(self, value):
        if self.original_image is not None:
         angle = int(value)  # Get the slider value as an integer
         self.current_image = rotate_image(self.original_image, angle)  # Rotate the original image
         self.display_image_on_canvas()


    def flip_horizontal(self):
        if self.current_image is not None:
            self.image_history.save_state(self.current_image)
            self.current_image = flip_image(self.current_image, flip_code=1)
            self.display_image_on_canvas()

    def resize_image(self):
        if self.current_image is not None:
            # Ask the user for new width and height
            new_width = simpledialog.askinteger("Resize", "Enter new width:")
            new_height = simpledialog.askinteger("Resize", "Enter new height:")

            if new_width and new_height:
                self.image_history.save_state(self.current_image)
                self.current_image = resize_image(self.current_image, width=new_width, height=new_height)
                self.display_image_on_canvas()
            else:
                messagebox.showwarning("Resize", "Invalid dimensions entered.")

    def undo(self):
        previous_image = self.image_history.undo()
        if previous_image is not None:
            self.current_image = previous_image
            self.display_image_on_canvas()
        else:
            messagebox.showinfo("Info", "No more actions to undo.")

    def redo(self):
        next_image = self.image_history.redo()
        if next_image is not None:
            self.current_image = next_image
            self.display_image_on_canvas()
        else:
            messagebox.showinfo("Info", "No more actions to redo.")

    def display_image_on_canvas(self):
        if self.current_image is not None:
            rgb_image = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB)
            resized_image = cv2.resize(rgb_image, (800, 600))
            self.tk_image = tk.PhotoImage(data=cv2.imencode('.png', resized_image)[1].tobytes())
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorGUI(root)
    root.mainloop()
