Code description
This is the public code of the paper DCF-Yolov8: An Improved Algorithm for Aggregating Low-Level Features to Detect Agricultural Pests and Diseases
The paper address is https://www.mdpi.com/2073-4395/13/8/2012

Paper algorithm improvement
Based on the characteristics of the IP102 agricultural pest data set, we improved the C2F module and proposed D2F. The module structure is shown in the figure below. This module has better feature extraction effects on low-level features of agricultural pests and diseases.

![image](https://github.com/SprBoot/DCF-Yolov8/assets/44434637/3a6d71b0-f138-489e-ba65-fbdfa7495a04)

For specific codes, see DCF-Yolov8/ultralytics/nn/modules/block.py

We use the Mish activation function, which is more robust in dealing with nonlinear features. Our algorithm's ability to learn feature effects is still strong at higher rounds.
