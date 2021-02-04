import numpy as np
import matplotlib.pyplot as plt

experimentalData = np.loadtxt('nuclear_data.txt', usecols=(0,1,3))
aidansData = np.loadtxt('aidansNuclearData.txt')

plt.scatter(experimentalData[:,0], experimentalData[:,2], marker='v', color='black', s=.1)
plt.scatter(aidansData[:,0], aidansData[:,2], marker='v', color='blue', s=.1)

plt.title('Aidans Data = Blue')
plt.xlabel('Atomic Mass Number')
plt.ylabel('Binding Energy Per Nucleon')

plt.show()