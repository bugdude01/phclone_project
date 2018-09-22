# Product Hunt Clone

## Clone of Product Hunt to show use of Python and Django.

Hi guys, here's a neat little projct. The idea was to make a simple clone of a website called Product Hunt (http://www.producthunt.com) using
Python and Django to illustrate how easy it would be to build, use a small database, handle authentications etc.

Initially used to refresh myself on Python but also used to get to grips with Django 2. With Python 3 being used exclusively with Django 2 you
will need to have this installed in order for things to work correctly. 

Incidentally, Django 2 is super neat and routing, as always, is super simple but now we are no longer reliant on REGEX!! Apologies to those 
of you who are good with REGEX, I've always been irritated by it but now I'm not forced to use it; super cool.

Anyway, here's the details on how to set this up.

# Geting Started

OK, first things first, this clone was written using Django 2 which means you will need to be using Python 3. Please ensure that you have Python 3 installed and that you have the ability to run Python 3 code. You can check on your command line or in your terminal by typing  `python --version` and seeing what is displayed. If you are unsure if you have Python 3 or not you can type `python3 --version` and if Python 3 is installed it will display which version you have. If you don't have Python 3 instsalled the best way to do this is by going to https://www.python.org/downloads/ and click on the download option for your operating system. Their website should auto detect which OS you are using (Windows / MacOS / Linux etc.) so just go ahead and download VERSION 3.whatever and install in the usual way.

Now you need to instsall Django. You can do this by going to the Django project site (https://www.djangoproject.com/) and downloading from there or you can just as easily use your terminal / command line by typing `pip3 install django`. This will get you the latest version and you're all good to go.

So now you have the right version of Python installed you need to get yourself sorted with a virtual environment. Open up your terminal / command line and type `pip3 install virtualenv`. This will enable you to run your code in a nice segregated area without affecting other programs that you may me working on. Now set up your virtual environment by making your way to the folder you want to work in and type `virtualenv "the name you want to use"` and your virtual environmnt will be set up. To activate the virtual environment, whilst in the same folder type `source "the name you chose"/bin/activate` and you will be running your virtual environment and ready to install the stuff you need to get going. In order to come out of the virtual environment just type `deactivate` and out you come. Easy!

Now that you have the virtual environment available, you can now go ahead and clone this repository and move it into the folder in which you have your virtual environment.

More to follow .... Stay tuned
