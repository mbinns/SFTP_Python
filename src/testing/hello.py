#!/usr/bin/env python
import os
import socket
import traceback
import paramiko
from paramiko.py3compat import input

# setup logging
paramiko.util.log_to_file('iot_sftp.log')

# get host key, if we know one
host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
hostkeytype = None
hostkey = None

# server configureation
hostname = "joey14.cs.clemson.edu"
username = "mbinns"
password = "Guard!ans0tG"
Port = 22

# Kerberos auth
UseGSSAPI = False
DoGSSAPIKeyExchange = False

# grab the ssh host keys
try:
    host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
except IOError:
    print('*** Unable to open host keys file')
    host_keys = {}

if hostname in host_keys:
    hostkeytype = host_keys[hostname].keys()[0]
    hostkey = host_keys[hostname][hostkeytype]
    print('Using host key of type %s' % hostkeytype)

# attempt to connect to the specified server and list directories
try:
    t = paramiko.Transport((hostname, Port))
    t.connect(hostkey, username, password, gss_host=socket.getfqdn(hostname),
              gss_auth=UseGSSAPI, gss_kex=DoGSSAPIKeyExchange)
    sftp = paramiko.SFTPClient.from_transport(t)

    dirlist = sftp.listdir('.')
    print("Dirlist: %s" % dirlist)

    sftp.get('demo_sftp_folder/README','Copied_README')
    t.close()

except Exception as e:
    print('*** Caught exception: %s: %s' % (e.__class__, e))
    traceback.print_exc()
    try:
        t.close()
    except:
        pass
    sys.exit(1)
