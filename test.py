import tensorflow as tf

sess = tf.Session()
with sess.as_default():
    tensor = tf.range(10)
    print_op = tf.print([tensor])
    with tf.control_dependencies([print_op]):
        tripled_tensor = tensor * 3

sess.run(tripled_tensor)


a = tf.constant([[1, 2, 3, 4], [2, 3, 4, 4], [3, 4, 5, 4]])
mask_i = tf.constant([1, 0, 1])
mask = mask_i > 0
print(sess.run(mask))
b = tf.where(mask, a, tf.zeros(tf.shape(a), dtype=tf.int32))

print(sess.run(b))



mask_re = tf.expand_dims(mask_i, 1)
print(sess.run(tf.multiply(mask_re, a)))
print(sess.run(mask_re * a))