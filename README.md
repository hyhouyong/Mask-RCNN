# Mask R-CNN for Object Detection and Segmentation

This is an implementation of [Mask R-CNN](https://arxiv.org/abs/1703.06870) on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.
## Show
 use cpu ,epochs 5
![](https://github.com/hyhouyong/Mask-RCNN/blob/master/assert/Figure_1.png)
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

* Details:(https://www.cnblogs.com/houyong/p/10266228.html)
 
3.Download pre-trained weights
===
mask_rcnn_coco.h5
* BaiDuYun:https://pan.baidu.com/s/1CmcfVleyw7QpVZRo3JxS2w code:tf7f
    
    
4.Train
===
    python train_shape.py
5.Test
===
    python test_shape.py
    
