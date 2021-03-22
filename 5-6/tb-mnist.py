from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("mnist/", one_hot=True)

print(mnist.train.images)
print(len(mnist.train.images))

print(mnist.train.labels)
print(len(mnist.train.labels))

print(len(mnist.train.labels[0]))
print(mnist.train.labels[0])
print(mnist.train.labels[1])
print(mnist.train.labels[2])
print(mnist.train.labels[3])


