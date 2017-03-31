import numpy as np
import pandas as pd

data = pd.read_csv("iris.csv")

### Shuffle data
data_shuffle = data.values
np.random.shuffle(data_shuffle)

### Split data
# y = data.pop('Species')
# data.pop('Id')
# X = data
y = data_shuffle.T[5]
X = np.delete(data_shuff, 5, axis=1)

### create numerical labels
label_list = list(set(y))
y_numeric = np.zeros(len(y))
for i, label in enumerate(y):
	y_numeric[i] = label_list.index(label)

### cut class 2
class_cut = 2
c2_idx_list = np.where(y_numeric == class_cut)
X_2class = np.delete(X, c2_idx_list, axis=0)    # row: axis=0, col axis=1
y_2class = np.delete(y_numeric, c2_idx_list)

# get test set
c0_idx_list = np.where(y_2class == 0)
c1_idx_list = np.where(y_2class == 1)
X_test_c0 = X_2class[c0_idx_list][:5]
y_test_c0 = y_2class[c0_idx_list][:5]
X_test_c1 = X_2class[c1_idx_list][:5]
y_test_c1 = y_2class[c1_idx_list][:5]
X_test = np.vstack((X_test_c0, X_test_c1))
y_test = np.hstack((y_test_c0, y_test_c1))
# remove test data from training data
X_train = np.delete(X_2class, 
					np.vstack((c0_idx_list[0][:5],c1_idx_list[0][:5])), 
					axis=0) 
y_train = np.delete(y_2class, 
					np.vstack((c0_idx_list[0][:5],c1_idx_list[0][:5]))) 

### save stuff
# np.save('iris_X_2class_train.npy', X_2class)
# np.save('iris_X_2class_test.npy', X_2class)
# np.save('iris_y_2class_train.npy', y_2class)
# np.save('iris_y_2class_test.npy', y_2class)

