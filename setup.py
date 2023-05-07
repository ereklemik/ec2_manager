from setuptools import setup, find_packages

setup(
    name='ec2_manager',
    version='1.0',
    packages=find_packages(),
    python_requires='>=3.10.6',
    install_requires=[
        'boto3',
    ],
    author='Erekle Mikiashvili',
    author_email='ereklemikiashvili@gmail.com'
)
