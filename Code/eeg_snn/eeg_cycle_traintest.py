import os
import sys
import time
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import eeg_clf_test_snn
import eeg_clf_train_snn


def multiply_weights():
    # w: np.array containing the weights
    n_cl = 2
    for i in range(n_cl):
        cl_weights = np.load("output_files/stdp_weights{}.npy".format(i))
        cl_weights *= 0.9
        np.save("output_files/stdp_weights{}.npy".format(i), cl_weights)


def PCA_dim_red(X, var_desired=0.95):
    """
    Dimensionality reduction using PCA
    X:            matrix (2d np.array)
    var_desired:  desired preserved variance

    Returns X with reduced dimesnions
    """
    # PCA
    pca = PCA(n_components=X.shape[1]-1)
    pca.fit(X)
    print('pca.explained_variance_ratio_:\n',pca.explained_variance_ratio_)    
    var_sum = pca.explained_variance_ratio_.sum()
    var = 0
    for n, v in enumerate(pca.explained_variance_ratio_):
        var += v
        if var / var_sum >= var_desired:
            print("Reached Variance: {:1.3f}".format(var/var_sum))
            return PCA(n_components=n+1).fit_transform(X)


def cross_val(k):
    """ 
    load data and split corresponding to k-fold cross validation
    """
    experiment_number = 0    # select experiment dataset
    path = '/home/rychly/Dropbox/[TUM]/4. WiSe 1617/Masterarbeit/code/eeg_feature_extraction'
    # Load data
    X = np.load(path + '/Feat_mat_erp_'+ str(experiment_number) +'.npy')
    y = np.load(path + '/Feat_label_erp_'+ str(experiment_number) +'.npy')
    # Shift to zero mean and normalize y
    y = y-1
    # Normalize X and reduce dimensions
    X = normalize(X)
    X = PCA_dim_red(X)
    # Split data
    idx_arr = np.arange(len(y)) 
    np.random.shuffle(idx_arr)
    idx_arr_split = np.array_split(idx_arr, k)
    X_i_list = []
    y_i_list = []
    for idx_part in idx_arr_split:
        X_i_list.append(X[idx_part])
        y_i_list.append(y[idx_part])
    return X_i_list, y_i_list



# --- INITIALISATION -----------------------------------------------------------

# Check number of cycles
try:
    n_cycles = int(sys.argv[1])
except:
    n_cycles = 1    
print("\n {} Cycle(s)! \n".format(n_cycles))


# --- SIMULATION ---------------------------------------------------------------

cross_validation  = True
cross_val_k = 10

# Simulation Parameter          BEST RESULTS => mean: 0.67, std.dev.: 0.058
homeostasis       = False         # True
epochs            = 1             # 1
# Network Parameter         
trial_num         = 90#76         # 90
randomness        = True          # True
rand_data         = False         # False
reverse_src_del   = False         # False
# STDP Parameter            
tau_pl            = 5.            # 5.


### Run Train and Test Scripts n_cycles times
print('Training network ... ')
rates = []
##
## Cross Validation
##
if cross_validation == True:
    X_i_list, y_i_list = cross_val(cross_val_k)
    for k in range(cross_val_k):
        # init training sets
        if k == 0:
            inserted = 1
            X_train = X_i_list[1]
            y_train = y_i_list[1]
        else:
            inserted = 0
            X_train = X_i_list[0]
            y_train = y_i_list[0]
        # add rest to training set
        for i in range(cross_val_k):
            if i != k and i != inserted:
                X_train = np.concatenate((X_train, X_i_list[i]), axis=0)
                y_train = np.concatenate((y_train, y_i_list[i]), axis=0)
        # create test sets
        X_test = X_i_list[k]
        y_test = y_i_list[k]
        # Set training parameter
        trial_num = len(X_train)
        # Train
        eeg_clf_train_snn.train_snn(n_training      = 4, 
                                    data            = X_train,
                                    cls             = y_train,
                                    use_old_weights = False,
                                    randomness      = randomness,
                                    tau_pl          = tau_pl,
                                    rand_data       = rand_data,
                                    trial_num       = trial_num,
                                    reverse_src_del = reverse_src_del)
        # Test
        print('Testing network ... ')
        rates.append(eeg_clf_test_snn.test_snn(randomness = True,
                                               data = X_test,
                                               cls = y_test))
        print("Cross Val k={}, CLF Rate = {}".format(k+1, rates[-1]))


##
##  Normal Training (if NOT cross validation)
##
else:
    for c in range(n_cycles):
        eeg_clf_train_snn.train_snn(n_training      = 4,  # 4 
                                    use_old_weights = False,
                                    randomness      = randomness,
                                    tau_pl          = tau_pl,
                                    rand_data       = rand_data,
                                    trial_num       = trial_num,
                                    reverse_src_del = reverse_src_del)
        for _ in range(epochs - 1):
            if homeostasis == True:
                multiply_weights()
            eeg_clf_train_snn.train_snn(n_training      = 1,
                                        use_old_weights = True,
                                        randomness      = randomness,
                                        tau_pl          = tau_pl,
                                        rand_data       = rand_data,
                                        trial_num       = trial_num,
                                        reverse_src_del = reverse_src_del)
        # Wait 2 sec
        t_sleep = 1    # in seconds
        print('Waiting {} seconds ... '.format(t_sleep))
        time.sleep(t_sleep)
        ### Test network
        print('Testing network ... ')
        rates.append(eeg_clf_test_snn.test_snn(randomness=True))
        print("Cycle {}, CLF Rate = {}".format(c+1, rates[-1]))

        # stop training if clf rate is high enough
        rate_tresh = 0.7
        #if rates[-1] > rate_tresh:
        #   break


# Save clf rates
np.save("output_files/clf_rates.npy", rates)

# Print results
if n_cycles > 1:
    print("Results ({} cylces): Mean CLF-Rate = {}, with std.dev = {}".format(
        c+1, np.mean(rates), np.std(rates)))

