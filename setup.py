from setuptools import setup, find_packages


setup(
    name='python-smooch',
    packages=find_packages(exclude=['docs', 'tests']),
    version='v1.0.3',
    description='A Python wrapper for the Smooch API',
    license='MIT',
    author='Devin McGloin',
    author_email='devin@devinmcgloin.com',
    url='https://devinmcgloin.com/python-smooch',
    download_url='https://github.com/devinmcgloin/python-smooch/tarball/v1.0.3',
    keywords=['messaging', 'smooch'],
    install_requires=[
        'requests',
        'PyJWT'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

        "License :: OSI Approved :: MIT License",

        "Topic :: Communications :: Chat"
    ],
)
