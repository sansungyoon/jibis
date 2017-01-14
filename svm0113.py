import dataTransform
import numpy as np
import time

start = time.clock()

from sklearn.svm import SVC
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

C_range = np.logspace(-2, 10, 13)
gamma_range = np.logspace(-9, 3, 13)

param_grid = dict(gamma=gamma_range, C=C_range)

cv = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=None)

grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
grid.fit(dataTransform.X, dataTransform.y)

end = time.clock()

print('The best parameters are %s with a score of %0.2f' % (grid.best_params_, grid.best_score_))
print"time Taken (" + str(end-start) + ")sec"
