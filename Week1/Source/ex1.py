#Import tensorflow libraries
import tensorflow as tf

#Create three matrices to perform evaluation of (a^2+b)*c
#Creates 2x2 matrices
Matrix_one = tf.constant([[2,3],[3,4]])
Matrix_two = tf.constant([[2,3],[3,4]])
Matrix_three = tf.constant([[5,7],[1,3]])

#we use square method to square Matrix_one and result is added to Matrix_two and stored in the variable add

add = tf.add(tf.square(Matrix_one),Matrix_two)

#We then multiply varibale add with Matrix_three to get final result which is stored in final variable
final = tf.matmul(add,Matrix_three)
#b = tf.pow(Matrix_one,2)

#we create a session object which will let us execute and evaluate object and finally close the session once our work is completed
with tf.Session() as sess:
    #Print the result
    print("Final Output of expression:(a^2+b)*c\n",sess.run(final))













    # fun = (tf.square(Matrix_one))+(Matrix_two)
    # print(sess.run(fun))
    # print(sess.run(add))