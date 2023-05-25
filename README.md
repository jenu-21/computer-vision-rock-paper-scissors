# Computer Vision RPS

##  Create the computer vision system 
Using teachable-machine we created an image model using the webcam for rock, paper, scissors and nothing.

This is then trained by the programme and eventually exported from the Tensorflow tab onto local files which is then later pushed onto the github account.
 
## Creating a Rock-Paper-Scissors game
Create another file called manual_rps.py that will be used to play the game without the camera through functions: get_computer_choice and get_user_choice and eventually further coding to work out who won. 

## Use the camera to play Rock-Paper-Scissors
Replaced the hard-coded user guess with the output of the computer vision model. Created a new file called camera_rps.py which will have the new code.

Create a new function called get_prediction that will return the output of the model used earlier.

Use the function time.time() to get how much time has passed since the script started.

The game was repeated until either the computer or the user wins three rounds.
