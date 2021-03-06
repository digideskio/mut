import sys
from setuptools import setup, find_packages

REQUIRES = [
    'boto>=2.39,<2.40',
    'certifi',
    'docopt>=0.6,<0.7',
    'docutils',
    'dominate>=2.1,<2.2',
    'libgiza>=0.2.13,<0.3',
    'PyYAML',
    'requests>2.9,<2.10',
    'rstcloth>0.2.5',
    'sphinx==1.4b1',
]

# Need a fallback for the typing module
if sys.version < '3.5':
    REQUIRES.append('mypy-lang')

setup(
    name='mut',
    description='',
    version='0.0.0',
    author='Andrew Aldridge',
    author_email='i80and@foxquill.com',
    license='Apache',
    packages=find_packages(),
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        ],
    entry_points={
        'console_scripts': [
            'mut = mut.helper:main',
            'mut-build = mut.main:main',
            'mut-images = mut.build_images:main',
            'mut-intersphinx = mut.intersphinx:main',
            'mut-lint = mut.lint:main',
            'mut-publish = mut.stage:main',
            ],
        }
    )
