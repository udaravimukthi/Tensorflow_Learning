from os import terminal_size
import tensorflow as tf

#element wise addion
tensorA = tf.constant([10,20,30])
tensorB = tf.constant([40,55,71])

print(tensorA)
print(tensorB)

print("tensor Additon")
tensorC = tf.add(tensorA, tensorB)
print(tensorC)
tensorD = tensorA + tensorB
print(tensorD)

print("tensor substraction")
tensorD= tensorA- tensorB
print(tensorD)
tensorE = tf.subtract(tensorA, tensorB)
print(tensorE)

print("tensor division")
tensorF = tensorA/ tensorB
print(tensorF)
tensorG = tf.divide(tensorA, tensorB)
print(tensorG)

print("tensor multplication")
tensorH = tf.multiply(tensorA, tensorB)
print(tensorH)

# dot product
print("DOT PRODUCT")
import numpy as np

tensorA = tf.constant(np.array([[1,2],[3,4]]))
tensorB = tf.constant(np.array([[5,4],[8,7]]))

print("tensorA")
print(tensorA)
print("tensorB")
print(tensorB)

tensorC =tf.tensordot(tensorA, tensorB, axes=1)
print(tensorC)