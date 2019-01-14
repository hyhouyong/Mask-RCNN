# Mask R-CNN for Object Detection and Segmentation

This is an implementation of [Mask R-CNN](https://arxiv.org/abs/1703.06870) on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.

## Getting Started 

1.Environment
===
    Windows/Linux + Keras >= 2.0.8 + TensorFlow >= 1.3.0
    pip install -r requirements.txt
2.Custom Train Data
===
    pip install labelme
    labelme
    mkdir train_data
    train_data
        |-json
        |-labelme_json
        |-pic
        |-cv2_mask
 ====
 Details:(https://www.cnblogs.com/houyong/p/10266228.html)
 3.Download trained weights
 ===
    
 4.Train
 ===
    python train_shape.py
 5.Test
 ===
    python test_shape.py
    
