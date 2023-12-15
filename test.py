import numpy as np
t = np.array([[1,2,3,'foo'], [2,3,4,'bar']])

rows, cols = np.where(t == 'bar')
print("Vị trí của 'CDN' là:", rows[0], cols[0])