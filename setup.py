import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='sigback',
    version='0.0.1',
    description='Process and add background to signature images',
    long_description=long_description,
    licence='MIT',
    author='Heitor Boschirolli',
    author_email='heitor.boschirolli@gmail.com',
    url='https://github.com/pypa/sampleproject',
    packages=['blend', 'processing'],
    install_requires=[
        'scikit-learn',
        'numpy',
    ]
)
