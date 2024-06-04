from setuptools import setup, find_packages

setup(
    name="linedraw",
    version="0.1.0",
    description="Convert images to line drawings",
    author="Author Name",
    author_package="author@example.com",
    url="https://github.com/rahulps1000/linedraw",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Pillow',   # Pillow for image manipulation
        'numpy',    # NumPy for numerical operations
        'opencv-python'  # OpenCV for additional image processing
    ],
    entry_points={
        'console_scripts': [
            'linedraw=linedraw.main:main',  # Adjust the path and function name as necessary
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
