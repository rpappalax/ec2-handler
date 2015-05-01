ec2-handler
=======================

Description
-----------

Python Boto scripts for handling Amazon EC2 instances.

For now this is a one-trick-pony:
when given an instance Name as string and a region,
it will simply return the latest instance created with that Name

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

    (venv)$ ec2
    Usage: ec2 [args..] [options]



Example
-----

.. code:: bashl

optional arguments:
  -h, --help            show this help message and exit
  -a ACCESS_KEY, --access-key ACCESS_KEY
                        Access Key
  -s SECRET_KEY, --secret-key SECRET_KEY
                        Secret Key
  -r REGION, --region REGION
  -p PRODUCT_NAME, --product-name PRODUCT_NAME
                        Product Name (i.e. loop_client)


Import
-----

from ec2-handler import EC2Handler

<TBD>

