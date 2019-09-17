from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds
from tiny_imagenet import TinyImagenetDataset

tf.compat.v1.enable_eager_execution()

# checksum_dir = os.path.join(os.path.dirname(__file__), 'checksums/')
# checksum_dir = os.path.normpath(checksum_dir)
# tfds.download.add_checksums_dir(checksum_dir)

tiny_imagenet_builder = TinyImagenetDataset()
print(tiny_imagenet_builder.info)

tiny_imagenet_builder.download_and_prepare(
    download_config=tfds.download.DownloadConfig(register_checksums=True))

tiny_imagenet_train = tiny_imagenet_builder.as_dataset(split="validation")

for an_example in tiny_imagenet_train.take(5):
    image, label, id = an_example["image"], an_example["label"], an_example["id"]

    # plt.imshow(image.numpy().astype(np.float32))
    print(f"{image.shape}")

    bgr = cv2.cvtColor(image.numpy(), cv2.COLOR_RGB2BGR)

    print("Label: %d" % label.numpy())
    print("id", id)
    cv2.imshow('test', bgr)
    cv2.waitKey(0)

# print(tiny_imagenet_train)
