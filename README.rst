deploy-verifier
=======================

Description
-----------

Python scripts to verify Mozilla Cloud Services deployments.

Note: still under development. 

|travis| |pypi|

.. |travis| image:: https://travis-ci.org/rpappalax/deploy-verifier.svg?branch=dev
    :target: https://travis-ci.org/rpappalax/deploy-verifier

.. |pypi| image:: https://badge.fury.io/py/deploy-verifier.svg
    :target: http://badge.fury.io/py/deploy-verifier


**Supported projects**
 - loop-client
 - loop-server
 - msisdn-gateway 
 - shavar 


Install
-------

.. code:: bash

    $ git clone https://github.com/rpappalax/deploy-verifier.git
    $ cd deploy-verifier
    $ python setup.py develop
    $ make build

Setup
-----
deploy-verify uses the AWS boto library which requires that a config file:
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

