# Master Thesis: Brain Machine Interface

## Task: Decoding of 3D Imaginary Reach and Grasp Movements from Non-invasive EEG Signals using Spiking Neural Networks on SpiNNaker Neuromorphic Hardware

### Outline:
#### Step 1: SNN for Iris data set
Implement a spiking neural network (SNN) with an Spike-Time-Dependent Plasticity  (STDP) learning algorithm to classify a binary version of the iris data set. 
Since the Iris data set is proven to be easy to classify we can check if our implementation of the SNN and STDP works. 

Current State:
Approximately 90% classification rate (Parameters are not finally tuned)

#### Step 2: EEG Feature Extraction
There are several ways for extracting features from raw EEG data. We chose to first use a simple method by calculating the power of the alpha sub bands (8-10Hz, 9-11Hz, 10-12Hz, 11-13Hz, 12-14Hz) for each epoch of imaginary movement. It is planned to later test the wavelet transform or use the Event Related Desynchronization ERD[%] and the Event Related Synchronization ERS[%] values for the alpha and beta bands respectively as features.
