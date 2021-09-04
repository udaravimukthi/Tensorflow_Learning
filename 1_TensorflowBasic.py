import os

# to remove the additonal details 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

print(tf.__version__)

#tensor
# for integer
tensorA =tf.constant(8)
print(tensorA)

#for floating point
tensorA =tf.constant(8.0)
print(tensorA)

# for matrix type
tensorA =tf.constant([[10,20,30],[40,50,60]], shape=(3,2))
print(tensorA)

#ones matrix
tensorA =tf.ones((4,4))
print(tensorA)