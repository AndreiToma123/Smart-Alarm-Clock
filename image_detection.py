"""
Installation:
go to https://pytorch.org/get-started/locally/ and select the options suitable for installing pytorch in your computer then copy the command and run it.
type: 
git clone https://github.com/ultralytics/yolov5  #for cloning
cd yolov5
pip install -r requirements.txt  # installing dependencies
"""

import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
img = "selfie.png"   #file "selfie.png" will be automatically generated when you take a selfie from CameraUi.py
#img = "pic1.jpeg"   #or img = "pic2.jpg" if you want to test without taking a selfie if your camera has low quality

results = model(img)
results.print()
#results.show() #if you want to see the detection on picture


