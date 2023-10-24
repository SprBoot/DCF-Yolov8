Code description

This is the public code of the paper DCF-Yolov8: An Improved Algorithm for Aggregating Low-Level Features to Detect Agricultural Pests and Diseases
The paper address is https://www.mdpi.com/2073-4395/13/8/2012

Paper algorithm improvement

Based on the characteristics of the IP102 agricultural pest data set, we improved the C2F module and proposed D2F. The module structure is shown in the figure below. This module has better feature extraction effects on low-level features of agricultural pests and diseases.

![image](https://github.com/SprBoot/DCF-Yolov8/assets/44434637/3a6d71b0-f138-489e-ba65-fbdfa7495a04)

For specific codes, see DCF-Yolov8/ultralytics/nn/modules/block.py

We use the Mish activation function, which is more robust in dealing with nonlinear features. Our algorithm's ability to learn feature effects is still strong at higher rounds.

![image](https://github.com/SprBoot/DCF-Yolov8/assets/44434637/b97c0cf5-ccda-47ef-b218-d8537e7f3bec)

For details on modifying the activation function code, see DCF-Yolov8/ultralytics/nn/modules/conv.py

We have uploaded the model training results.You can download it at https://drive.google.com/drive/folders/1q5YWRY2el8SOZOdxBRwH-PA7rsCuoPjm?usp=drive_link. Ours.zip and Ours-val.zip are the training results and verification results of our improved algorithm. yolov8.zip and yolov8-va.zip are the training and verification results of the yolov8 algorithm. yolov8-mish.zip is the result we used for ablation experiments. The results include our model weights and experimental metrics.

We have summarized the original images in the paper, see agronomy.pptx for details

Acknowledgments

Our paper is an improvement on the Yolov8 algorithm, thanks to the Yolov8 team[https://github.com/ultralytics/ultralytics.git]. Thanks to the IP102 dataset team[https://github.com/xpwu95/IP102.git].Thanks to yolox[https://github.com/Megvii-BaseDetection/YOLOX.git], yolov5 algorithm[https://github.com/ultralytics/yolov5.git]. The code for the heat map comes from https://github.com/z1069614715/objectdetection_script.git.
