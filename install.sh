#!/bin/bash

if [ "${PWD##*/}" == "doccli" ] ; then
  sudo chmod +x doccli
  sudo mv doccli /usr/local/bin
  
  sudo mkdir ~/.doccli_src
  sudo mv * ~/.doccli_src
  
  cd ~/.doccli_src && sudo python -m venv .venv
  cd ~/.doccli_src && sudo .venv/bin/pip install requests pypresence
else
  echo "WEJDZ DO FOLDERU DOCCLI!"
fi
