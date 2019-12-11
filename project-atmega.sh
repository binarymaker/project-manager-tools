echo
echo '+------------------------------------------+'
echo '|Creating project eco-system for avr-atmega|'
echo '+------------------------------------------+'

echo
echo Download dependency modules
echo ---------------------------
git submodule add -b library https://github.com/binarymaker/embclib.git library/embclib
git submodule add -b library https://github.com/binarymaker/avr-atmega-driver.git library/avr-atmega-driver
git submodule add -b library https://github.com/binarymaker/embedded-printf.git library/printf

echo 
echo import dependency modules configuration
echo ---------------------------------------
echo import embclib module configuration to project
cp -r library/embclib/config/. config/config-embclib
echo import avr-atmega-driver module configuration to project
cp -r library/avr-atmega-driver/config/. config/config-avr-atmega-driver
echo import printf module configuration to project
cp -r library/printf/config/. config/config-printf

echo
echo Checkout to develop branch
echo --------------------------
git checkout -b develop