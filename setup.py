"""tiny-imagenet-tfds is a library to access tiny-imagenet dataset using tf.data.Dataset.

This library contains the support to download, extract, and prepare the dataset as tfrecords.
"""

import datetime
import os
import sys

from setuptools import find_packages
from setuptools import setup

project_name = 'tiny-imagenet-tfds'

# To enable importing version.py directly, we add its path to sys.path.
version_path = os.path.join(
    os.path.dirname(__file__), 'tiny_imagenet')
sys.path.append(version_path)

DOCLINES = __doc__.split('\n')

REQUIRED_PKGS = [
    'tensorflow-datasets'
]

TESTS_REQUIRE = [
]

# Static files needed by datasets.
DATASET_FILES = [
    'url_checksums/tiny_imagenet_dataset.txt'
]

EXTRAS_REQUIRE = {
}

setup(
    name=project_name,
    version='0.1.0',
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    author='Kapil Sachdeva',
    author_email='not@anemail.org',
    url='http://github.com/ksachdeva/tiny-imagenet-tfds',
    download_url='https://github.com/ksachdeva/tiny-imagenet-tfds/tags',
    license='Apache 2.0',
    packages=find_packages(exclude=("example",)),
    package_data={
        'tiny_imagenet': DATASET_FILES,
    },
    scripts=[],
    install_requires=REQUIRED_PKGS,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='tensorflow machine learning datasets tiny-imagenet',
)
