import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-foldable-item-list-widget',
    version='0.0.11',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_foldable_item_list_widget.ico': ['down-arrow.svg', 'up-arrow.svg']},
    description='PyQt QListWidget which itemWidget is foldable',
    url='https://github.com/yjg30737/pyqt-foldable-item-list-widget.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-svg-icon-pushbutton>=0.0.1'
    ]
)