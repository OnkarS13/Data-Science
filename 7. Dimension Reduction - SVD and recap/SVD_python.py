# Singular-value decomposition
import numpy as np
from numpy import array
from scipy.linalg import svd

# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])

A = array([[1,0,0,0,2], [0,0,3,0,0], [0,0,0,0,0], [0,4,0,0,0]])
print(A)

# SVD
U, d, Vt = svd(A)

print(U)
print(d)
print(np.diag(d))
print(Vt)


# Applying SVD on dataset
import pandas as pd
data = pd.read_excel("C:/Data/University_Clustering.xlsx")
data.head()

data = data.iloc[:, 2:]
data.head()

from sklearn.preprocessing import scale 

# Considering only numerical data 
data.data = data

# Normalizing the numerical data 
uni_normal = scale(data)
uni_normal

from sklearn.decomposition import TruncatedSVD
# svd
svd = TruncatedSVD(n_components=3) # n_components means output columns
svd.fit(uni_normal)
result = pd.DataFrame(svd.transform(uni_normal))
result.head()

result.columns = "pc0", "pc1", "pc2"

# Scatter diagram
import matplotlib.pylab as plt
plt.scatter(x = result.pc0, y = result.pc1)
