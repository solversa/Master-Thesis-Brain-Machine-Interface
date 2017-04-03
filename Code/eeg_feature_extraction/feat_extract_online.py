import numpy as np
import mne
import matplotlib.pyplot as plt
from mne.time_frequency import tfr_morlet 

#
# Set Paramter
#
n_trials   = 120
n_pre      = 0
n_post     = 1999
n          = n_pre + n_post + 1
n_channels = 3
freq_s     = 250    # Sampling Frequency



#
# Load Data
#
epo_fname = 'exp_1-epo.fif'
epochs = mne.read_epochs(epo_fname)
epo_arr = epochs.get_data()
def get_data(delta_t):


























