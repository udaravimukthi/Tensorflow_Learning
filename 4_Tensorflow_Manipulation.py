import os

# to remove the additonal details 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

x = tf.constant([0,10,4,7,7,8,9,1])
print("Printing tensor")
print(x)

print("x[1:]")
print(x[1:])

print("x[2:6]")
print(x[2:6])

#skiping values
print("x[::2]")
print(x[::2])

#reverse order
print("reverse ordeer")
print(x[::-1])

#indices(beda wen krla kotasak geneema)
print("Indicies")
indicesIndexes = tf.constant([0,3])
print(indicesIndexes)

indexedTensor = tf.gather(x, indices= indicesIndexes)
print(indexedTensor)

#another tecquinqe
y = tf.constant([[10,20],[30,40],[50,60],[70,80]])
print("Printing new tensor y")
print(y)

#get first row with all elements
print("y[0]")
print(y[0])

print("y[0,:2]")
print(y[0,:2])

print("y[0,:1]")
print(y[0,:1])

#first 2 rows an 1 colomn
print("first 2 rows")
print(y[0:2,:1])

#first 3 rows with 1 colomn
print("first three rows with 1st colmmn")
print(y[:3,:1])

print("testing 1")
print(y[0,:1])

print("testing 2")
print(y[0,1])

print("testing 3")
print(y[2:,1])
#reshaping
print("Reshaping")
tensorA = tf.range(16)
print("1.tensor")
print(tensorA)
print("2.reshape")
x = tf.reshape(tensorA, (2,8))
print(x)

x = tf.reshape(tensorA, (16,1))
print(x)