from ultralytics import YOLO# 加载模型
model = YOLO("ultralytics/models/v8/yolov8s.yaml")  # 从头开始构建新模型# Use the model
results = model.train(data="VisDrone.yaml", epochs=100,device='0,1,2,3')  # 训练模型

