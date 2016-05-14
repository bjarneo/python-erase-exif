from setuptools import setup

__version__ = '0.1.0'

setup(
    name='erase_exif',
    version=__version__,
    description='Erase exif meta data from your images',
    long_description='https://github.com/bjarneo/python-erase-exif',
    url='https://github.com/bjarneo/python-erase-exif',
    download_url='https://pypi.python.org/pypi/erase-exif',
    author='Bjarne Oeverli',
    author_email='bjarne.oeverli@gmail.com',
    license='MIT',
    keywords='erase exif image images',
    packages=['erase_exif'],
    install_requires=[
        'Pillow',
        'colorama==0.3.7'
    ],
    entry_points={
        'console_scripts': [
            'erexif=erase_exif.cli:main'
        ]
    },
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
    ],
)
