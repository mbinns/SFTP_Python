#!/usr/bin/env python
import os
import socket
import traceback
import paramiko
import sys
from paramiko.py3compat import input

# setup logging
paramiko.util.log_to_file('iot_sftp.log')

# server configureation
host = "130.127.49.33"
password = ""
username = "mbinns"

# attempt to connect to the specified server and list directories using ssh and sftp
try:
    ssh = paramiko.SSHClient()

    # incase the server is unknown auto add to the list of know hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # load the host keys client is aware of
    ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))

    # connect to server using ssh private key/password 
    # ssh.connect(host, username=username, password=password)
    ssh.connect(host, username=username, look_for_keys=True)

    # open sftp connection
    sftp = ssh.open_sftp()

    # list dirs as a test
    dirlist = sftp.listdir('.')
    print("Dirlist: %s" % dirlist)
    
    # copy file back from server 
    # SYNTAX: remote_location/file, local_location/name
    sftp.get('demo_sftp_folder/README','./Copied_README')

    # close hanging connections
    sftp.close()
    ssh.close()

except Exception as e:
    print('*** Caught exception: %s: %s' % (e.__class__, e))
    traceback.print_exc()
    try:
        t.close()
    except:
        pass
    sys.exit(1)
