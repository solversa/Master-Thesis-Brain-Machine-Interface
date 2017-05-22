Master Thesis: Brain Machine Interface
======================================

## Task: Decoding of 3D Imaginary Reach and Grasp Movements from Non-invasive EEG Signals using Spiking Neural Networks on SpiNNaker Neuromorphic Hardware

For the task of decoding the EEG signals a generic multivariate classifier based on a spiking neural network model abstracted from the insect olafactory system (particular the antenna lobe AL) is used.
The model in this work is solely trained and used on the SpiNNaker neuromorphic platform which restricts the implementation of the STDP algorithm used for learning [http://apt.cs.manchester.ac.uk/projects/SpiNNaker/].

![alt tag](http://www.frontiersin.org/files/Articles/164125/fnins-09-00491-HTML/image_m/fnins-09-00491-g001.jpg)

[http://journal.frontiersin.org/article/10.3389/fnins.2015.00491/full]


### UPDATES:
I presented my results on the 22.05.17. The slides can be seen in the folder 'Report_Midterm'

### Spiking Neural Network
--------------------------

####learning the Iris data set
We implement a spiking neural network (SNN) with a Spike-Time-Dependent Plasticity  (STDP) learning algorithm to classify a binary version of the iris data set. 
Since the Iris data set is proven to be easy to classify we can check if our implementation of the SNN and STDP works.

=> Results: We manage to achieve ~100% classification rate on the iris data set!

#### Classifying EEG data with the SNN
Since we showed our network is able to learn (on the iris data set) and STDP works we tried using it to classify imaginary movements from EEG data. For that we use the feature matrices created from the raw EEG data.

=> Results: Our highest reached average accuracy is 68% (over 100 Training and test cycles with the following parameters:
- Network Parameter:
epochs = 1 (n_training = 4)
trial_num = 90 (training with full training set, test with remaining 12 samples)
rand (network randomnes) = on
- Neuron Parameter:
tau_pl = 5. 
stdp_w_max = 0.4
stdp_w_min = 0.0
stdp_A_pl = 0.02

To further improve the network's accuracy the following approaches are (or will be tested):
- Homeostasis:	a system's self regularization to keep some of it's property in balance. In this case to converge to a stable output.
For this we multiply all weights by a constant (homeostasis_multiplier) after training the network on only a small sub-batch of the training set. This is repeated until convergence of the output or saturation of the weights.
Results: We could not increase the accuracy constantly with this method and always fell short a few percent points of our highest reached accuracy before.
- Time Coding
Until now we use population coding to create spikes from the calculated feature values. In the next weeks we want to implement time coding (and a combination of population and time coding) to hopefully increase the network's accuracy.


### Feature Extraction
----------------------

There are several ways for extracting features from raw EEG data. We chose the following (and plan to further implement a wavelet transfrom fro feature extraction)

#### Features: Bandpower of alpha and beta sub band 
Creating features by calculating the power of the alpha sub bands (8-10Hz, 9-11Hz, 10-12Hz, 11-13Hz, 12-14Hz) for each epoch of imaginary movement. 
![alt text](https://github.com/LeRyc/Master-Thesis-Brain-Machine-Interface/blob/master/readme_img/feat_extract_subbands.png)


### Features: Event-Related Synchronization (ERS) and Desynchronization (ERD)
The highest classification accuracy with statistical machine learning algorithms and the spiking neural network is achieved with the ERS and ERD features.
![alt text](https://github.com/LeRyc/Master-Thesis-Brain-Machine-Interface/blob/master/readme_img/feat_extract_ersd.png)






