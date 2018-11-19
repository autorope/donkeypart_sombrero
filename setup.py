from setuptools import setup, find_packages

setup(name='donkeypart_sombrero',
      version='0.1',
      description='Library for donkeycar custom hat, the sombrero.',
      long_description="no long description given",
      url='https://github.com/autorope/donkeypart_sombrero',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      install_requires=['numpy',
                        'gpiozero',
                        'donkeypart_PCA9685_actuators@ https://github.com/autorope/donkeypart_PCA9685_actuators/archive/0.1.2.zip'
                        ],
      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars datastore',
      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
