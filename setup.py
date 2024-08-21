# SPDX-FileCopyrightText: Bosch Rexroth AG
#
# SPDX-License-Identifier: MIT
from setuptools import setup

setup(name='sdk-py-webserver',
      version='2.3.0',
      description='Webserver Sample written in Python for ctrlX',
      author='SDK Team',
      install_requires=['flask', 'flask_socketio', 'gevent-websocket'],
      scripts=['application.py'],
      packages=['scripts', 'static', 'templates'],
      license='MIT License'
      )
