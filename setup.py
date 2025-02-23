from setuptools import setup, find_packages

setup(
    name='python-etl-pipeline',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python ETL pipeline for processing data from multiple sources.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'sqlalchemy',
        'logging',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)