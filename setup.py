from distutils.core import setup

setup(
    name = 'ororo-pp',
    packages = ['ororo-pp'],
    version = '0.1',
    description = 'A basic pre-processor for CloudFormation Templates',
    author = 'Dean Wilson',
    author_email = 'dean.wilson@gmail.com',
    url = 'https://github.com/deanwilson/ororo-pp',
    download_url = 'https://github.com/deanwilson/ororo-pp/tarball/0.1',
    keywords = ['CloudFormation', 'AWS', 'Preprocessor'],
    classifiers = [
        "Topic :: Text Editors :: Text Processing",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
    ],
    install_requires=[
        "Jinja2"
    ]
)
