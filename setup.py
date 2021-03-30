import setuptools
from os import path
import package

here = path.abspath(path.dirname(__file__))
AUTHORS = """
Stephanie Valleau
Nida Janulaitis
Evan Komp
Brenden Pelkie
"""


# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

if __name__ == "__main__":
    setuptools.setup(
        name='package',
        version=package.__version__,
        author=AUTHORS,
        project_urls={
            'Source': 'https://github.com/valleau-lab/tutorials',
        },
        description=
        'Tutorials of useful tools used by the Valleau lab.',
        long_description=long_description,
        include_package_data=False,
        keywords=[
            'Machine Learning', 'Reaction Kinetics', 'Ab initio',
            'Chemical Engineering','Chemistry', 
        ],
        license='Apache License 2.0',
        packages=setuptools.find_packages(exclude="tests"),
        scripts = [], #if we want to include shell scripts we make in the install
        install_requires=[
            'numpy', 
        ],
        extras_require={
            'tests': [
                'pytest',
                'coverage',
                'flake8',
                'flake8-docstrings'
            ],
        },
        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Operating System :: OS Independant',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
        zip_safe=False,
    )
