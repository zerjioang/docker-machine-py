from setuptools import setup, find_packages

__version__ = "00.1"

install_requires = [
    'coloredlogs', 'mkdocs', 'mkdocs-material'
]

setup(
    name="docker-machine-py",
    version=__version__,
    packages=find_packages(),
    install_requires=install_requires,
    package_data={
        '': ['*.rst'],
    },
    author="zerjioang",
    author_email="sergio.anguita@opendeusto.es",
    description="Python wrapper for docker-machine",
    license="GPL3",
    keywords="docker machine docker-machine container",
    url="https://github.com/zerjioang/docker-machine-py",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
