# YourBlocks
A simple web app to illustrate the features of blockchain.

## How to setup?
1. Copy the file 'blockchain.py' to a suitable directory.
2. Open Terminal and enter the directory in which the file is present. 
3. Enter the command: $ export FLASK_APP=blockchain.py This is will tell the terminal which application to work with by exporting
   the FLASK_APP environment variable.
4. Enter: $ python -m flask run --host=0.0.0.0 This will run an externally visible server.
5. Enter the URL "http://0.0.0.0:5000/" followed by a HTTP function name in a web browser for performing the required operation.

## Technologies used
1. Flask - A python framework used for creating web applications
2. hashlib - Module for using the sha256 cryptographic algorithm
3. Python - Used for creating the blockchain architecture
