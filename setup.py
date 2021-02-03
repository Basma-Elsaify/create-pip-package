
from setuptools import find_packages, setup

from version import __version__

setup(
    name='pipprojectpkg',
    version=__version__,  # noqa
    author='Opensource contribution',
    author_email='basmaelsaify@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Just for testing, to be updated or removed',
    include_package_data=True,
    long_description=open('README.md').read(),
    extras_require={},
    license='Apache-2.0',
    packages=find_packages(exclude=('examples', 'tests',)),
    namespace_packages=[],
    zip_safe=False,
)