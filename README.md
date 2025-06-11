# Adaptive Weighted Entropy Minimization for Universal Domain Adaptation

This repository contains the code for the paper "Adaptive Weighted Entropy Minimization for Universal Domain Adaptation" 

## Requirements

The code is written in Python 3.6 and requires the following packages:

- [apex](https://github.com/NVIDIA/apex) 
- python 3.8.10
- torch 1.12.0+cu113
- torchvision 0.13.0+cu113
- pyyaml==5.4.1
- easydict
- neptune
- numpy==1.24.4
- scikit-learn==1.3.2

[data-preparation](https://github.com/VisionLearningGroup/OVANet?tab=readme-ov-file#data-preparation) and [training-and-evaluation](https://github.com/VisionLearningGroup/OVANet?tab=readme-ov-file#training-and-evaluation) are the same as the OVANet.


针对ACM MM提出的问题进行下面三个实验：
1. 修改amazon目标域数据集中的样本比例，测试data imbalance的情况
2. 使用O分类器的输出作为权重，和现有权重做对比，提供理论依据
3. 修改backbone，改成ViT