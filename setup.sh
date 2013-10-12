
##Download an compile verse and the verse2 python binaries
git clone https://github.com/verse/verse.git
mkdir verse/build
cd verse
git apply ../install/python2build.patch
cd build
cmake ../
make

#Gets us back to our main working directory
cd ../../

#moves us into the subscripts directory
cd install

##installs and compiles the pypy sandbox
./pypy.sh
