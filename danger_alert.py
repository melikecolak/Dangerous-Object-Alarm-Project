#Melike Colak 09.08.2021
import jetson.inference
import jetson.utils
import os
import argparse
import sys
import Jetson.GPIO as GPIO
import time


# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)



BuzzerPin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT) 
GPIO.setwarnings(False)
global Buzz 
Buzz = GPIO.PWM(BuzzerPin, 440) 
Buzz.start(50) 
Buzz.ChangeDutyCycle(0)

while True:

	try:
		# capture the next image
		img = input.Capture()

		# detect objects in the image (with overlay)
		detections = net.Detect(img, overlay=opt.overlay)
		
		
		# print the detections
		print("..........DETECTED {:d} OBJECTS IN IMAGE.........".format(len(detections)))
		for detection in detections:
			print(detection)
			if len(detections) > 0:
				class_id = detections[0].ClassID
				print(class_id)
				if class_id == 1:
					Buzz.ChangeDutyCycle(50)
					print("...............BUZZER IS RUNNING.............")
					time.sleep(0.05)
					Buzz.ChangeDutyCycle(0)
					
					# os.system('clear')
			
			
		# render the image
		output.Render(img)

		# update the title bar
		output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

		# print out performance info
		net.PrintProfilerTimes()

		# exit on input/output EOS
		if not input.IsStreaming() or not output.IsStreaming():
			break
	except KeyboardInterrupt:
		print(".............KEYBOARD INTERRUPT, EXITING PROGRAM..........")
		Buzz.stop()
		sys.exit(0) 

Buzz.stop()

