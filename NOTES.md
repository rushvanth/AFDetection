# Literature Survey Notes

## An Automated System for ECG Arrhythmia Detection Using Machine Learning Techniques

### **Abstract:**
The new advances in multiple types of devices and machine learning models provide opportunities for practical automatic computer-aided diagnosis (CAD) systems for ECG classification methods to be practicable in an actual clinical environment. This imposes the requirements for the ECG arrhythmia classification methods that are inter-patient. We aim in this paper to design and investigate an automatic classification system using a new comprehensive ECG database inter-patient paradigm separation to improve the minority arrhythmical classes detection without performing any features extraction. We investigated four supervised machine learning models: support vector machine (SVM), k-nearest neighbors (KNN), Random Forest (RF), and the ensemble of these three methods. We test the performance of these techniques in classifying: Normal beat (NOR), Left Bundle Branch Block Beat (LBBB), Right Bundle Branch Block Beat (RBBB), Premature Atrial Contraction (PAC), and Premature Ventricular Contraction (PVC), using inter-patient real ECG records from MIT-DB after segmentation and normalization of the data, and measuring four metrics: accuracy, precision, recall, and f1-score. The experimental results emphasized that with applying no complicated data pre-processing or feature engineering methods, the SVM classifier outperforms the other methods using our proposed inter-patient paradigm, in terms of all metrics used in experiments, achieving an accuracy of 0.83 and in terms of computational cost, which remains a very important factor in implementing classification models for ECG arrhythmia. This method is more realistic in a clinical environment, where varieties of ECG signals are collected from different patients.
### **Models Used:** 
- SVM
- KNN
- Random Forest

### **Parameters Classified:** 
- Normal beat
- Left Bundle Branch Block Beat
- Right Bundle Branch Block Beat
- Premature Atrial Contraction
- Premature Ventricular Contraction

### **Result:** 

SVM is better than all the other three.  

**Accuracy:** 
- SVM - 0.83
- RF - 0.81
- KNN - 0.78 

**Computational Cost:**

![Paper1](images/paper1.jpg)

## Automatic classification of heartbeats using ECG morphology and heartbeat interval features

### **Abstract:**
A method for the automatic processing of the electrocardiogram (ECG) for the classification of heartbeats is presented. The method allocates manually detected heartbeats to one of the five beat classes recommended by ANSI/AAMI EC57:1998 standard, i.e., normal beat, ventricular ectopic beat (VEB), supraventricular ectopic beat (SVEB), fusion of a normal and a VEB, or unknown beat type. Data was obtained from the 44 nonpacemaker recordings of the MIT-BIH arrhythmia database. The data was split into two datasets with each dataset containing approximately 50 000 beats from 22 recordings. The first dataset was used to select a classifier configuration from candidate configurations. Twelve configurations processing feature sets derived from two ECG leads were compared. Feature sets were based on ECG morphology, heartbeat intervals, and RR-intervals. All configurations adopted a statistical classifier model utilizing supervised learning. The second dataset was used to provide an independent performance assessment of the selected configuration. This assessment resulted in a sensitivity of 75.9%, a positive predictivity of 38.5%, and a false positive rate of 4.7% for the SVEB class. For the VEB class, the sensitivity was 77.7%, the positive predictivity was 81.9%, and the false positive rate was 1.2%. These results are an improvement on previously reported results for automated heartbeat classification systems.
### **Models Used:**

### **Parameters Classified:** 
### **Result:** 
**Accuracy:** 
**Computational Cost:**

> BibTex
1. 
```
@Article{jcm10225450,
AUTHOR = {Sraitih, Mohamed and Jabrane, Younes and Hajjam El Hassani, Amir},
TITLE = {An Automated System for ECG Arrhythmia Detection Using Machine Learning Techniques},
JOURNAL = {Journal of Clinical Medicine},
VOLUME = {10},
YEAR = {2021},
NUMBER = {22},
ARTICLE-NUMBER = {5450},
URL = {https://www.mdpi.com/2077-0383/10/22/5450},
PubMedID = {34830732},
ISSN = {2077-0383},
ABSTRACT = {The new advances in multiple types of devices and machine learning models provide opportunities for practical automatic computer-aided diagnosis (CAD) systems for ECG classification methods to be practicable in an actual clinical environment. This imposes the requirements for the ECG arrhythmia classification methods that are inter-patient. We aim in this paper to design and investigate an automatic classification system using a new comprehensive ECG database inter-patient paradigm separation to improve the minority arrhythmical classes detection without performing any features extraction. We investigated four supervised machine learning models: support vector machine (SVM), k-nearest neighbors (KNN), Random Forest (RF), and the ensemble of these three methods. We test the performance of these techniques in classifying: Normal beat (NOR), Left Bundle Branch Block Beat (LBBB), Right Bundle Branch Block Beat (RBBB), Premature Atrial Contraction (PAC), and Premature Ventricular Contraction (PVC), using inter-patient real ECG records from MIT-DB after segmentation and normalization of the data, and measuring four metrics: accuracy, precision, recall, and f1-score. The experimental results emphasized that with applying no complicated data pre-processing or feature engineering methods, the SVM classifier outperforms the other methods using our proposed inter-patient paradigm, in terms of all metrics used in experiments, achieving an accuracy of 0.83 and in terms of computational cost, which remains a very important factor in implementing classification models for ECG arrhythmia. This method is more realistic in a clinical environment, where varieties of ECG signals are collected from different patients.},
DOI = {10.3390/jcm10225450}
}
```
<<<<<<< HEAD
2.
```
@ARTICLE{1306572,  author={Philip de Chazal and O'Dwyer, M. and Reilly, R.B.},  journal={IEEE Transactions on Biomedical Engineering},   title={Automatic classification of heartbeats using ECG morphology and heartbeat interval features},   year={2004},  volume={51},  number={7},  pages={1196-1206},  doi={10.1109/TBME.2004.827359}}
```
=======


___

## Dealing with Class Imbalance in Data

1. SMOTE oversampling - Minority class is oversampled to increase the number of instances of that class. 
2. Weighting the cost function - Assign weights to your class labels such that the cost function penalizes loss on certain classes more severely.

Useful Resources :-

- [8 Tactics to Combat Imbalanced Classes in Your Machine Learning Dataset](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)
- [Resampling strategies for imbalanced datasets](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets)
- [Dealing with Imbalanced Data](https://towardsdatascience.com/methods-for-dealing-with-imbalanced-data-5b761be45a18)
- [How to Handle Imbalanced Classes in Machine Learning](https://elitedatascience.com/imbalanced-classes)

Papers :-

- [SMOTE Original Paper](https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume16/chawla02a-html/chawla2002.html)
- [Comparative study of algorithms for Atrial Fibrillation detection](https://ieeexplore.ieee.org/abstract/document/6164553)
- [Automated Atrial Fibrillation Detection using a Hybrid CNN-LSTM Network on Imbalanced ECG Datasets](https://www.sciencedirect.com/science/article/pii/S1746809420303323)
- [The Effect of Data Augmentation on Classification of Atrial Fibrillation in Short Single-Lead ECG Signals Using Deep Neural Networks](https://ieeexplore.ieee.org/abstract/document/9053800)
- [Robust ECG signal classification for detection of atrial fibrillation using a novel neural network](https://ieeexplore.ieee.org/abstract/document/8331487)
- [Detection of Atrial Fibrillation using model-based ECG analysis](https://ieeexplore.ieee.org/abstract/document/4761755)
- [Robust detection of atrial fibrillation from short-term electrocardiogram using convolutional neural networks](https://www.sciencedirect.com/science/article/pii/S0167739X20305410)
- [Reliable PPG-based algorithm in atrial fibrillation detection](https://ieeexplore.ieee.org/abstract/document/7833801)
- [K-margin-based Residual-Convolution-Recurrent Neural Network for Atrial Fibrillation Detection](https://arxiv.org/abs/1908.06857)
- [Ensemble Learning for Detection of Short Episodes of Atrial Fibrillation](https://ieeexplore.ieee.org/abstract/document/8553253)
- [Handling Class Overlap and Imbalance to Detect Prompt Situations in Smart Homes](https://ieeexplore.ieee.org/document/6753930)
- [MOON: A Mixed Objective Optimization Network for the Recognition of Facial Attributes](https://link.springer.com/chapter/10.1007%2F978-3-319-46454-1_2)
- [Learning Deep Features for One-Class Classification](https://arxiv.org/abs/1801.05365)

>>>>>>> 3b4f5d2c10bb28c7a2b0564823ccafa3c4a734cf
