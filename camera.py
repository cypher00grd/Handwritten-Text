import cv2
import streamlit as st
import numpy as np
from PIL import Image

def take_photo():

    st.write(" **Turn on your camera and capture an image.**")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error(" Unable to access the camera. Please check your webcam permissions.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error(" Failed to capture image. Try again.")
        return None

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame)

    return image
