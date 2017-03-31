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

data_fname = 'exp_1_raw.fif'
raw = mne.io.read_raw_fif(data_fname).load_data()

# Read and plot a segment of raw data
start, stop = raw.time_as_index([100, 115])  # 100 s to 115 s data segment
data, times = raw[:, start:stop]
# Plot
if 0:
	scalings = 'auto'  # Could also pass a dictionary with some value == 'auto'
	raw.plot(scalings=scalings)





#
# Processing
#
 
### Power Spectral Density
#raw.plot_psd(area_mode='range', tmax=10.0, show=False)




### Induces Power
n_cycles = 2  # number of cycles in Morlet wavelet
freqs = np.arange(8, 14)  # frequencies of interest

power, itc = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles,
                        return_itc=True, decim=3, n_jobs=1)
#power.plot([power.ch_names.index('MEG 1332')])





























