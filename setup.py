from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='promethium-py',
    version='0.1.0',
    author='Rohan Kishore',
    author_email='rohan@example.com',
    description='A Pythonic interface to a rich, offline database of chemical information.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rohankishore/promethium',
    packages=find_packages(),
    package_data={
        'promethium': ['data/*.csv'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
        'pandas',
        'numpy',
    ],
)