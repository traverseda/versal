mkdir pypy
cd pypy
wget https://bitbucket.org/pypy/pypy/downloads/pypy-2.1-src.tar.bz2
tar -jxvf  ./pypy-2.1-src.tar.bz2

cd pypy/pypy-2.1-src/pypy/goal

../../rpython/bin/rpython -O2 --sandbox targetpypystandalone.py

