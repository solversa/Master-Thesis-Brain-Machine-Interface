Master Thesis: Brain Machine Interface
======================================

## Task: Decoding of 3D Imaginary Reach and Grasp Movements from Non-invasive EEG Signals using Spiking Neural Networks on SpiNNaker Neuromorphic Hardware

For the task of decoding the EEG signals a generic multivariate classifier based on a spiking neural network model abstracted from the insect Olfactory system (particular the antenna lobe AL) is used.
The model in this work is solely trained and used on the SpiNNaker neuromorphic platform which restricts the implementation of the STDP algorithm used for learning [http://apt.cs.manchester.ac.uk/projects/SpiNNaker/].

![alt tag](http://www.frontiersin.org/files/Articles/164125/fnins-09-00491-HTML/image_m/fnins-09-00491-g001.jpg)

[http://journal.frontiersin.org/article/10.3389/fnins.2015.00491/full]


### UPDATES:
I presented my results on the 22.05.17. The slides can be seen in the folder 'Report_Midterm'



--------------------------
## Spiking Neural Network

### Iris data set
We implemented a spiking neural network (SNN) with a Spike-Time-Dependent Plasticity  (STDP) learning algorithm to classify a binary version of the iris data set. 
Since the Iris data set is proven to be easy to classify we can check if our implementation of the SNN and STDP works.

=> ***Results***: We manage to achieve ~100% classification rate on the iris data set!

### Classifying EEG data with the SNN
Since we showed our network is able to learn (on the iris data set) and STDP works we tried using it to classify imaginary movements from EEG data. For that we use the feature matrices created from the raw EEG data.

=> Results: Our highest reached average accuracy is ~68% (over 100 Training and test cycles with the following parameters:
- Network Parameter:
epochs=1 (n_training = 4),
trial_num=90 (training with full training set, test with remaining 12 samples),
rand (network randomness)=on
- Neuron Parameter:
tau_pl=5.,
stdp_w_max=0.4,
stdp_w_min=0.0,
stdp_A_pl=0.02

To further improve the network's accuracy the following approaches are (or will be tested):
- Homeostasis:	a system's self regularization to keep some of it's property in balance. In this case to converge to a stable output.
For this we multiply all weights by a constant (homeostasis_multiplier) after training the network on only a small sub-batch of the training set. This is repeated until convergence of the output or saturation of the weights.
Results: We could not increase the accuracy constantly with this method and always fell short a few percent points of our highest reached accuracy before.
- Time Coding
Until now we use population coding to create spikes from the calculated feature values. In the next weeks we want to implement time coding (and a combination of population and time coding) to hopefully increase the network's accuracy.



----------------------
## Feature Extraction

There are several ways for extracting features from raw EEG data. We chose the following (and plan to further implement a wavelet transform fro feature extraction)

### Features: Band power of alpha and beta sub band 
Creating features by calculating the power of the alpha sub bands for each epoch of imaginary movement. 
![alt text](https://github.com/LeRyc/Master-Thesis-Brain-Machine-Interface/blob/master/readme_img/feat_extract_subbands.png)


## Features: Event-Related Synchronization (ERS) and De-synchronization (ERD)
ERD and ERS are brain oscillatory acitivity in diverse frequency bands. With threse
![alt text](https://github.com/LeRyc/Master-Thesis-Brain-Machine-Interface/blob/master/readme_img/feat_extract_ersd.png)

### ERD/ERS quantification (Alternative method for computation of ERD and ERS)

Bootstrap-based method to calculate to show a time-frequency map with signnificant changes of ERD or ERS for specific electrodes. In
<br />
<br />
[Source: Meng J, Zhang S, Bekyo A, Olsoe J, Baxter B, He B (2016) Noninvasive electroencephalogram based control of a robotic arm for reach and grasp tasks. Scientific Reports 6: 38565. http://dx.doi.org/10.1038/srep38565]

--------------------------
## Further Approaches 
* #### CROSS-TRIAL ENCODING: 
Instead of trying to simply reconstruct the input trial, the CAE now had to reconstruct a different trial belonging to the same class.9 This strategy can be considered as a special case of the generalized framework for auto-encoders proposed by Wang et al. (2014).10 Given nC trials for a class C , n2C or nC (nC − 1) pairs of input and target trials can be formed depending on whether pairs with identical trials are included. This increases the number of training examples by a factor depending on the partitioning of the dataset with respect to the different classes. As for the basic auto-encoding scheme, the training objective is to minimize a reconstruction error. In this sense, it is unsupervised training but the trials are paired for training using knowledge about their class labels. We found that using the distance based on the dot product worked best as reconstruction error.
<br />
<br />
[Source: Sebastian Stober, Avital Sternin, Adrian M. Owen & Jessica A. Grahn (2016),
DEEP FEATURE LEARNING FOR EEG RECORDINGS, https://arxiv.org/pdf/1511.04306.pdf]

--------------------------
## Data Acquisition 
As soon as the new G-Tech amplifier for recording EEG signals is available in our lab we will record and work on our own data sets.
Feature matrices are created from recording session session that typically contain 120 trials:
![alt text](https://github.com/LeRyc/Master-Thesis-Brain-Machine-Interface/blob/master/readme_img/eeg_recording_trial.png)


--------------------------
## Outline of Thesis

* ### Introduction
	- Use of BCIs
	- BCI Basics

* ### Thesis Statement
	- The use of Spiking Neural Networks for the decoding of EEG signals could potentially greatly improve the classification accuracies.

* ### Approach
	- Use already existing Spiking Neural Network classifier that is abstracted from the insect Olfactory system.
	- Modify the network to use STDP for learning in it's last layer of weights
	  (prove that STDP is generally working by successfully classifying Iris dataset)
	- Modify network to classify features created from EEG signals

* ### Conclusion
	- EEG is f****** hard to classify



