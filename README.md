<h1 align="center">
  :black_circle: Handwritten Digit Recognition :black_circle:
</h1>

### 📚 Project Overview
This Python project 🐍 implements a ***Handwritten Digit Recognition Application*** using a ***Convolutional Neural Network (CNN)*** built with ***Keras***. The application allows users to draw digits on a canvas ✍️, which are then recognized by the trained model 🤖✨. The model is trained on ***the MNIST dataset***, which contains images of handwritten digits 🧑‍🎨

### 🌟 Key Highlights

-   **User -Friendly Interface:** Draw digits easily on a digital canvas 🎨🖥️.
-   **Real-Time Recognition:** Instantly recognize the drawn digit with high accuracy ⚡🔍.
-   **Interactive Experience:** Engage with the application and see your drawings come to life! 🎉👩‍🎤

### ✨ Features

-   Draw digits on a canvas 🖌️🎨.
-   Recognize the drawn digit using a pre-trained CNN model 🧠🔍.
-   Display the predicted digit and confidence percentage 📊📈.
-   Clear the canvas with a button 🧹🔄.

## 📸 Screenshots
This section showcases key moments of the handwritten digit recognition application in action. Each screenshot highlights a specific feature of the application, providing a visual representation of its functionality. 🌟

### 1\. Application Launch 🚀

*Description*: This screenshot captures the initial state of the application, featuring the logo and user instructions. It provides users with a clear understanding of how to interact with the application upon launch. 🖥️✨

![Application Launch](https://github.com/user-attachments/assets/e91f5809-91f6-498c-878a-f9fc4f7990a5)

### 2\. Drawing on Canvas 🎨

*Description*: This screenshot illustrates a user actively drawing a digit on the canvas. It demonstrates the intuitive interface that allows for seamless user interaction, showcasing the application's capability to capture handwritten input. ✍️🖌️

![Drawing on Canvas](https://github.com/user-attachments/assets/99787db9-be8d-4511-ad1a-22d232201fd6)

### 3\. Prediction Result ✅

*Description*: This screenshot displays the outcome after the user clicks the "Recognize" button. It shows the predicted digit along with the confidence percentage, highlighting the model's performance and accuracy in recognizing handwritten digits. 📊🤖

![Prediction Result](https://github.com/user-attachments/assets/6ded250a-a727-4381-bf3f-f8321c3a0778)

## Getting Started 🚀
To get your project up and running, follow these steps:

### Prerequisites
Make sure you have Python installed on your machine. You will also need to install the required packages listed in `requirements.txt`.

### Installation 🛠️

#### 1\. Clone the Repository 📥
Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/MohammadAshmir786/Handwritten_Digit_Recognition.git
   ```

#### 2\. Navigate to the Project Directory 📂
Change into the project directory:
  ```bash
  cd Handwritten_Digit_Recognition
  ```

#### 3\. Install Dependencies 📦
Make sure you have all the required packages installed. Run the following command to install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```

#### 4\. Run the Application 🖥️
Start the application by executing:
  ```bash
  python digit_recognition_app.py
  ```

#### 5\. Draw and Recognize ✍️🔍
-   Draw a digit on the canvas.
-   Click the "Recognize" button to see the prediction!
-   Use the "Clear" button to clear the canvas and Draw again.

> [!IMPORTANT]
> Before running the training model or the recognition application, replace the placeholder **`"absolute path to the saved model"`** in the code with the actual absolute path to your saved model 🛠️🔑.

## Model Training 🏆
The model is trained on the MNIST dataset. The training process involves the following steps:

1.  Load the MNIST dataset.
2.  Preprocess the images (normalize and reshape).
3.  Build the CNN model.
4.  Compile and train the model using callbacks for early stopping and model checkpointing.
5.  Save the best model as `best_model.keras`.

### Model Architecture 📝
The CNN model consists of:

-   Two convolutional layers followed by max pooling layers.
-   A flattening layer.
-   A dense layer with dropout for regularization.
-   An output layer with softmax activation for multi-class classification.

## Contributing 🤝
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License 📄
This project is licensed under the MIT License. See the [LICENSE](https://github.com/MohammadAshmir786/Handwritten_Digit_Recognition/blob/f8ec66381499f827e9a0815b3ec250777d2930da/LICENSE) file for details.

## Acknowledgments 🙏
-   [Keras](https://keras.io/)for the deep learning framework.
-   [MNIST Dataset](https://keras.io/api/datasets/mnist/) for providing the handwritten digit dataset.

## Contact 📬
For any inquiries or feedback, feel free to reach out to me at [<kbd>mail ↗️</kbd>](moashmir7003@gmail.com).


* * *


Thank you for exploring this project! Enjoy recognizing your handwritten digits! 🎉
