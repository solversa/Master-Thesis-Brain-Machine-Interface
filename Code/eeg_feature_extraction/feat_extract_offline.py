import numpy as np
import mne
import matplotlib.pyplot as plt
from mne.time_frequency import tfr_morlet 

mne.set_log_level('WARNING')

#
# Set Paramter
#
n_channels = 3
freq_s     = 250.    # Sampling Frequency


#
# Load Data
#

raw_fname = 'exp_1-raw.fif'
epo_fname = 'exp_1-epo.fif'
#raw = mne.io.read_raw_fif(raw_fname).load_data()
epo = mne.read_epochs(epo_fname).get_data()


#
# Plot Data
#

# Read and plot a segment of raw data
#start, stop = raw.time_as_index([100, 115])  # 100 s to 115 s data segment
#data, times = raw[:, start:stop]
# Plot
#if 0:
#	scalings = 'auto'  # Could also pass a dictionary with some value == 'auto'
#	raw.plot(scalings=scalings)


#
# Processing
#
n_epo = epo.shape[0]
n_chan = epo.shape[1]
n_smpl = epo.shape[2]

### Create new epochs array with bandpassed frequencies
# (n_epochs, n_channels, n_subchannels, n_samples)
if 0:
	# Define frequency bands f[0]=[f_mim_0, f_max_0]
	frq_bnds = np.array([np.arange(8,13),np.arange(10,15)]).T.astype(float)

	# new epochs array: (n_epochs, n_channels, n_subchannels, n_samples)
	epo_filtered = np.zeros((n_epo, n_chan, len(frq_bnds), n_smpl))
	# bandpass filter all channels in each epoch:
	for e, epoch in enumerate(epo):    # for all epochs
		print('\n\n\nEPOCH {} of {} \n\n\n'.format(e, n_epo))
		for c, channel in enumerate(epoch): # for all channels
			for sub_c, freq_range in enumerate(frq_bnds):    # for all sub channels
				epo_filtered[e, c, sub_c, :] = mne.filter.band_pass_filter(
													x=channel, Fs=freq_s, 
													Fp1=freq_range[0], 
													Fp2=freq_range[1])
	np.save('epo_filtered.npy', epo_filtered)

### Calculate Power of all subbands
if 1:
	epo_filtered = np.load('epo_filtered.npy')

if 1:
	n_cycles = 2  # number of cycles in Morlet wavelet
	freqs = np.arange(7, 30, 3)  # frequencies of interest
	from mne.time_frequency import tfr_morlet  # noqa
	power, itc = tfr_morlet(epo_filtered, freqs=freqs, n_cycles=n_cycles,
	                        return_itc=True, decim=3, n_jobs=1)
	#power.plot([power.ch_names.index('MEG 1332')])


































