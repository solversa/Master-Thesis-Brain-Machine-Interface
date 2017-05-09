import os
import sys
import time
import numpy as np
import iris_clf_test_snn
import iris_clf_train_snn

homeostasis = True
homeostasis_epochs = 1    # epochs with homeostasis

def multiply_weights():
	# w: np.array containing the weights
	n_cl = 2
	for i in range(n_cl):
		cl_weights = np.load("output_files/stdp_weights{}.npy".format(i))
		cl_weights *= 0.5
		np.save("output_files/stdp_weights{}.npy".format(i), cl_weights)


# Check number of cycles
try:
	n_cycles = int(sys.argv[1])
except:
	n_cycles = 1	
print("\n {} Cycle(s)! \n".format(n_cycles))


# Run Train and Test Scripts n_cycles times
rates = []
for c in range(n_cycles):

	print('Training network ... ')
	if homeostasis == False:
	### Normal Training Run
		iris_clf_train_snn.train_snn(homeostasis = False, 
									 n_training  = 2,
									 randomness  = False)

	### Homeostasis Training Run
	else: 
		iris_clf_train_snn.train_snn(homeostasis = False,
								 	 n_training  = 1,
								 	 randomness  = False,
								 	 tau_pl      = 0.3,    # (0.2 - 0.3 works))
								 	 stdp_w_max  = 0.4)
		for _ in range(homeostasis_epochs):
			multiply_weights()
			iris_clf_train_snn.train_snn(homeostasis = True,
										 n_training  = 1,
										 randomness  = False)

	# Wait 2 sec
	t_sleep = 1    # in seconds
	print('Waiting {} seconds ... '.format(t_sleep))
	time.sleep(t_sleep)

	### Test network
	print('Training network ... ')
	rates.append(iris_clf_test_snn.test_snn(randomness = True))
	print("Cycle {}, CLF Rate = {}".format(c+1, rates[-1]))


# Save clf rates
np.save("output_files/clf_rates.npy", rates)

# Print results
if n_cycles > 1:
	print("Results ({} cylces): Mean CLF-Rate = {}, with std.dev = {}".format(
		n_cycles, np.mean(rates), np.std(rates)))

