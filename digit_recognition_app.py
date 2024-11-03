import tkinter as tk
import numpy as np
from keras.models import load_model
from PIL import Image, ImageTk, ImageGrab
import PIL.ImageOps

# Define the main directory for assets and model
# replace (absolute path to the saved model) with the path to your saved model
main_dir = "absolute path to the saved model"

# Initialize the main application window
master = tk.Tk()
master.configure(background="white")
master.title("Handwritten Digit Recognition")
master.geometry("960x540")
master.iconbitmap(f"{main_dir}//assets//favicon.ico")
master.resizable(0, 0)

# Load the pre-trained model for digit recognition
model = load_model(f"{main_dir}//best_model.keras")

# Load and resize the logo image for display
image_path = f"{main_dir}//assets//logo.png"
logo_file = Image.open(image_path)
logo_file = logo_file.resize((311, 283), Image.LANCZOS)
wp_img = ImageTk.PhotoImage(logo_file)

# Create a Label to display the logo image
logo = tk.Label(master, image=wp_img, bg="white")
logo.place(x=20, y=20)


# Function to destroy a widget
def destroy_widget(widget):
    widget.destroy()


# Function to predict the digit drawn on the canvas
def predict_digit():
    global predicted_num_label, accuracy_label

    # Capture the canvas area as an image
    x = master.winfo_rootx() + canvas.winfo_x()
    y = master.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Grab the image from the canvas and convert to grayscale
    im1 = ImageGrab.grab(bbox=(x, y, x1, y1))
    im1 = im1.convert("L")  # Convert to grayscale

    # Resize the image to match the input size of the model
    im1 = im1.resize((28, 28))

    # Invert the color of image for better output result
    im1 = PIL.ImageOps.invert(im1)

    # Convert the image to a NumPy array and preprocess it
    img = np.array(im1)
    img = img.reshape(1, 28, 28, 1)  # Reshape for model input
    img = img / 255.0  # Normalize pixel values to [0, 1]

    # Predict the digit using the model
    res = model.predict(img)[0]
    pred = np.argmax(res)  # Get the predicted digit
    acc = max(res)  # Get the prediction confidence
    acc_percent = round(acc * 100)

    # Display the predicted digit and accuracy
    predicted_num_label = tk.Label(
        master,
        text="The number is: " + str(pred),
        width=25,
        height=2,
        fg="white",
        bg="#4584b6",
        font=("times", 16, "bold"),
    )
    predicted_num_label.place(x=30, y=410)

    accuracy_label = tk.Label(
        master,
        text="The precision is: " + str(acc_percent) + "%",
        width=25,
        height=2,
        fg="black",
        bg="#ffde57",
        font=("times", 16, "bold"),
    )
    accuracy_label.place(x=30, y=460)


# Function to draw on the canvas
def draw_digit(event):
    x = event.x
    y = event.y
    r = 12  # Radius of the brush
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")  # Draw a circle
    predict_btn.configure(state=tk.NORMAL, bg="#4584b6")  # Enable the predict button


# Function to clear the canvas and reset the prediction
def clear_digit():
    predict_btn.configure(state=tk.DISABLED, bg="#B2CDE2")  # Disable the predict button
    canvas.delete("all")  # Clear the canvas
    try:
        predicted_num_label.destroy()  # Remove prediction label
        accuracy_label.destroy()  # Remove accuracy label
    except:
        pass


# Button to trigger digit recognition
predict_btn = tk.Button(
    master,
    text="Recognize",
    state=tk.DISABLED,
    command=predict_digit,
    width=15,
    borderwidth=0,
    bg="#B2CDE2",
    fg="white",
    font=("times", 18, "bold"),
)
predict_btn.place(x=60, y=305)

# Button to clear the canvas
clr_btn = tk.Button(
    master,
    text="CLEAR",
    width=15,
    borderwidth=0,
    command=clear_digit,
    bg="#ffde57",
    fg="black",
    font=("times", 18, "bold"),
)
clr_btn.place(x=60, y=355)

# Create a canvas for drawing
canvas = tk.Canvas(
    master,
    width=550,
    height=450,
    highlightthickness=1,
    highlightbackground="#4584b6",
    cursor="pencil",
)
canvas.place(x=380, y=60)
canvas.bind("<B1-Motion>", draw_digit)  # Bind drawing to left mouse button

# Label to display instructions
legend = tk.Label(
    master,
    text="Write a number",
    width=18,
    height=1,
    fg="white",
    bg="#4584b6",
    font=("times", 16, "bold"),
)
legend.place(x=550, y=30)

# Start the main application loop
master.mainloop()
