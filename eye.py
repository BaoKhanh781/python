from gpiozero import RGBLED
from time import sleep
#Define eye board
right_eye_led = RGBLED(red="BOARD3",green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8",green="BOARD10", blue="BOARD12")
#Receive and break down features
def extract_features(command):
    print(command)
    extract_features = command["features"]
    print(extract_features)
    if("eyes" in extract_eye_features):
        print("Found Eyes")
        eye_features = extract_features["eyes"]
        eyes(eye_features)
       
#Perform the command for eyes
def eyes(eye_command):
    print(eye_command)
    if("set_right_rgb_eye_color" in eye_command):
        print("Found Set Right eye Color")
        right_eye_rgb = eye_command["set_right_rgb_eye_color"]
        print(right_eye_rgb)
       
def main():
    print("Starting Program")
    command = {"robot": "Doraemon", "features":{"eyes": {"set_right_rgb_eye_color": [255, 0, 0]}}}
    extract_features = command["features"]
   
    print("Ending Program")
   
main()
