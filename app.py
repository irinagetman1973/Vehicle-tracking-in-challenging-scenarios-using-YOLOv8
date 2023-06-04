# Importing the necessary libraries

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Adding an appropriate title for the test website
st.title("Welcome")
# Creating a side bar radio option for selecting the required elements
_radio = st.sidebar.radio("",
                          ("Load Data", "Run the Model","Model's Evaluation Report"))

if _radio == "Load Data":
     # Creating a header in the fundamentals section
    st.header("Track with Confidence, Powered by YOLOv8!")

    # Loading the model
    # model_path = "model_test.h5"
    # model = load_model(model_path, compile = False)
    
    # Uploading an image
    img_data = st.file_uploader(label="Image", accept_multiple_files=True)

    # Making the required prediction
    if img_data is not None and len(img_data) > 0:
        # Assigning a random count
        count = 0

        # Opening and displaying the image
        img = Image.open(img_data[count]) 
        st.image(img)

        # Converting into a numpy array
        img = np.array(img)
        img = np.expand_dims(img, 0)

        # Making the appropriate prediction
        # prediction = model.predict(img)
        # output = np.argmax(prediction)

        # Displaying the prediction
        st.write("The Predicted Result is: ", output)
        print(output)

    # While no image is uploaded
    else:
        st.write("Waiting For Upload of Image...")      
elif _radio == "Run the Model":
    # Creating a header in the fundamentals section
    st.header("Track with Confidence, Powered by YOLOv8!")

  