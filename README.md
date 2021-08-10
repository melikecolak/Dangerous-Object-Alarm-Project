# Real Time Dangerous Object Detection and Alarm with NVIDIA Jetson

## Motivation
We expect cops or security officers to be aware of situations that may pose a danger to us and to take precautions. But it is far from the truth to expect a person to thoroughly examine security cameras throughout the day.

However, it is not difficult to create safe zones in living spaces with Artificial Intelligence. Especially in children's playgrounds, school yards, work areas or in front of our house. With this project I have developed, it is possible to detect a dangerous object in real time. As soon as the object is detected, the alarm system works and warns you, preventing possible chaos.
<p align= "center">
<img src="https://user-images.githubusercontent.com/73293751/128674807-f6defe21-cae5-4212-9634-cb0a56c4deda.jpeg" width="470" height="275">
</p>
 
## Project

## Peripheral Devices
- Nvidia Jetson 
- Logitech C270 Webcam or Raspberry Pi Camera
- Breadboard
- Jumpers
- Passive Buzzer

## Pin Configuration
PWM Ports are used in this Project. In Jetson Nano, you have to change the 33rd or 32nd pin functions PWM to use passive buzzer. Passive buzzers need to output analog signals, but on the Jetson Nano we use pwm signals to make "beep" sound. You can find how to use PWM on Jetson Nano **[here.](https://forums.developer.nvidia.com/t/how-do-i-use-pwm-on-jetson-nano/72595/7)** Logic Power pin connected to 5V (4th pin).

## How Does It Work?
You can reach my demo on this youtube **[link.](https://youtu.be/qKqjXZwpTS4)** . Model dataset downloaded from **[Kaggle](https://www.kaggle.com/atulyakumar98/gundetection)**. This dataset contains 3000 picture and labeled with yolov3 txt format. So the first thing I did was convert the dataset Yolo V3 to PASCAL VOC format. You can reach this python script **[right there.](https://github.com/melikecolak/Dangerous-Object-Alarm-Project/blob/main/txt-to-xml.py)**. 
In training section, i used very useful library  **[Jetson-inference](https://github.com/dusty-nv/jetson-inference)**, then trained my dataset with SSD-Mobilenet model.

## Run !
1. Build jetson-inference from the source with  **[this guide](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)**
2. Clone the project.
``` bash
git clone https://github.com/melikecolak/Dangerous-Object-Alarm-Project.git
```
3. Go to project directory.
``` bash
cd Dangerous-Object-Alarm-Project
```
4. Run the demo!
Camera depends on you. If you use csi camera instead usb, you have to change csi://0. If you want to learn more about Camera Streaming and Multimedia, you can visit **[this link.](https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-streaming.md)**
``` bash
python3 danger_alert.py --model=model/ssd-mobilenet.onnx --labels=model/labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes v4l2:///dev/video0
```

