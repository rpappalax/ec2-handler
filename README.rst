ec2-handler
=======================

Description
-----------

Python Boto scripts for handling Amazon EC2 instances 

Note: still under development. 

|travis| |pypi|

.. |travis| image:: https://travis-ci.org/rpappalax/ec2-handler.svg?branch=dev
    :target: https://travis-ci.org/rpappalax/ec2-handler

.. |pypi| image:: https://badge.fury.io/py/ec2-handler.svg
    :target: http://badge.fury.io/py/ec2-handler


Install
-------

.. code:: bash

    $ git clone https://github.com/rpappalax/ec2-handler.git
    $ cd ec2-handler
    $ python setup.py develop
    $ make build

Setup
-----
ec2-handler uses the AWS boto library which requires that a config file:
".boto" be in your home dir for authentication.  
Be sure to secure your config file:

.. code:: bash

 $ chmod 400 .boto 


**Example .boto file**

.. code:: bash

 [Credentials]
 aws_access_key_id = ABCDEFGHIJKLMNOP
 aws_secret_access_key= QRSTUVWXYZabcdefGHIJK/X9/o123456789 



Build
-----

.. code:: bash

    $ make build 
    $ source ./venv/bin/activate

Run
-----

.. code:: bash

    (venv)$ verify
    Usage: verify [args..] [options]

    <TBD>


Example
-----

.. code:: bash

    <TBD>

