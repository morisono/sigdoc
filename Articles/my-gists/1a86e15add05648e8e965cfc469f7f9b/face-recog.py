import cv2
import numpy as np
import gradio as gr
from imgbeddings import imgbeddings
from PIL import Image
import psycopg2
import os

# Function to calculate face match rate using image embeddings
def face_match_rate(image1, image2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Detect faces in images
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    faces2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if faces are detected
    if len(faces1) == 0 or len(faces2) == 0:
        return 0.0

    # Extract embeddings for the first image
    embeddings1 = imgbeddings(Image.fromarray(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)))

    # Extract embeddings for the second image
    embeddings2 = imgbeddings(Image.fromarray(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)))

    # Calculate cosine similarity between the embeddings
    similarity = np.dot(embeddings1, embeddings2) / (np.linalg.norm(embeddings1) * np.linalg.norm(embeddings2))

    return similarity

# Function to save embeddings to PostgreSQL database
def save_embeddings_to_db(image, embeddings):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect("<YOUR_CONNECTION_STRING>")
        cursor = conn.cursor()

        # Insert image and embeddings into the database
        cursor.execute("INSERT INTO image_embeddings (image, embeddings) VALUES (%s, %s)", (image, embeddings))
        conn.commit()

        # Close database connection
        cursor.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

# Function to process uploaded images and display match rate
def process_images(image1, image2):
    # Calculate face match rate
    match_rate = face_match_rate(image1, image2)

    # Save embeddings of the first image to the database
    # Convert embeddings to string for saving to database (assuming embeddings is a numpy array)
    embeddings_str = ','.join(map(str, embeddings1))
    save_embeddings_to_db(image1, embeddings_str)

    # Display match rate
    return f"Match rate: {match_rate:.2f}"

# Create Gradio UI
face_recognition_ui = gr.Interface(
    fn=process_images,
    inputs=["image", "image"],
    outputs="text",
    title="Face Recognition",
    description="Upload two images to compare them and see the match rate.",
    capture_session=True
)

# Launch the UI
face_recognition_ui.launch()
