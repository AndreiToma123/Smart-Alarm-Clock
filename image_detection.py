"""
Objects and face detection on images

Installation:
go to https://pytorch.org/get-started/locally/ and select the options suitable for installing pytorch in your computer then copy the command and run it.
type: 
git clone https://github.com/ultralytics/yolov5  #for cloning yolov5
cd yolov5
pip install -r requirements.txt  # installing dependencies
"""

import torch

class ImageDetection:
    def __init__(self, image):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='final.pt', force_reload=True)
        self.results = self.model(image)
        self.results.print() #result 
        self.results.show() #if you want to see the detection on picture

if __name__ == "__main__":
    ImageDetection("selfie.png") 
    #file "selfie.png" will be automatically generated when you take a selfie from CameraUi.py
    #if you want to test without taking a selfie, change "selfie.png" to "pic1.jpeg" or "pic2.jpg" or "Face2.png".

