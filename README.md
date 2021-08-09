# Real Time Dangerous Object Detection and Alarm with NVIDIA Jetson

## Motivation
We expect cups or security officers to be aware of situations that may pose a danger to us and to take precautions. But it is far from the truth to expect a person to thoroughly examine security cameras throughout the day.

However, it is not difficult to create safe zones in living spaces with Artificial Intelligence. Especially in children's playgrounds, school yards, work areas or in front of our house. With this project I have developed, it is possible to detect a dangerous object in real time. As soon as the object is detected, the alarm system works and warns you, preventing possible chaos.
<p align= "center">
<img src="https://user-images.githubusercontent.com/73293751/128674807-f6defe21-cae5-4212-9634-cb0a56c4deda.jpeg" width="470" height="275">
</p>
 
# Project

## Peripheral Devices
- Nvidia Jetson 
- Logitech C270 Webcam
- Breadboard
- Jumpers
- Passive Buzzer

## Pin Configuration
PWM Ports are used in this Project. In Jetson Nano, you have to change the 33rd or 32nd pin functions PWM to use passive buzzer. Passive buzzers need to output analog signals, but on the Jetson Nano we use pwm signals to make "beep" sound. You can find how to use PWM on Jetson Nano **[here.](https://forums.developer.nvidia.com/t/how-do-i-use-pwm-on-jetson-nano/72595/7)** Logic Power pin connected to 5V (4th pin).

## How Does It Work?
You can reach my demo on this youtube **[link.] (BURAYA PROJE LİNKİ GELCEK)** . Model dataset downloaded from **[Kaggle](https://www.kaggle.com/atulyakumar98/gundetection)**. This dataset contains 3000 picture and labeled with yolov3 txt format. So the first thing I did was convert the dataset Yolo V3 to PASCAL VOC format. You can reach this python script **[right there.](https://github.com/melikecolak/Dangerous-Object-Alarm-Project/blob/main/txt-to-xml.py)**. 
Then training section i used very useful library  **[Jetson-inference](https://github.com/dusty-nv/jetson-inference)**. 

