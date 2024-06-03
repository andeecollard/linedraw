from setuptools import setup, find_packages

setup(
    name='linedraw',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow', 
        'Numpy',
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'linedraw=linedraw.linedraw_cli:main',
        ],
    },
)
