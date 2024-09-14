from setuptools import setup, find_packages

setup(
    name='orpheuspypractice',
    version='0.1.16',
    author='JGWill',
    author_email='jgi@jgwill.com',
    description='A Practice Package to Experiment with Orpheus\'s goals',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jgwill/orpheuspypractice',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "tlid",
        "requests",
        "music21",
        "ipython",
        "jgcmlib"
    ],
    entry_points={
        'console_scripts': [
            "jgabcli2 = orpheuspypractice:jgabcli_main",
            "say_hello = orpheuspypractice:say_hello",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)