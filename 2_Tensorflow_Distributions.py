import os

# to remove the additonal details 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

#normal distribution
x = tf.random.normal((4,4), mean=0, stddev=1)
print("Normal distribution")
print(x)

# uniform distribution
x = tf.random.uniform((4,4), minval= 0, maxval= 2)
print("Uniform distribution")
print(x)

# range function
x = tf.range(start=5, limit=20, delta=3)
print("Range Function")
print(x)

#casting
y = tf.cast(x, dtype= tf.float64)
print("casting")
print(y)