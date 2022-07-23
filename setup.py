from setuptools import setup

install_requires = [
    'shap>=0.41.0',
    'dalex>=1.4.1'
]

setup(name='fairdetect_test',
      version='0.2',  # Development release
      description='Library to identify bias in pre-trained models!',
      url='https://github.com/CarlosBlazquezP/test_upload',
      author='Carlos Blazquez',
      author_email='Carlos.BlazquezP@gmail.com',
      license='MIT',
          packages=['fairdetect_test'],
      zip_safe=False,
      install_requires=install_requires)