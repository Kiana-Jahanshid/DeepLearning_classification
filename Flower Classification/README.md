# 17 Flowers classification with Deep Learning


# Description 
In this face classification project ,  we have used CNN to predict Flower images labels , and a dataset which contains 17 classes of flowers.


# How to install 
```
pip install -r requirements.txt 
```


# How to run 


You only need to Run `AnimalClassification_Augment.ipynb` . At the end of the code , in inference part , corresponding predicted labels are shown .  


# RESULTS 
Here is the loss and accuracy results :
## without Augmentation 
|| Accuracy  | Loss |
| ------------ | ------------- | ------------- |
train  | 0.9964  | 0.0110 |
validation   | 0.6615  | 2.6746 |

## with Augmentation 
|| Accuracy  | Loss |
| ------------ | ------------- | ------------- |
train  | 0.8481  | 0.4208 |
validation   | 0.7692  | 0.8456 |

> # Conclusion :
> # validation accuracy increased by 10% using Data Augmentation .

### confusion matrix (with augmentation):
<p float="center">
    <img src  = "https://github.com/kiana-jahanshid/DeepLearning_classification/blob/main/Flower%20Classification/assets/confmat.png" width=500 /> 
</p>

### loss & accuracy diagram (with augmentation):
<p float="center">
    <img src  = "https://github.com/kiana-jahanshid/DeepLearning_classification/blob/main/Flower%20Classification/assets/loss_acc.png" width=500 /> 
</p>


## telegram bot :
<p float="center">
    <img src  = "https://github.com/kiana-jahanshid/DeepLearning_classification/blob/main/Flower%20Classification/assets/bot0.jpg" width=400 />   
    <img src  = "https://github.com/kiana-jahanshid/DeepLearning_classification/blob/main/Flower%20Classification/assets/bot1.jpg" width=400 /> 
</p>