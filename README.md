# Object-Detection-using-Python-Yolo-Algorithm
PROJECT OBJECTIVE--
To create a robust object detection system using OpenCV with the MobileNet-SSD  model for real time recognition of objects from the COCO dataset, employing a  camera-based video feed for dynamic visualization.

Description--
This project integrates a pre-trained  MobileNet-SSD model to detect and  classify objects in real time. The system  uses COCO dataset classes and displays  detected objects with bounding boxes and confidence levels.

Project Details--
Real-Time Detection:Achieve real-time object detection in video streams or camera feeds with high accuracy and speed.

Multi-Class Object Recognition:  Detect and classify multiple objects of  various classes simultaneously within a single frame, such as persons,  vehicles, animals, and everyday items.

Integration with OpenCV:  Utilize OpenCV for pre-processing (resizing,scaling, and normalization) and post-processing of images to enhance the performance and user experience.

User-Friendly Interface: Develop an interface for easy visualization and  interaction, allowing users to see the detected objects and obtain relevant information in real-time.

Overview of Object Detection:-

Object Detection is a computer vision technique that involves identifying and  locating objects within an image or video. Unlike image classification, which assigns a label to an entire image, object detection provides:
Class Identification
Localization

Why Choose YOLO?:-

If your project requires real-time object detection with good accuracy and the ability to handle multiple objects simultaneously, YOLO is the ideal choice. Its speed and simplicity make it suitable for a variety of applications, even on devices with limited processing power.

PROJECT MODULES 
Implementation Details :

1. Dataset and Model Initialization:  Load class labels from coco.names to map object IDs to names.Configure the model using the provided .pbtxt and .pb files.
2. Camera and Video Stream Setup: Initialize the video feed (cv2.VideoCapture(0)). Set resolution and other parameters like brightness for optimal  performance.
3. Object Detection: Process each video frame using the cv2.dnn_DetectionModel. Perform object detection with a confidence threshold of 50%.
4. Visualization and Annotation: Draw bounding boxes and display object names with confidence levels. Real-time visualization using cv2.imshow.
5. User Control: Provide an interface to exit the program by pressing 'q'.
   

APPLICATION OF PROJECT  
1. Surveillance Systems: Identifying and tracking people or vehicles.

2. Autonomous Vehicles: Detecting pedestrians, cars, traffic signs, etc.

3. Medical Imaging: Detecting tumors or abnormalities in scans.


How to run the code :
      1. First open cmd . 
       2. Then select Project Directory  using cd
       3. For run the project use command :
	python project_name.py
          Here we use command for own project :
	python main.py

# Screenshot---
https://github.com/CodingwithAnkit-tech/Object-Detection-using-Python-Yolo-Algorithm/blob/main/Object-Detection-using-Python-Yolo-Algorithm.png








 




