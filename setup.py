try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'tagtool',
    'packages': ['tagtool'],
    'version': '0.6',
    'description': 'Perform mass ID3 tagging operations.',
    'url': 'https://github.com/dufferzafar/tagtool',
    'license': 'MIT',
    'author': 'Shadab Zafar',
    'author_email': 'dufferzafar0@gmail.com',
    'install_requires': [
        'docopt',
        'mutagen'
    ],
    'scripts': [
        'bin/tagtool',
        'bin/tagfix'
    ],
}

setup(**config)
