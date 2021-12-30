# Literature Survey Notes

## An Automated System for ECG Arrhythmia Detection Using Machine Learning Techniques


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



> BibTex

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