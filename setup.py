from distutils.core import setup
setup(
  name = 'pyqt5-notificator',
  packages = ['notificator','notificator.alingments','notificator.resources','notificator.UI'],
  version = '1.0.10',
  license='MIT',
  description = 'pyqt5_notificator is a module to generate pyqt5 desktop notifications',
  author = 'Alejandro Alejo',
  author_email = 'alejandroalejo714@gmail.com',
  url = 'https://github.com/Alejandro1407/PyQt5_Notficator',
  download_url = 'https://github.com/Alejandro1407/PyQt5_Notficator/archive/1.0.0.tar.gz',
  keywords = ['notifity','desktop'],
  install_requires=[
          'pyqt5',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)