import cv2
thres=0.5
cap=cv2.VideoCapture(0)

cap.set(3,648)
cap.set(4,448)
cap.set(10,70)


className=[]
classFile='coco.names'
with open(classFile,'rt') as f:
	className=f.read().rstrip('\n').split('\n')
#print(className)

configPath='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath='frozen_inference_graph.pb'

#automatic detaction  model of deep nueral network.

net=cv2.dnn_DetectionModel(weightsPath,configPath)

# net ki property 

net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)
#-----------------------------------------------------------------------
#camera setup
while True:
	success,img=cap.read()
	classIds,confs,bbox=net.detect(img,confThreshold=thres)
	print(classIds,bbox)
	if len(classIds)!=0:
		for classId, confidence,box in zip (classIds.flatten(),confs.flatten(),bbox):
			cv2.rectangle(img,box,color=(0,255,0),thickness=2)
			cv2.putText(img,className[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
			cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
	cv2.imshow("output",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break





