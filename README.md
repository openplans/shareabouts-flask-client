Shareabouts Flask Starter Client
================================

What is this?
-------------

A template to get your [Shareabouts](http://shareabouts.org) client app running on
[DotCloud](https://www.dotcloud.com/) as fast as possible. This starter kit is based
off of [zachwill](https://github.com/zachwill)'s
[Flask Cloud](https://github.com/zachwill/flask_cloud) project.

Instructions
------------

First, you'll need to clone the repo.

    $ git clone git@github.com:openplans/shareabouts-flask-client.git
    $ cd shareabouts-flask-client

Second, let's download `pip`, `virtualenv`, and the DotCloud CLI.

    $ sudo easy_install pip
    $ pip install virtualenv
    $ pip install dotcloud

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt

Now, you can run the application locally.

    $ python bootstrap.py

You can easily specify which port you'd like to run your application on, too:

    $ python bootstrap.py 5555

To upload your application to DotCloud, you'll first need to do the
following:

    $ dotcloud create <my_application_name>
    $ dotcloud push <my_application_name> .

This should return a URL, and you can then view your application in
your web browser of choice.

And, to deactivate `virtualenv` (once you've finished coding), you
simply run the following command:

    $ deactivate


Adding Requirements
-------------------

In the course of creating your application, you may find yourself
installing various Python modules with `pip` -- in which case you'll
need to update the `requirements.txt` file. One way that this can be
done is with `pip freeze`.

    $ pip freeze > requirements.txt


Other Hosting Environments
--------------------------

In case you're wanting to host your application on another environment
(the use case I'm imagining currently is Amazon's AWS), you could always
install `pip` and then uncomment `gevent` from the `requirements.txt`
file (or whatever server you plan on using).

We'll first setup our isolated environment like before:

    $ sudo easy_install pip
    $ pip install virtualenv
    $ virtualenv --no-site-packages env
    $ source env/bin/activate

You then should have no problem installing the packages.

    $ pip install -r requirements.txt

The idea then is that your application could be served with `gevent` by
envoking the `bootstrap.py` file like so:

    $ python bootstrap.py --gevent

Currently, this is more of a general idea than a working implementation
-- I'm sure you'd want to put `nginx` in front of your configuration to
serve up static files and media.
