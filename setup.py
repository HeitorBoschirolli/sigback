import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='sigback',
    version='0.1.0',
    description='Process and add background to signature images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HeitorBoschirolli/sigback',
    author='Heitor Boschirolli',
    author_email='heitor.boschirolli@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    packages=['sigback', 'blend', 'processing'],
    include_package_data=False,
    install_requires=['scikit-learn', 'numpy']
)
