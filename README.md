# SecurityTrainingGround

## Installation

### Setup The Server
If you're on Dreamhost, this is a bit of a pain right now.  This code uses python 3, and Dreamhost has python 2 installed, so here's what I did:

wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz
tar xfz Python-3.4.3.tgz
cd Python-3.4.3
./configure --prefix="$HOME/opt/python-3.4.3"
make && make install
echo "source .bash_profile" >> ~/.bashrc
echo 'export PATH=$HOME/opt/python-3.4.3/bin:$PATH' >> ~/.bash_profile
cd ~/opt/python-3.4.3
ln -s python3.4 python
ln -s pip3.4 pip
pip install django
pip install boto

Ok, now you're ready to download the code, change to your web root then:
git clone https://github.com/kc0bfv/SecurityTrainingGround.git
cp SecurityTrainingGround/wsgi.py passenger_wsgi.py

If you installed a custom python 3 like above, you're good to go, if not you need to modify passenger_wsgi.py by commenting out the INTERP and if sys.executable lines.  Put # in front of them.  Easy peasy.

If you're on Dreamhost, you need to tell dreamhost to serve the static files correctly:
ln -s $PWD/SecurityTrainingGround/static public/

### Setup an Amazon account

### Setup an image
Mine is easy to use, but if you don't want to do that there's some instruction on how to build your own...

#### Setup your own image

##### Break some stuff

##### Install the Score Bot

##### Set the settings

### Setup the web server
Install the prerequisites:

### Set the settings
Most is self-explanatory, the defaults will get you setup with my image.

### Try it out!
