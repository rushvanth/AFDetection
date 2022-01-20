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

## Clustering ECG complexes using Hermite functions and self-organizing maps

### **Abstract:**
An integrated method for clustering of QRS complexes is presented which includes basis function representation and self-organizing neural networks (NN’s). Each QRS complex is decomposed into Hermite basis functions and the resulting coefficients and width parameter are used to represent the complex. By means of this representation, unsupervised self-organizing NN’s are employed to cluster the data into 25 groups. Using the MIT-BIH arrhythmia database, the resulting clusters are found to exhibit a very low degree of misclassification (1.5%). The integrated method outperforms, on the MIT-BIH database, both a published supervised learning method as well as a conventional template cross-correlation clustering method.

### **Models Used:** 
- SOM

### **Parameters Classified:** 
- Normal beat
- Fusion of Ventricular and Normal Beat
- Premature Atrial Beat
- Premature Ventricular Beat

### **Result:** 
Misclassification is too low (1.5%) in SOM compared to Conventional Cross Correlation method (4.4%)
CPU Consumption: less than 1 min/record

**Accuracy:** 
- SOM - 99.7%

## Automated detection of atrial fibrillation using R-R intervals and multivariate-based classification

### **Abstract:**
Automated detection of AF from the electrocardiogram (ECG) still remains a challenge. In this study, we investigated two multivariate-based classification techniques, Random Forests (RF) and k-nearest neighbor (k-nn), for improved automated detection of AF from the ECG. We have compiled a new database from ECG data taken from existing sources. R-R intervals were then analyzed using four previously described R-R irregularity measurements: (1) the coefficient of sample entropy (CoSEn), (2) the coefficient of variance (CV), (3) root mean square of the successive differences (RMSSD), and (4) median absolute deviation (MAD). Using outputs from all four R-R irregularity measurements, RF and k-nn models were trained. RF classification improved AF detection over CoSEn with overall specificity of 80.1% vs. 98.3% and positive predictive value of 51.8% vs. 92.1% with a reduction in sensitivity, 97.6% vs. 92.8%. k-nn also improved specificity and PPV over CoSEn; however, the sensitivity of this approach was considerably reduced (68.0%).

### **Models Used:** 
- KNN
- RF

### **Parameters Classified:** 
-  normal sinus rhythm
-  atrial fibrillation
-  pre-atrial contractions
-  pre-ventricular contractions
  
### **Result:** 
- Sensitivity 
  - KNN - 68%
  - RF - 92.8%
- Specificity
  - KNN - 95.1%
  - RF - 98.3%

## Comparative study of algorithms for Atrial Fibrillation detection

### **Abstract:**
Automatic detection of Atrial Fibrillation (AF) is necessary for the long-term monitoring of patients who are suspected to have AF. Several methods for AF detection exist in the literature. These methods are mainly based on two different characteristics of AF ECGs: the irregularity of RR intervals (RRI) and the fibrillatory electrical Atrial Activity (AA). The electrical AA is characterized by the absence of the P-wave (PWA) and special frequency properties (FSA). Nine AF detection algorithms were selected from literature and evaluated with the same protocol in order to study their performance under different conditions. Results showed that the highest sensitivity (Se=97.64%) and specificity (Sp=96.08%) was achieved with methods based on analysis of irregularity of RR interval, while combining RR and atrial activity analysis gave the highest positive predictive value (PPV=92.75%). Algorithms based on RR irregularity were also the most robust against noise (Se=85.79% and Sp=81.90% for SNR=0dB; and Se=82.52% and Sp=40.47% for SNR=-5dB).

### **Models Used**
- Nine algorithms based on analysis of RR Intervals and Atrial Activity
- **RRI**
  - Markov Model(MM)
  - Simple Variance Parameter
  - Statistical framework combination
  - Kolmogorov Smirnov test
  - Autoregressive modeling and white noise
- **AA**
  - QRS-T cancellation
- **Both RRI and AA**
  - Combined RRI using MM, with P wave absence (PWA) and Frequency spectrum analysis (FSA)
  - RRI, PWA based on the position and morphology of the P wave
  - RRI, PWA and FSA and classified using Neural Networks model.
  
### **Results**
- Highest Sensitivity - 97.64% (Statistical framework)
- Highest Specificity -  96.08% (Kolmogorov Smirnov test)
- Lowest Error - 5.32% (Kolmogorov Smirnov test)
- Highest PPV - 92.75% (RRI, PWA)
- Lowest Sensitivity - 62.8% (AA only)
- Lowest Specificity - 77.46% (AA only)
- Highest Error - 28.39% (AA only)
  
## Automated Atrial Fibrillation Detection using a Hybrid CNN-LSTM Network on Imbalanced ECG Datasets

### **Abstract:**
Atrial fibrillation is a heart arrhythmia strongly associated with other heart-related complications that can increase the risk of strokes and heart failure. Manual electrocardiogram (ECG) interpretation for its diagnosis is tedious, time-consuming, requires high expertise, and suffers from inter- and intra-observer variability. Deep learning techniques could be exploited in order for robust arrhythmia detection models to be designed. In this paper, we propose a novel hybrid neural model utilizing focal loss, an improved version of cross-entropy loss, to deal with training data imbalance. ECG features initially extracted via a Convolutional Neural Network (CNN) are input to a Long Short-Term Memory (LSTM) model for temporal dynamics memorization and thus, more accurate classification into the four ECG rhythm types, namely normal (N), atrial fibrillation (AFIB), atrial flutter (AFL) and AV junctional rhythm (J). The model was trained on the MIT-BIH Atrial Fibrillation Database and achieved a sensitivity of 97.87%, and specificity of 99.29% using a ten-fold cross-validation strategy. The proposed model can aid clinicians to detect common atrial fibrillation in real-time on routine screening ECG.

### **Models Used:** 
- LSTM

### **Parameters Classified:** 
-  normal
-  atrial fibrillation 
-  atrial flutter
-  AV junctional rhythm
  
### **Result:** 
Sensitivity - 97.87%
Specificity - 99.29%

## Robust ECG signal classification for detection of atrial fibrillation using a novel neural network

### **Abstract**
Electrocardiograms (ECG) provide a non-invasive approach for clinical diagnosis in patients with cardiac problems, particularly atrial fibrillation (AF). Robust, automatic AF detection in clinics remains challenging. Deep learning has emerged as an effective tool for handling complex data analysis with minimal pre- and post-processing. A 16-layer 1D Convolutional Neural Network (CNN) was designed to classify the ECGs including AF. One of the key advances of the proposed CNN was that skip connections were employed to enhance the rate of information transfer throughout the network by connecting layers earlier in the network with layers later in the network. Skip connections led to a significant increase in the feature learning capabilities of the CNN as well as speeding up the training time. For comparisons, we also have implemented recurrent neural networks (RNN) and spectrogram learning. The CNN was trained on 8,528 ECGs and tested on 3,685 ECGs ranging from 9 to 60 seconds in length. The proposed 16-layer CNN outperformed RNNs and spectrogram learning. The training of the CNN took 2 hours on a Titan XPascal GPU (NVidia) with 3840 cores. The testing accuracy for the CNN was 82% and the runtime was ~0.01 seconds for each signal classification. Particularly, the proposed CNN identified normal rhythm, AF and other rhythms with an accuracy of 90%, 82% and 75% respectively. We have demonstrated a novel CNN with skip connections to perform efficient, automatic ECG signal classification that could potentially aid robust patient diagnosis in real time.

### **Models Used**
- 16 layer 1D CNN
- Recurrent Neural Network
- Spectrogram Learning
  
### **Parameters Classified**
- Normal Rhythm
- AF
- Other Rhythms

### **Results**

![Paper1](images/F1_scores.jpg)

Overall Accuracy: 82%
Normal: 90%
AF: 82%
Others: 75%

**Computational Cost**
Training: 2 hours with 3840 cores
Testing: 0.01 seconds for each classification

## Detection of Atrial Fibrillation using model-based ECG analysis

### **Abstract**
Atrial fibrillation (AF) is an arrhythmia that can lead to several patient risks. This kind of arrhythmia affects mostly elderly people, in particular those who suffer from heart failure (one of the main causes of hospitalization). Thus, detection of AF becomes decisive in the prevention of cardiac threats. In this paper an algorithm for AF detection based on a novel algorithm architecture and feature extraction methods is proposed. The aforementioned architecture is based on the analysis of the three main physiological characteristics of AF: i) P wave absence ii) heart rate irregularity and iii) atrial activity (AA). Discriminative features are extracted using model-based statistic and frequency based approaches. Sensitivity and specificity results (respectively, 93.80% and 96.09% using the MIT-BIH AF database) show that the proposed algorithm is able to outperform state-of-the-art methods.

### **Methods Used**
- P wave absence (template based)
- Heart rate irregularity (Markov Process)
- Atrial Activity (Discrete Packet Wavelet Transform & QRS-T Cancellation)
    
### **Results**
- Sensitivity - 93.80% 
- Specificity - 96.09%

## Robust detection of atrial fibrillation from short-term electrocardiogram using convolutional neural networks

### **Abstract**
The most prevalent arrhythmia observed in clinical practice is atrial fibrillation (AF). AF is associated with an irregular heartbeat pattern and a lack of a distinct P-waves signal. A low-cost method for identifying this condition is the use of a single-lead electrocardiogram (ECG) as the gold standard for AF diagnosis, after annotation by experts. However, manual interpretation of these signals may be subjective and susceptible to inter-observer variabilities because many non-AF rhythms exhibit irregular RR-intervals and lack P-waves similar to AF. Furthermore, the acquired surface ECG signal is always contaminated by noise. Hence, highly accurate and robust detection of AF using short-term, single-lead ECG is valuable but challenging. To improve the existing model, this paper proposes a simple algorithm of a discrete wavelet transform (DWT) coupled with one-dimensional convolutional neural networks (1D-CNNs) to classify three classes: Normal Sinus Rhythm (NSR), AF and non-AF (NAF). The experiment was conducted with a combination of three public datasets and one dataset from an Indonesian hospital. The robustness of the proposed model was evaluated based on several validation data with an unseen pattern from 4 datasets. The results indicated that 1D-CNNs outperformed other approaches and achieved satisfactory performances with high generalization ability. The accuracy, sensitivity, specificity, precision, and F1-Score for two classes were 99.98%, 99.91%, 99.91%, 99.99%, and 99.95%, respectively. For the three classes, the accuracy, sensitivity, specificity, precision, and F1-Score was 99.17%, 98.90%, 99.17%, 96.74%, and 97.48%, respectively. Potentially, our approach can aid AF diagnosis in clinics and patient self-monitoring to improve early detection and effective treatment of AF.

### **Methods Used**
- DWT coupled 1D CNN

### **Parameters Classified**
- Normal Sinus Rhythm (NSR)
- AF 
- Non-AF (NAF)

### **Results**
- For AF and NSR
  - DWT alone
  	- Accuracy - 92.97%
  	- Sensitivity	- 87.46%
  	- Specificity - 87.46%
  	- Precision - 71.78%
  	- F1-Score - 81.63%
  - DWT + 10 fold (Class Imbalance)
  	- Accuracy - 99.98%
  	- Sensitivity	- 99.91%
  	- Specificity	- 99.91%
  	- Precision	- 99.99%
  	- F1-Score	- 99.95%		
- For AF, NSR and NAF
  - DWT + 10 fold
  	- Accuracy	- 99.17%
  	- Sensitivity	- 98.90%
  	- Specificity	- 99.17%
  	- Precision	- 96.74%
  	- F1-Score - 97.48%
(It has also results of other class imbalance techniques. This is the best result)

## Reliable PPG-based algorithm in atrial fibrillation detection

### **Abstract**
Atrial Fibrillation (AF) is the most common type of arrhythmia. Since AF is a risk factor for stroke, automatic detection of AF is an important public health issue. Currently, the most useful and accurate tool for diagnosing AF is electrocardiography (EKG). On the other hand, PPG-based AF detection desires exploration. Photoplethysmogram (PPG) is an alternative technique to obtain the heart rate information by pulse oximetry. Convenience makes PPG promising in identifying arrhythmia like AF. The aim of this study is to investigate the potential of analyzing PPG waveforms to identify patients with AF. With the extracted features from multiple parameters, including interval and amplitude of PPG signals, patients were classified into AF and non-AF by support vector machine (SVM). The receiver operating characteristic curve (ROC) and statistical measures were applied to evaluate model performances. Among 468 patients' signals recorded in clinic environments, we achieve ROC area under curve, sensitivity and accuracy of 0.971, 0.942, and 0.957, respectively. The result suggests that the PPG-based AF detection algorithm is a promising pre-screening tool to help doctors monitoring patient with arrhythmia.

### **Methods Used**
- ANOVA(feature extraction)
- SVM

### **Parameters Classified**
- Amplitude of PPG signal
- Interval of PPG signal    

### **Results**
- Sensitivity - 0.942
- Specificity - 0.962
- Accuracy - 0.957

## K-margin-based Residual-Convolution-Recurrent Neural Network for Atrial Fibrillation Detection

### **Abstract**
Atrial Fibrillation (AF) is an abnormal heart rhythm which can trigger cardiac arrest and sudden death. Nevertheless, its interpretation is mostly done by medical experts due to high error rates of computerized interpretation. One study found that only about 66% of AF were correctly recognized from noisy ECGs. This is in part due to insufficient training data, class skewness, as well as semantical ambiguities caused by noisy segments in an ECG record. In this paper, we propose a K-margin-based Residual-Convolution-Recurrent neural network (K-margin-based RCR-net) for AF detection from noisy ECGs. In detail, a skewness-driven dynamic augmentation method is employed to handle the problems of data inadequacy and class imbalance. A novel RCR-net is proposed to automatically extract both long-term rhythm-level and local heartbeat-level characters. Finally, we present a K-margin-based diagnosis model to automatically focus on the most important parts of an ECG record and handle noise by naturally exploiting expected consistency among the segments associated for each record. The experimental results demonstrate that the proposed method with 0.8125 F1NAOP score outperforms all state-of-the-art deep learning methods for AF detection task by 6.8%.

### **Methods Used**
- K-margin-based Residual-Convolution-Recurrent neural network
- skewness-driven dynamic augmentation method (Class Imbalance)

### **Parameters Classified**
- Normal sinus rhythm
- Atrial Fibrillation
- Other rhythm
- Too noisy to classify

### **Results**
- F1 score - 0.8125

## Ensemble Learning for Detection of Short Episodes of Atrial Fibrillation

### **Abstract**
Early detection of atrial fibrillation (AF) is of great importance to cardiologists in order to help patients suffer from chronic cardiac arrhythmias. This paper proposes a novel algorithm to detect short episodes of atrial fibrillation (AF) using an ensemble framework. Several features are extracted from long term electrocardiogram (ECG) signals based on the heart rate variability (HRV). The most significant subset of features are selected as inputs to the four classifiers. Outputs of these classifiers are then combined for the final detection of the AF episodes. Results from an extensive analysis of the proposed algorithm show high classification accuracy (around 85 %) and sensitivity (around 92 %) for classifying very short episodes of AF (10 beats per segment, which is approximately 6 seconds). The accuracy and sensitivity of the proposed algorithm are improved significantly to 96.46 % and 94 %, respectively, for slightly longer episodes (60 beats per segment) of AF. Compared to the state-of-the-art algorithms, the proposed method shows the potential to pave the way to extend to real-time AF detection applications.

### **Methods Used**
- Random Forests (RF)
- Support Vector Machine (SVM)
- Adaptive Boosting (Ad-aBoost)
- Group Method of data Handling (GMDH)
- Trained separately using 5-fold cross validation
- Outputs are combined using Dempster-Shafer theory (DST)

### **Parameters Classified**
- RR Intervals
  - Standard Deviation
  - Mean
  - Root Mean Square
  - Normalised Root Mean Square

### **Results**
![Paper1](images/accuracy.jpg)
![Paper1](images/combination.jpg)


# Class Imbalance

## The Effect of Data Augmentation on Classification of Atrial Fibrillation in Short Single-Lead ECG Signals Using Deep Neural Networks

### **Abstract:**
Cardiovascular diseases are the most common cause of mortality worldwide. Detection of atrial fibrillation (AF) in the asymptomatic stage can help prevent strokes. It also improves clinical decision making through the delivery of suitable treatment such as, anticoagulant therapy, in a timely manner. The clinical significance of such early detection of AF in electrocardiogram (ECG) signals has inspired numerous studies in recent years, of which many aim to solve this task by leveraging machine learning algorithms. ECG datasets containing AF samples, however, usually suffer from severe class imbalance, which if unaccounted for, affects the performance of classification algorithms. Data augmentation is a popular solution to tackle this problem. In this study, we investigate the impact of various data augmentation algorithms, e.g., oversampling, Gaussian Mixture Models (GMMs) and Generative Adversarial Networks (GANs), on solving the class imbalance problem. These algorithms are quantitatively and qualitatively evaluated, compared and discussed in detail. The results show that deep learning-based AF signal classification methods benefit more from data augmentation using GANs and GMMs, than oversampling. Furthermore, the GAN results in circa 3% better AF classification accuracy in average while performing comparably to the GMM in terms of f1-score.

### **Models Used:** 
- oversampling
- Gaussian Mixture Models (GMMs)
- Deep Convolutional Generative Adversarial Networks (DCGAN)
  
### **Result:** 
Oversampling < GMM < DCGAN

## Handling Class Overlap and Imbalance to Detect Prompt Situations in Smart Homes

### **Abstract:**
The class imbalance problem is a well-known classification challenge in machine learning that has vexed researchers for over a decade. Under-representation of one or more of the target classes (minority class(es)) as compared to others (majority class(es)) can restrict the application of conventional classifiers directly on the data. In addition, emerging challenges such as overlapping classes, make class imbalance even harder to solve. Class overlap is caused due to ambiguous regions in the data where the prior probability of two or more classes are approximately equal. We are motivated to address the challenge of class overlap in the presence of imbalanced classes by a problem in pervasive computing. Specifically, we are designing smart environments that perform health monitoring and assistance. Our solution, ClusBUS, is a clustering-based under sampling technique that identifies data regions where minority class samples are embedded deep inside majority class. By removing majority class samples from these regions, ClusBUS preprocesses the data in order to give more importance to the minority class during classification. Experiments show that ClusBUS achieves improved performance over an existing method for handling class imbalance.

### **Models Used:** 
- Clustering-based Under-sampling (ClusBus)
- SMOTE
  
### **Result:** 
ClusBus > SMOTE

___

## Robust detection of atrial fibrillation from short-term electrocardiogram using convolutional neural networks

### **This paper is explained above**

## Automatic detection of arrhythmia from imbalanced ECG database using CNN model with SMOTE

### **Abstract:**
Timely prediction of cardiovascular diseases with the help of a computer-aided diagnosis system minimizes the mortality rate of cardiac disease patients. Cardiac arrhythmia detection is one of the most challenging tasks, because the variations of electrocardiogram(ECG) signal are very small, which cannot be detected by human eyes. In this study, an 11-layer deep convolutional neural network model is proposed for classification of the MIT-BIH arrhythmia database into five classes according to the ANSI–AAMI standards. In this CNN model, we designed a complete end-to-end structure of the classification method and applied without the denoising process of the database. The major advantage of the new methodology proposed is that the number of classifications will reduce and also the need to detect, and segment the QRS complexes, obviated. This MIT-BIH database has been artificially oversampled to handle the minority classes, class imbalance problem using SMOTE technique. This new CNN model was trained on the augmented ECG database and tested on the real dataset. The experimental results portray that the developed CNN model has better performance in terms of precision, recall, F-score, and overall accuracy as compared to the work mentioned in the literatures. These results also indicate that the best performance accuracy of 98.30% is obtained in the 70:30 train-test data set.

### **Models Used:** 
- SMOTE

### **Result:** 
- Accuracy - 98.3%
  
## Classification of imbalanced ECG beats using re-sampling techniques and AdaBoost ensemble classifier

### **Abstract:**
Computer-aided heartbeat classification has a significant role in the diagnosis of cardiac dysfunction. Electrocardiogram (ECG) provides vital information about the heartbeats. In this work, we propose a method for classifying five groups of heartbeats recommended by AAMI standard EC57:1998. Considering the nature of ECG signal, we employed a non-stationary and nonlinear decomposition technique termed as improved complete ensemble empirical mode decomposition (ICEEMD). Later, higher order statistics and sample entropy measures are computed from the intrinsic mode functions (IMFs) obtained from ICEEMD on each ECG segment. Furthermore, three data level pre-processing techniques are performed on the extracted feature set, to balance the distribution of heartbeat classes. Finally, these features fed to AdaBoost ensemble classifier for discriminating the heartbeats. Simulation results show that the proposed method provides a better solution to the class imbalance problem in heartbeat classification.

### **Models Used:** 
- Imbalance (Steps)
  - Re-sampling
  - Synthetic minority oversampling technique (SMOTE)
  - Distribution based data sampling
- ML techniques
  - AdaBoost ensemble classifier (reduce error rate)
  - SVM
  - LDA
  - k-NN

### **Parameters Classified**
- Non-ectopic beats
- Supra Ventricular ectopic beats
- Ventricular ectopic beats
- Fusion beats
- Unknown beats
  
### **Result:** 
- Imbalance: Accuracy - 98.3%
![Paper1](images/ML_techniques.jpg)


## Dealing with Class Imbalance in Data

1. SMOTE oversampling - Minority class is oversampled along with majority undersampling to increase the number of instances of that class. 
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
- [Automatic detection of arrhythmia from imbalanced ECG database using CNN model with SMOTE](https://link.springer.com/article/10.1007/s13246-019-00815-9)
- [Classification of imbalanced ECG beats using re-sampling techniques and AdaBoost ensemble classifier](https://www.sciencedirect.com/science/article/pii/S1746809417302872)