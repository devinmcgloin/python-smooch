from distutils.core import setup

setup(
    name='smooch',
    packages=['smooch', 'smooch.parse'],
    version='0.01',
    description='A Python wrapper for the Smooch API',
    license='MIT',
    author='Devin McGloin',
    author_email='devin@devinmcgloin.com',
    url='https://github.com/devinmcgloin/smooch',
    download_url='https://github.com/devinmcgloin/smooch/tarball/v0.1',
    keywords=['messaging', 'smooch'],  # arbitrary keywords
    install_requires=[
        'PyPWT',
        'requests'
    ],
    classifiers=[],
)
