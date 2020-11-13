from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_elasticsearch_layer',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        # Exclude virtual environment.
        'venv',
        # Exclude test source files.
        'b_elasticsearch_test'
    ]),
    description=(
        'AWS CDK based lambda layer including Elasticsearch client.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "aws-cdk.core>=1.54.0,<2.0.0",
        "aws-cdk.aws_lambda>=1.54.0,<2.0.0",
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='AWS CDK Lambda Layer Elasticsearch',
    url='https://github.com/biomapas/B.ElasticsearchLayer.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
