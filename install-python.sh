#!/bin/bash

set -e

if [ -x /usr/local/bin/python3.5 ]; then
  echo 'Skipping Python installation since Python 3.5 is already installed.'
else
  echo 'Install required libraries...'
  apt-get update -yq
  apt-get install -yq libreadline-dev libsqlite3-dev libssl-dev

  echo 'Install Python 3.5...'
  cd /tmp
  wget -O- https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz | tar xz
  cd Python-3.5.1
  ./configure
  make
  make altinstall

  echo 'Clean up...'
  cd && rm -rf /tmp/Python-3.5.1

  echo 'Done!'
fi