from setuptools import setup, find_packages

setup(
    name='orpheuspypractice',
    version='0.3.0',
    author='JGWill',
    author_email='jgi@jgwill.com',
    description='AI-Powered Music Generation & Interactive Composition Toolkit',
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
        "jgcmlib>=1.0.59",
        "jghfmanager>=0.1.5",
        "langchain",
        "langchain_openai",
        "langchain_community",
        "arxiv",
        "pyyaml",
        "python-dotenv",
        "langgraph",
        "wikipedia",
        "llm",
        "pandas",
        "numpy",
        "langchain-experimental",
        "langsmith",
        "numexpr",
        "strip-tags",
        "jaraco.functools",
        "jaraco.context",
        
    ],
    entry_points={
        'console_scripts': [
            "oabc = orpheuspypractice:jgabcli_main",
            "omid2score = orpheuspypractice:jgabcli_main_mid2score",
            "osay_hello_orpheuspypractice = orpheuspypractice:say_hello",
            "olca = orpheuspypractice.olca:main",
            "oiv = orpheuspypractice.oiv:main",
            "odep = orpheuspypractice.dependency_action:main",
            "ohfi = orpheuspypractice:jgthfcli_main",
            "wfohfi_then_oabc_foreach_json_files = orpheuspypractice:wfohfi_then_oabc_foreach_json_files",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
