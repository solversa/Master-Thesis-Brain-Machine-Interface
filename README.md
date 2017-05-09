# Master Thesis: Brain Machine Interface

## Task: Decoding of 3D Imaginary Reach and Grasp Movements from Non-invasive EEG Signals using Spiking Neural Networks on SpiNNaker Neuromorphic Hardware

For the task of decoding the EEG signals a generic multivariate classifier based on a spiking neural network model abstracted from the insect olafactory system (particular the antenna lobe AL) is used.
The model in this work is solely trained and used on the SpiNNaker neuromorphic platform which restricts the implementation of the STDP algorithm used for learning [http://apt.cs.manchester.ac.uk/projects/SpiNNaker/].

![alt tag](http://www.frontiersin.org/files/Articles/164125/fnins-09-00491-HTML/image_m/fnins-09-00491-g001.jpg)

[http://journal.frontiersin.org/article/10.3389/fnins.2015.00491/full]

### Outline:
#### Step 1: SNN for Iris data set
We implement a spiking neural network (SNN) with a Spike-Time-Dependent Plasticity  (STDP) learning algorithm to classify a binary version of the iris data set. 
Since the Iris data set is proven to be easy to classify we can check if our implementation of the SNN and STDP works. 
Since we didn't manage to achieve consistant calssification results on the iris dataset we are trying different changes in architecture and coding:
- Remove (some) randomness of the network
- Time coding instead of population coding 
- Homeostasis: Since its tricky to use STDP in an unbalanced network we multiply the weights between every training epoch by a number between 0 and 1. This should lead to the convergence of the network to a stable solution.
- Add delay to the inputs reversely proportional to the feature values

#### Step 2: EEG Feature Extraction
There are several ways for extracting features from raw EEG data. We chose to first use a simple method by calculating the power of the alpha sub bands (8-10Hz, 9-11Hz, 10-12Hz, 11-13Hz, 12-14Hz) for each epoch of imaginary movement. It is planned to later test the wavelet transform or use the Event Related Desynchronization ERD[%] and the Event Related Synchronization ERS[%] values for the alpha and beta bands respectively as features.
