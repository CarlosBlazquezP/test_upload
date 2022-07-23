from setuptools import setup

install_requires = [
    'shap>=0.41.0',
    'dalex>=1.4.1'
]

setup(name='fairdetect',
      version='0.1',  # Development release
      description='Library to identify bias in pre-trained models!',
      url='https://github.com/CarlosBlazquezP/test_github_upload',
      author='Carlos Blazquez',
      author_email='Carlos.BlazquezP@gmail.com',
      license='MIT',
          packages=['fairdetect'],
      zip_safe=False,
      install_requires=install_requires)