#Import tensorflow libraries
import tensorflow as tf

#Create three matrices to perform evaluation of (a^2+b)*c
#Creates 2x2 matrices
a = tf.constant([[2,3],[3,4]])
b = tf.constant([[2,3],[3,4]])
c = tf.constant([[5,7],[1,3]])

#we use square method to square a and result is added to b and stored in the variable add

add = tf.add(tf.square(a),b)

#We then multiply varibale add with c to get final result which is stored in final variable
final = tf.matmul(add,c)
#b = tf.pow(Matrix_one,2)

#we create a session object which will let us execute and evaluate object and finally close the session once our work is completed
with tf.Session() as sess:
    #Print the result
    print("Final Output of expression:(a^2+b)*c\n",sess.run(final))













    # fun = (tf.square(Matrix_one))+(Matrix_two)
    # print(sess.run(fun))
    # print(sess.run(add))