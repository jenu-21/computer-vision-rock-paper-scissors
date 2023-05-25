import cv2
import random
from keras.models import load_model as keras_load_model
import numpy as np 
import time

def get_computer_choice():
     choices = ["Rock", "Scissors", "Paper"]
     return random.choice(choices)
  
    
def load_trained_model():
    model = keras_load_model('keras_model.h5')
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy')
    return model

def preprocess_image(image):
    resized_image = cv2.resize(image, (224, 224), interpolation = cv2.INTER_AREA)
    normalized_image = (resized_image.astype(np.float32) / 127.0) - 1
    return normalized_image

def get_prediction(image, model):
    
    normalized_image = preprocess_image(image)

    data = np.ndarray(shape=(1, 224, 224, 3), dtype = np.float32)
    data[0] = normalized_image

    prediction = model.predict(data)
    choices = ["Rock", "Scissors", "Paper", "Nothing"]
    index = np.argmax(prediction)
    response = choices[index]
    return response

def play():
    model = load_trained_model()
    cap = cv2.VideoCapture(0)

    countdown_duration = 3
    countdown_start_time = time.time()

    computer_wins = 0
    user_wins = 0

    while computer_wins < 3 and user_wins < 3: 
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        elapsed_time = time.time() - countdown_start_time
        if elapsed_time >= countdown_duration:
            prediction = get_prediction(frame, model)
            computer_choice = get_computer_choice()
            print("User chooses:", prediction)
            print("Computer chooses:", computer_choice)
            
            if prediction == "Nothing":
                print("Computer wins by default!")
                computer_wins += 1
            elif computer_choice == prediction:
                print("It's a tie!")
            elif(
                (computer_choice == "Rock" and prediction == "Scissors") or
                (computer_choice == "Scissors" and prediction == "Paper") or
                (computer_choice == "Paper" and prediction == "Rock")
            ):
                print("Computer wins!")
                computer_wins += 1
            else:
                print("User wins!")
                user_wins += 1

            countdown_start_time = time.time()        
            
                    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

play()


