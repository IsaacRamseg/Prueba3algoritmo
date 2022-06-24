#https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/#usage1
#https://numpy.org/doc/stable/reference/generated/numpy.ravel.html
import numpy as np
def asientos():
    avion=np.array(range(1,43),dtype='str')
    avion=avion.reshape(7,6)
    print(avion)

asientos()