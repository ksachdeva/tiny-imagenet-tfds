import os
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds
from tiny_imagenet import TinyImagenetDataset

# optional
tf.compat.v1.enable_eager_execution()

tiny_imagenet_builder = TinyImagenetDataset()

# this call (download_and_prepare) will trigger the download of the dataset
# and preparation (conversion to tfrecords)
#
# This will be done only once and on next usage tfds will
# use the cached version on your host.
#
# You can pass optional argument to this method called
# DownloadConfig (https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig)
# to customize the location where the dataset is downloaded, extracted and processed.
tiny_imagenet_builder.download_and_prepare()

train_dataset = tiny_imagenet_builder.as_dataset(split="train")
validation_dataset = tiny_imagenet_builder.as_dataset(split="validation")

assert(isinstance(train_dataset, tf.data.Dataset))
assert(isinstance(validation_dataset, tf.data.Dataset))

for a_train_example in train_dataset.take(5):
    image, label, id = a_train_example["image"], a_train_example["label"], a_train_example["id"]
    print(f"Image Shape - {image.shape}")
    print(f"Label - {label.numpy()}")
    print(f"Id - {id.numpy()}")

# print info about the data
print(tiny_imagenet_builder.info)
