from setuptools import setup, find_packages

setup(
    name='pyqt-foldable-item-list-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_foldable_item_list_widget.ico': ['down-arrow.svg', 'up-arrow.svg']},
    description='PyQt QListWidget which itemWidget is foldable',
    url='https://github.com/yjg30737/pyqt-foldable-item-list-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)