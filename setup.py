from tagtool.version import __VERSION__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tagtool',
    packages=['tagtool'],
    version=__VERSION__,
    description='Tagtool allows you to perform mass ID3 tag cleaning operations.',
    long_description=open('Readme.md').read(),
    url='https://github.com/dufferzafar/tagtool',
    license='MIT',
    author='Shadab Zafar',
    author_email='dufferzafar0@gmail.com',
    install_requires=[
        'docopt',
        'mutagen'
    ],
    scripts=[
        'bin/tagtool',
        'bin/tagfix'
    ],
    classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
    ],
)
