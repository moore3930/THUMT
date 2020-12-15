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






@tf.function
def my_func(step):
    # other model code would go here
    with writer.as_default():
        tf.summary.scalar("my_metric", 0.5, step=step)
        merge_summary = tf.summary.merge([tf.get_collection(tf.GraphKeys.SUMMARIES, "my_metric")])

for step in range(100):
    my_func(step)
    writer = tf.summary.FileWriter("/tmp/mylogs", sess.graph)
    writer.flush()



# with tf.compat.v1.Graph().as_default():
#   step = tf.Variable(0, dtype=tf.int64)
#   step_update = step.assign_add(1)
#   writer = tf.summary.create_file_writer("/tmp/mylogs")
#   with writer.as_default():
#     tf.summary.scalar("my_metric", 0.5, step=step)
#   all_summary_ops = tf.compat.v1.summary.all_v2_summary_ops()
#   writer_flush = writer.flush()
#
#   sess = tf.compat.v1.Session()
#   sess.run([writer.init(), step.initializer])
#   for i in range(100):
#     sess.run(all_summary_ops)
#     sess.run(step_update)
#     sess.run(writer_flush)