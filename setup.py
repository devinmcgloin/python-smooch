from distutils.core import setup

setup(
    name='python-smooch',
    packages=['smooch', 'smooch.parse'],
    version='v0.1.3',
    description='A Python wrapper for the Smooch API',
    license='MIT',
    author='Devin McGloin',
    author_email='devin@devinmcgloin.com',
    url='https://github.com/devinmcgloin/python-smooch',
    download_url='https://github.com/devinmcgloin/python-smooch/tarball/v0.1.3',
    keywords=['messaging', 'smooch'],  # arbitrary keywords
    install_requires=[
        'PyPWT',
        'requests'
    ],
    classifiers=[],
)
