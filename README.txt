# Unlock Door System for Speech Impaired using IoT and Deep Learning

This project is designed to help speech-impaired individuals unlock a door using hand gestures. It uses a combination of computer vision, machine learning, and IoT technologies to detect and interpret hand gestures, and then trigger the unlocking mechanism of a solenoid lock.

## Features

- Hand gesture recognition using computer vision and machine learning
- Solenoid lock control using Arduino Nano
- Text-to-speech output using Pyttsx3
- Integration with IFTTT to trigger events

## Hardware Requirements

- Intel Core i7-10 gen, i5-12 gen, or i5-10 gen CPU
- 8 GB to 16 GB RAM
- 40 GB hard drive
- 12V solenoid lock
- 15V DC charger
- 5V relay
- Arduino Nano
- Jumper wires
- Micro USB
- Power supply
- Wireless network

## Software Requirements

- Python 3.10.10
- Visual Studio Code
- OpenCV
- Serial
- Time
- Cvzone 1.5.6
- Requests 2.28.2
- Windows 11
- Pyttsx3
- Tensorflow
- IFTTT

## Installation

1. Clone the repository: git clone https://github.com/AngelaMore/Door-Unlock-System-for-Speech-Impaired-using-IoT-and-Deep-Learning.git
2. Install necessary libraries
3. Connect the solenoid lock and the relay to the Arduino Nano as per the circuit diagram
4. Run the main program:'python lock.py'

## Usage

1. Position the camera to capture the hand gestures
2. Make sure the solenoid lock is connected to the relay and the relay is connected to the Arduino Nano
3. Run the program and wait for the hand detection to start
4. Show the hand gestures to unlock the door
5. If the set pin matches then the solenoid lock unlocks
5. The text-to-speech output will indicate whether the door has been unlocked or not
6. The IFTTT integration will trigger an event to send a text message via SMS

## Credits

Angela More, Siddhi Mhatre, Vanshika Patil,Varsha Kamble

Under the Guidance of Prof. Sujata Bhairyallkar
  
Department of Computer Engineering, Saraswati College of Engineering

