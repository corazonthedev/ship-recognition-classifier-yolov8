import roboflow
import numpy as np 
import supervision as sv
import json, cv2, os 
from tkinter import filedialog
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("MY_API_KEY")

rf = roboflow.Roboflow(api_key=api_key) #access API KEY
project = rf.workspace().project("recog-boat") #select workspace
model = project.version("2").model #select version
img, vid = None, None

class ship_recognition_classifier():
    def __init__(self):
        selected_input = input("select input type 1-image 2-video 3-webcam: ")
        if selected_input == "1": self.get_img()
        elif selected_input == "2": self.get_vid()
        elif selected_input == "3": self.webcam()
        else: self.__init__() #looping

    def get_img(self):
        img = filedialog.askopenfilename(filetypes=[("Image", "*.jpg;")]) 
        return self.predict_image(img)
        
    def get_vid(self):
        vid = filedialog.askopenfilename(filetypes=[("Video", "*.mp4;")]) 
        return self.predict_video(vid)

    def predict_image(self,img):
        prediction = model.predict(img, confidence=50, overlap=30).save('prediction.jpg')
        image = cv2.imread('prediction.jpg') #open saved file
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def predict_video(self,vid):
        job_id, signed_url, expire_time = model.predict_video( #run the model on the video
        vid,
        fps=5,
        prediction_type="batch-video")

        results = model.poll_until_video_results(job_id) #wait for the results

        confidence_threshold = 0.7 #set a confidence threshold

        for frame in results['recog-boat']: #filter the results based on the confidence threshold
            frame['predictions'] = [pred for pred in frame['predictions'] if pred['confidence'] >= confidence_threshold]

        with open("results.json", "w") as f: #save the filtered results to a JSON file
            json.dump(results, f)

        with open("results.json", "r") as f: #load your results
            results = json.load(f)

        def callback(scene: np.ndarray, index: int) -> np.ndarray: #define a callback function to process each frame
            if index in results["frame_offset"]: #create a Detections object from the inference results for the current frame
                detections = sv.Detections.from_inference(
                    results["recog-boat"][results["frame_offset"].index(index)])
                #extract the class names for the predictions in the current frame
                class_names = [i["class"] for i in results["recog-boat"][results["frame_offset"].index(index)]["predictions"]]
            else:
                #if the current frame index does not exist in the results, find the nearest frame index that does
                nearest = min(results["frame_offset"], key=lambda x: abs(x - index))
                #create a Detections object from the inference results for the nearest frame
                detections = sv.Detections.from_inference(
                    results["recog-boat"][results["frame_offset"].index(nearest)])
                #extract the class names for the predictions in the nearest frame
                class_names = [i["class"] for i in results["recog-boat"][results["frame_offset"].index(nearest)]["predictions"]]

            bounding_box_annotator = sv.BoundingBoxAnnotator() #create box
            label_annotator = sv.LabelAnnotator() #create label
            
            labels = [class_names[i] for i, _ in enumerate(detections)] #set labels

            #create labeled video
            annotated_image = bounding_box_annotator.annotate(
                scene=scene, detections=detections)
            annotated_image = label_annotator.annotate(
                scene=annotated_image, detections=detections, labels=labels)

            return annotated_image 

        sv.process_video(
            source_path=vid,
            target_path="output.mp4",
            callback=callback,)
    
        video_path = "output.mp4"  
        cap = cv2.VideoCapture(video_path)
        while True: #open saved video
            ret, frame = cap.read()

            if not ret:
                break
            cv2.imshow("Video", frame)
            
            if cv2.waitKey(25) & 0xFF == ord('q'): #q for exit
                break
            
        cap.release()
        cv2.destroyAllWindows()

    def webcam(self):
        from inference import InferencePipeline
        from inference.core.interfaces.stream.sinks import render_boxes
        import warnings
        warnings.filterwarnings("ignore") #for SupervisionWarnings
        pipeline = InferencePipeline.init(
            model_id="recog-boat/2",
            video_reference=0, #0 for webcam
            on_prediction=render_boxes) #function to run after each prediction
        pipeline.start()
        pipeline.join()

if __name__ == "__main__":
    sdc = ship_recognition_classifier()
