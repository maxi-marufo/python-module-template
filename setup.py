from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


def read_other_requirements(other_type):
    with open(other_type+'-requirements.txt') as f:
        return f.read()

setup(
      setup_requires=read_other_requirements('setup'),
      pbr=True,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=True
    )
