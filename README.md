CPSC 4200 Group Project
======================

This program will run as a daemon on an IOT devices and securly download updates over a network

## Dependencies

* python3+
* paramiko python library
    * https://github.com/paramiko/paramiko.git
* OpenSSH

## Testing

* the testing file in the code directory contains a file that can be edited to test with

## Running

* Edit the files host variable to point to the server you are trying to connect to
* Edit the files username variable for the user you are trying to login with
* You will then also want to give the file path on the remote server that you are trying to copy, along with the local directory for it to be saved in

## OPTIONAL

* you can also specify a password to login to the server with for the user. To do so you can fill in the password variable and then uncomment the password authentication line

