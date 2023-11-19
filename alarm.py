import datetime
import time
import os
import pygame

def set_alarm(alarm_time, message, sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print(f"Alarm: {message}")
            pygame.mixer.music.play()
            break
        time.sleep(1)

# Example usage:
alarm_time = input("Enter the alarm time (HH:MM:SS): ")
alarm_message = input("Enter the alarm message: ")
sound_file = input("Enter the path to the sound file (e.g., alarm.mp3): ")

set_alarm(alarm_time, alarm_message, sound_file)
