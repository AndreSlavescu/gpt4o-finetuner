from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='gpt4o-finetuner',
    version='0.0.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'convert_parquet_to_jsonl=data_to_jsonl:main',
        ],
    },
    author='Andre Slavescu',
    python_requires='>=3.10',
)
