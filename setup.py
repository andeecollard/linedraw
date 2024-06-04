from setuptools import setup, find_packages

setup(
    name="linedraw",
    version="0.1.0",
    description="Convert images to line drawings",
    long_description="A tool to convert images into line drawings using Python, leveraging libraries such as Pillow and OpenCV.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/andeecollard/linedraw",
    packages=find_packages(),  # Automatically find and include all packages
    include_package_data=True,
    install_requires=[
        'Pillow',  # Image handling
        'numpy',  # Numerical operations
        'opencv-python'  # Image processing
    ],
    entry_points={
        'console_scripts': [
            'linedraw=linedraw.main:main',  # Adjust this to your module and function
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
