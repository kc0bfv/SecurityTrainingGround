# SecurityTrainingGround

## Installation
I am hosting my current version of this on Dreamhost, which has been a really good hosting company for me.  Many of these instructions are geared toward them, but in general the instructions are valid for other hosting setups.  If you're hosting yourself, just remember that this uses Django.  I tried to do no magic, so the regular Django setup instructions should work for you.

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

If you're using Dreamhost, this next line tells Passenger where to run your program:
cp SecurityTrainingGround/wsgi.py passenger_wsgi.py

If you installed a custom python 3 like above, you're good to go, if not you need to modify passenger_wsgi.py by commenting out the INTERP and if sys.executable lines.  Put # in front of them.  Easy peasy.

If you're on Dreamhost, you need to tell dreamhost to serve the static files correctly:
ln -s $PWD/SecurityTrainingGround/static public/

Make the stopScript.py automatically run.  A shell script to do this is "runStopScript".  You'll want to modify it for your install...  I put my in crontab to run every 10 minutes, because that's as fast as Dreamhost likes...

If you want the Django admin CSS to work and you installed that custom Django like above:
ln -s "$HOME/opt/lib/python3.4/site-packages/django/contrib/admin/static/admin" public/static/

### Setup an Amazon account

### Setup an image
Mine is easy to use, but if you don't want to do that there's some instruction on how to build your own...

#### Setup your own image

##### Break some stuff

##### Install the Score Bot

##### Set the settings

### Set the settings
Run "setupDatabase" and give it a Django superuser and password.  This will be the user capable of modifying existing accounts and such, so maybe give it a good password.  Maybe one you don't mind sharing.

Run "writeConfig.py" and follow the instructions.  Most is self-explanatory, the defaults will get you setup with my image.


### Try it out!
