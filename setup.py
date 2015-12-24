import tagtool

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tagtool',
    packages=['tagtool'],
    version=tagtool.version,
    description='Tagtool allows you to perform mass ID3 tag cleaning operations.',
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
