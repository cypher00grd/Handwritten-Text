import streamlit as st
import pandas as pd
import io
import os
from google.cloud import vision
import re
from word2number import w2n
from camera import take_photo
os.environ["Collab_easyOCR"] = "key.json"
client = vision.ImageAnnotatorClient()
def extract_text_from_image(image):
    content = image.read()
    image = vision.Image(content=content)


    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return None

    return texts[0].description

def extract_text_from_image1(image):


    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='JPEG')
    content = img_byte_array.getvalue()

    image = vision.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return None

    return texts[0].description

def extract_details(text):

    roll_match = re.search(r"in words\)\s*([\w\s$\.]+)", text)
    if roll_match:
        roll_number = roll_match.group(1).replace(".", "").strip()
        roll_number = re.split(r"\d+|course|Course", roll_number, 1)[0].strip()
    else:
        roll_number = "Not Found"

    try:
        roll_number_digits = w2n.word_to_num(roll_number)
    except:
        roll_number_digits = "NIL"


    total_match = re.search(r"TOTAL\s+(\d+)", text)
    total_marks = total_match.group(1) if total_match else "Not Found"

    return roll_number, roll_number_digits, total_marks


def save_to_excel(roll_number, marks):

    file_path = "marks.xlsx"


    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Roll Number", "Marks"])

    new_entry = pd.DataFrame({"Roll Number": [roll_number], "Marks": [marks]})
    df = pd.concat([df, new_entry], ignore_index=True)


    df.to_excel(file_path, index=False)


st.title(" Automated Roll Number & Marks Recognition & Updation")
st.write("Upload an image or take a photo to extract the roll number and marks")


if st.button("Take Photo"):
    image = take_photo()
    if image:
        st.image(image, caption="Captured Photo", use_container_width=True)


        extracted_text = extract_text_from_image1(image)

        if extracted_text:

            roll_number, roll_number_digits, marks = extract_details(extracted_text)


            st.success(f" **Roll Number (Text):** {roll_number}")
            st.success(f" **Roll Number (Digits):** {roll_number_digits}")
            st.success(f" **Total Marks:** {marks}")


            if st.button(" Save to Excel"):
                save_to_excel(roll_number_digits, marks)
                st.success(" Data saved to marks.xlsx!")
        else:
            st.error(" No text found in image. Please try again.")


uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)


    extracted_text = extract_text_from_image(uploaded_file)

    if extracted_text:

        roll_number, roll_number_digits, marks = extract_details(extracted_text)


        st.success(f" **Roll Number (Text):** {roll_number}")
        st.success(f" **Roll Number (Digits):** {roll_number_digits}")
        st.success(f" **Total Marks:** {marks}")

        if st.button(" Save to Excel"):
            save_to_excel(roll_number_digits, marks)
            st.success(" Data saved to marks.xlsx!")

    else:
        st.error(" No text found in image. Please try again.")
