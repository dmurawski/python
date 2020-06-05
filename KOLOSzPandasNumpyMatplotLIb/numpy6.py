import numpy as np 

maceirz55 = np.zeros((5,5),dtype='str')
print(maceirz55)
wyraz1 = np.array(list('pilot'))
wyraz2 = np.array(list('ptak'))
wyraz3 = np.array(list('tomek'))
np.put(maceirz55, range(0,5),wyraz1)
np.put(maceirz55, range(0,20,5),wyraz2)
np.put(maceirz55,[4,8,12,16,20],wyraz3)

print(maceirz55)