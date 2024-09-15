from setuptools import setup, find_packages

setup(
    name='orpheuspypractice',
    version='0.1.40',
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
        "jgcmlib>=1.0.51"
    ],
    entry_points={
        'console_scripts': [
            "oabc = orpheuspypractice:jgabcli_main",
            "omid2score = orpheuspypractice:jgabcli_main_mid2score",
            "say_hello_orpheuspypractice = orpheuspypractice:say_hello",
            "odep = orpheuspypractice.dependency_action:main"
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
