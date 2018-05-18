# coding:utf-8


import tensorflow as tf


class TextCNN():
    def __init__(self, vector_length,lable_length):
        self.vector_length=vector_length
        self.lable_length=lable_length
        self.input_x=tf.placeholder(shape=[None,self.vector_length],name='input_x',dtype=tf.float32)
        self.input_y=tf.placeholder(shape=[None,self.lable_length],name='input_y',dtype=tf.float32)
    
    
    def weight(self,shape):
        weight=tf.Variable(initial_value=tf.random_normal(shape,stddev=2.0),name='weight')
        
        return weight
    
    def biases(self,shape):
        biases=tf.Variable(initial_value=tf.random_normal(shape=shape,stddev=1.0),name='biases')
        return biases
    
    def filters(self,shape):
        filters=tf.Variable(initial_value=tf.random_normal(shape,dtype=tf.float32),name='filter')
        return filters
        
    def create_model(self):
        with tf.name_scope('conv'):
            conv=tf.nn.conv2d(self.input_x,filter=self.filters([]))
        
    
    
