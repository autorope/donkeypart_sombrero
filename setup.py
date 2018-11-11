from setuptools import setup, find_packages

setup(name='donkeypart_sombrero',
      version='0.1',
      description='Library to use the custom raspberry pi hat for the donkey car.',
      long_description='none',
      long_description_content_type="text/markdown",
      url='https://github.com/autorope/donkeypart_sombrero',
      download_url="",
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      install_requires=['gpiozero', 'donkeycar'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars donkeypart',
      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
