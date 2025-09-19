import face_recognition
import os
import cv2


def load_known_faces(known_faces_dir):
    """
    Loads known faces from a directory and creates a dictionary of face encodings.
    Each subdirectory is considered a person's name.

    Args:
        known_faces_dir (str): Path to the directory containing subdirectories of known faces.

    Returns:
        tuple: A tuple containing the list of known face encodings and their corresponding names.
    """
    known_face_encodings = []
    known_face_names = []

    print("Loading known faces...")
    for name in os.listdir(known_faces_dir):
        person_dir = os.path.join(known_faces_dir, name)
        if os.path.isdir(person_dir):
            for filename in os.listdir(person_dir):
                if filename.endswith(('.jpg', '.png', '.jpeg')):
                    image_path = os.path.join(person_dir, filename)
                    try:
                        image = face_recognition.load_image_file(image_path)
                        face_encoding = face_recognition.face_encodings(image)[0]
                        known_face_encodings.append(face_encoding)
                        known_face_names.append(name)
                        print(f"  Loaded encoding for {name} from {filename}")
                    except IndexError:
                        print(f"  Warning: No face found in {filename} for {name}")
    print("Known faces loaded successfully.")
    return known_face_encodings, known_face_names


def classify_faces_in_photo(photo_path, known_face_encodings, known_face_names):
    """
    Detects faces in a photo, compares them to known faces, and draws a box and label.

    Args:
        photo_path (str): Path to the photo to be classified.
        known_face_encodings (list): A list of face encodings for known people.
        known_face_names (list): A list of names corresponding to the known face encodings.
    """
    print(f"\nProcessing photo: {photo_path}")

    # Load the image and convert it from BGR to RGB (OpenCV uses BGR by default)
    image = cv2.imread(photo_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Find all face locations and face encodings in the current photo
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Compare the face with all known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the first matching person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Draw boxes and labels on the image
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up the face locations
        top *= 1
        right *= 1
        bottom *= 1
        left *= 1

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        print(f"  Found face: {name}")

    # Display the resulting image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    """
    Main function to run the face classification process.
    """
    # Define the directory for known faces and the photo to test
    known_faces_dir = "known_faces"
    photo_to_classify = "test_photo.jpg"

    # Check if the known faces directory and test photo exist
    if not os.path.exists(known_faces_dir):
        print(f"Error: The directory '{known_faces_dir}' does not exist.")
        print("Please create this directory and add subdirectories with images of people.")
        print("Example: known_faces/Barack_Obama/obama1.jpg")
        return

    if not os.path.exists(photo_to_classify):
        print(f"Error: The file '{photo_to_classify}' does not exist.")
        print("Please place a photo you want to classify in the same directory.")
        return

    # Load known faces and then classify the test photo
    known_face_encodings, known_face_names = load_known_faces(known_faces_dir)
    classify_faces_in_photo(photo_to_classify, known_face_encodings, known_face_names)


if __name__ == "__main__":
    main()
