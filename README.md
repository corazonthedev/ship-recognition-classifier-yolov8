![wallp](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/8f8e3f91-f1f8-437d-a1c0-1cd282399efb)

# Overview

Custom trained Ship Recognition YOLOv8 with roboflow.


# How to Get API KEY

[How to get API KEY in roboflow](https://docs.roboflow.com/api-reference/authentication)

# How to Download

**You must use Python>=3.8,<=3.11 for installing requirements.**

    
      git clone https://github.com/corazonthedev/ship-recognition-classifier-yolov8
      cd ship-recognition-classifier-yolov8
      pip install -r requirements.txt


After getting your API KEY

      echo MY_API_KEY=your_api_key_here > .env
      python main.py

# How to Use

Select your input 
![1](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/7704d0e8-318b-4e12-a980-db7a6a9c8935)


## 1-For Image

Select your image 
![2](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/f9adc649-647e-464f-806f-a1f4b58fa2b2)

After a while result image will be displayed 
![3](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/60ad7e8c-0833-4e4a-8a2c-49ac07a1d724)

Result image is also saved as prediction.jpg
![4](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/f1f5c477-4b97-4e68-95fb-dab8c059bdb5)


## 2-For Video

Select your video
![5](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/706c8348-0479-4bb1-8e96-34378c9a7495)

Video will be processed
![6](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/d5414177-93d5-4dbd-b0eb-2acf6e43492a)

After a while result video will be displayed 


![7](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/5d08f567-070e-442f-930c-058a1801ded4)

Result video is also saved as output.mp4 with resulst.json file
![8](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/d3e18916-54eb-49eb-9c1b-fcb8f40486db)


## 3-For Webcam

[Webcam Example](https://youtu.be/WzT_XE2CNFI)

## On Roboflow

You can also use it in Roboflow [roboflow-recog-boats](https://universe.roboflow.com/boats-erj7q/recog-boat)

![10](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/19c88762-00f8-4a60-9dbe-7e745fe5d284)


# About Classifier 

![11](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/d5d4ceae-58d5-4163-a14c-9b97256859d0)

Classifier is currently using 1031 images in it's dataset. Without upgrading your plan Roboflow allows users 1000 Auto Label Credits, without auto labelling you can label images manually.  

As you can see in metrics, classifier is not very accurate because of insufficient dataset. It can be improved with uploading and labelling more data. 

You can also set confidence for both video and image input.

For images:


![image](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/481aadd1-af44-438c-85a0-e4e25fb9a413)


For videos:


![image](https://github.com/corazonthedev/ship-recognition-classifier-yolov8/assets/137296314/07f72ecb-ee26-4417-99ef-19fa85706aef)



[Creating Custom Trained Model](https://blog.roboflow.com/getting-started-with-roboflow/)





