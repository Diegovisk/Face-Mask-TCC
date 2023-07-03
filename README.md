# Face Mask Detection.

Python version: 3.8.17<br/>
Ultralytics version: 8.0.124

## Source for separated datasets:
https://www.kaggle.com/alexandralorenzo/maskdetection
https://www.kaggle.com/aditya276/face-mask-dataset-yolo-format
https://www.kaggle.com/andrewmvd/face-mask-detection

The combined dataset can be found on [Roboflow](https://app.roboflow.com/facemaskdatasetunion/face-mask-united-dataset/4).

AIZOO Face Mask dataset can be found at: [https://github.com/AIZOOTech/FaceMaskDetection](https://github.com/AIZOOTech/FaceMaskDetection).

### Setting up data:
Data from the combined dataset can be downloaded with Roboflow in the adequate format.

Data from the AIZOO dataset may need to be converted to the correct format.

More instructions are in the notebooks for each model's setup.

## Project goal:
Train YoloV8 and YoloNAS on the combined dataset, and then re-train its weights with AIZOO Dataset. Compare results to state-of-the-art works and try to perform better. 
