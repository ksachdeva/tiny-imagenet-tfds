# tiny-imagenet-tfds

## Introduction

Tiny Imagenet is a scaled down version of ImageNet dataset. This dataset was created by
folks at Stanford for their course [http://cs231n.stanford.edu/](http://cs231n.stanford.edu/).

### Salient Features

* 200 image classes
* Training dataset of 100,000 images
* Validation dataset of 10,000 images
* Test dataset of 10,000 images.
* All images are of size 64×64.

> Note that the labels for Test dataset have not been provided.

## Install

I have not yet published it on pypi yet so install it directly from github.

```bash
pip install git+https://github.com/ksachdeva/tiny-imagenet-tfds.git
```

## Usage

`tensorflow_datasets` is a python package that provides support for downloading, preparing and
constructing a `tf.data.Dataset`. See more information at -

[https://www.tensorflow.org/datasets/overview](https://www.tensorflow.org/datasets/overview)

This package provides the support for `tiny-imagenet` dataset.

```python
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

```
