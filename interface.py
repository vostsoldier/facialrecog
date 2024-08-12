import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
import cv2

class CameraApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Camera Interface")
        
        # Create a label to display the video feed
        self.video_label = tk.Label(window)
        self.video_label.pack()

        # Button to capture image
        self.capture_button = Button(window, text="Capture", command=self.capture_image)
        self.capture_button.pack()

        # Initialize the camera
        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the image to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        # Schedule the next frame update
        self.window.after(10, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite('/home/pi/Desktop/captured_image.jpg', frame)

    def __del__(self):
        self.cap.release()

# Create the GUI window
root = tk.Tk()
app = CameraApp(root)
root.mainloop()
