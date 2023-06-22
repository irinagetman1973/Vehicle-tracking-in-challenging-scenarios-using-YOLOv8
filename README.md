
<div align="center">

# Vehicle Tracking in Challenging Scenarios using YOLOv8

  <p>
    <a align="center" href="https://ultralytics.com/yolov8" target="_blank">
      <img width="50%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png?1687402279656"></a>
  </p>

<br>

<div>
 

    <a href="https://console.paperspace.com/github/ultralytics/ultralytics"><img src="https://assets.paperspace.io/img/gradient-badge.svg" alt="Run on Gradient"/></a>
    <a href="https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
    <a href="https://www.kaggle.com/ultralytics/yolov8"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>
  </div>
  <br>
</div>

## Introduction

This is a semester-long coursework for the third year of the Bachelor of Software Engineering program at Yoobee Colleges in Auckland, focusing on advanced topics in software development and project management.

This repository contains code for a vehicle tracking system based on the [YOLOv8](https://github.com/ultralytics/ultralytics) object detection algorithm.The interface is powered by [Streamlit](https://github.com/streamlit/streamlit). The system is designed to work in challenging scenarios, such as low light conditions, occlusions, and fast motion.

## Features
- Feature1: Object detection task.
- Feature2: Multiple detection models. `yolov8n`, `yolov8s`, `yolov8m`, `yolov8l`, `yolov8x`
- Feature3: Multiple input formats. `Image`, `Video`, `Webcam`
- Feature4: Multiple Object Tracking and Counting.

## Run online
You can use [This](https://monemati-yolov8-deepsort-streamlit-app-et5bli.streamlit.app/) link to try an online version on Streamlit.   

## Installation
### Create a virtual environment
```commandline
# create
python -m venv myvenv

# activate
myvenv\Sripts\activate
```

### Clone repository
```commandline
git clone 
cd YOLOv8-Streamlit
```

### Install packages
```commandline
# Streamlit dependencies
pip install streamlit

# YOLOv8 dependecies
pip install -e '.[dev]'
```
### Download Pre-trained YOLOv8 Detection Weights
Create a directory named `weights` and create a subdirectory named `detection` and save the downloaded YOLOv8 object detection weights inside this directory. The weight files can be downloaded from the table below.

| Model                                                                                | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt) | 640                   | 37.3                 | 80.4                           | 0.99                                | 3.2                | 8.7               |
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt) | 640                   | 44.9                 | 128.4                          | 1.20                                | 11.2               | 28.6              |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) | 640                   | 50.2                 | 234.7                          | 1.83                                | 25.9               | 78.9              |
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt) | 640                   | 52.9                 | 375.2                          | 2.39                                | 43.7               | 165.2             |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 640                   | 53.9                 | 479.1                          | 3.53                                | 68.2               | 257.8             |


## Run
```commandline
streamlit run app.py
```
Then will start the Streamlit server and open your web browser to the default Streamlit page automatically.
For Object Counting, you can choose "Video" from "Select Source" combo box and use "test3.mp4" inside videos folder as an example.

## Result

![alt text](images/YOLOv8-DeepSort-Streamlit-Counting.jpg "YOLOv8 DeepSort Streamlit Counting")
  
## Acknowledgement
- https://github.com/ultralytics/ultralytics
- https://github.com/streamlit/streamlit
- https://github.com/JackDance/YOLOv8-streamlit-app







## Things to do as of 12, May
1) new data recording and re-testing pretrained YOLOv8 model '&#x2705;'  [update: done on 16/05. Notebook "Custom_video_track_count"] 


2) work on evaluation  metrics (F1-score) and work out what other metrics used for Object Detection evaluation 

3) design the UI using Flask

4) submit a paper

## Things to do as of May,19

1) Improve the confidence score (Calculate average confidence ?)

2) Train a custom YOLOv8 model on one bright video &#x2705;

3) Test a new model on the second bright video &#x2705;

4) Do Cross Validation

5) Retest models again and evaluate metrics to see whether performances are consistant

6) List challenges for example, add very bright sun, small sizes of detected vehicles

## Questions for Scrum meeting 24/05

1) Is Literature Review required for an R&D report?

2) Time management tools. Scrum meetings? Trello?
