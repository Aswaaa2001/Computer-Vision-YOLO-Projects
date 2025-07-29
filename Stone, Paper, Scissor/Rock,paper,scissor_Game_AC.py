import pygame
import random
import time
import pyttsx3
import cv2
import threading
from ultralytics import YOLO

# Initialize Pygame and Speech Engine
pygame.init()
engine = pyttsx3.init()
model = YOLO("Yolov11Best_model.pt")

# Pygame window setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock, Paper, Scissors")
font = pygame.font.Font(None, 50)

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Countdown before each round
def countdown():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        text = font.render(str(i), True, (255, 255, 255))
        screen.blit(text, (400, 300))
        pygame.display.flip()
        pygame.time.wait(1000)
    return True

# Detect gesture with multiple frames for accuracy
def detect_gesture(cap, num_frames=5):
    detected_labels = []
    
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            continue
        
        label, _ = process_frame(frame)
        detected_labels.append(label)
    
    # Get the most frequent detected label
    most_frequent = max(set(detected_labels), key=detected_labels.count)
    return most_frequent if most_frequent != "Unknown" else "Unknown"

# Process frame and annotate
def process_frame(frame):
    results = model(frame)
    detected_labels = []
    
    for result in results:
        if result.boxes:
            for box in result.boxes:
                conf = box.conf[0].item()
                if conf > 0.1:
                    label = model.names[int(box.cls[0].item())]
                    detected_labels.append(label)
                    
                    # Draw bounding box
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    return (detected_labels[0] if detected_labels else "Unknown"), frame

# Display debug camera feed
def show_debug_window(cap, stop_event):
    while cap.isOpened() and not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break
        
        _, debug_frame = process_frame(frame)
        cv2.imshow("Debug Camera", debug_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Display messages in Pygame
def display_message(message, color):
    screen.fill((0, 0, 0))
    text = font.render(message, True, color)
    screen.blit(text, (250, 300))
    pygame.display.flip()
    pygame.time.wait(2000)



##########################################################



# Determine winner
def determine_winner(user, computer):
    user = user.capitalize().strip()  # Normalize user input
    computer = computer.capitalize().strip()  # Normalize computer choice

    # Fix inconsistent naming (Scissor vs. Scissors)
    if user == "Scissor":
        user = "Scissors"
    if computer == "Scissor":
        computer = "Scissors"
    
    ####################

    if user == "Stone":  # If detected as "Stone", change to "Rock"
        user = "Rock"

    if computer == "Stone":  # If computer randomly selects "Stone", change to "Rock"
        computer = "Rock"

    ###################


    if user == computer:
        return "It's a Tie!"

    winning_combinations = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if winning_combinations[user] == computer:
        return "You Won!"
    else:
        return "You Lost!"









#########################################################

# Main game loop
def game_loop():
    cap = cv2.VideoCapture(0)
    stop_event = threading.Event()
    
    debug_thread = threading.Thread(target=show_debug_window, args=(cap, stop_event))
    debug_thread.daemon = True
    debug_thread.start()
    
    while not stop_event.is_set():
        if countdown():
            user_choice = detect_gesture(cap)
            
            if user_choice == "Unknown":
                speak("No hand detected")
                display_message("No hand detected", (255, 0, 0))
                continue
            
            computer_choice = random.choice(["Rock", "Paper", "Scissors"])
            result = determine_winner(user_choice, computer_choice)
            speak(result)
            
            screen.fill((0, 0, 0))
            text = font.render(f"You: {user_choice}  Computer: {computer_choice}", True, (255, 255, 255))
            screen.blit(text, (100, 200))
            text = font.render(result, True, (255, 0, 0))
            screen.blit(text, (100, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

if __name__ == "__main__":
    game_loop()