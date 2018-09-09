import os
import time
import platform
import SendKeys
import ConfigParser
import sys
from subprocess import Popen, PIPE
from _winreg import *


HOMEDRIVE = os.environ['HOMEDRIVE']
SCRIPTSDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
WORKDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
PYTHON_EXEC = HOMEDRIVE + r'\Python27\python.exe'
SYSTEMROOT = os.environ['SYSTEMROOT']
PROGRAMFILES = os.environ['PROGRAMFILES']
PIP_PATH = r'C:\Python27\Scripts'
current_dir = os.getcwd()
if os.path.exists(current_dir + r'\Initialsetup_log.txt'):
    os.remove("Initialsetup_log.txt")

if "64" in platform.uname()[4]: # OS Architecute of the system
    OS_BIT = "64"
    PROGRAM_FILES = r'C:\Program Files (x86)'
else:
    OS_BIT = "32"
    PROGRAM_FILES = r'C:\Program Files'
PYTHONPATH = r'C:\Python27' 
setupfilepath =  WORKDIR + r'\Setupfiles\%s'%OS_BIT
def tskList():
    res, err = Popen('tasklist', shell=True, stdout=PIPE, stderr=PIPE).communicate()
    return res
def tskKill(tskName):
    Popen('taskkill /F /IM %s' %tskName, shell=True).communicate()

def ReadConfig(tag, variable):
    try:
        Config = ConfigParser.ConfigParser()
        Config.read(current_dir + r"\\Initialsetup_Config.ini")
        return Config.get(tag,variable)
    except Exception as e:
        return False
        
def Disablefirewall():
    #1. Disabling Firewall
    #print_and_write("\nTask 1: Disabling Firewall")
    res, err = Popen('NetSh Advfirewall set allprofiles state off',
                     shell=True,
                     stdout=PIPE,
                     stderr=PIPE).communicate()
    print_and_write('\nFirewall: Disabled')


def CreateStructure():
    #2. Disabling Firewall

    #print_and_write("\nTask 2: Creating directories 'scripts', 'tools'")
    if not os.path.exists(HOMEDRIVE + r'\Automation'):
        os.mkdir(HOMEDRIVE + r'\Automation')  

    if not os.path.exists(HOMEDRIVE + r'\Automation\scripts'):
        os.mkdir(HOMEDRIVE + r'\Automation\scripts')

    if not os.path.exists(HOMEDRIVE + r'\Automation\tools'):
        os.mkdir(HOMEDRIVE + r'\Automation\tools')

    if not os.path.exists(HOMEDRIVE + r'\Automation\utils'):
        os.mkdir(HOMEDRIVE + r'\Automation\utils')
        
    if not os.path.exists(HOMEDRIVE + r'\Automation\Scenario'):
        os.mkdir(HOMEDRIVE + r'\Automation\Scenario')
        
    if not os.path.exists(HOMEDRIVE + r'\Automa'):
        os.mkdir(HOMEDRIVE + r'\Automa')
        
    if not os.path.exists(HOMEDRIVE + r'\Automation\FTS Scenarios'):
        os.mkdir(HOMEDRIVE + r'\Automation\FTS Scenarios')

    if not os.path.exists(HOMEDRIVE + r'\TWS'):
        os.mkdir(HOMEDRIVE + r'\TWS')
        
    os.chdir(setupfilepath)
    os.system("sharefolder.bat")
    time.sleep(60)
    print_and_write("\nFolder Structure : Created")
    print_and_write("\nTurn On Fast Startup : Disabled")
    print_and_write("\nIPV6 : Disable")
    print_and_write("\nDriver signing : Enabled")
    print_and_write("\nPower settings : Never")

def toolscopy():
    try:
        
        #src = ReadConfig('toolsfolder', 'src_path')
        #dst = ReadConfig('toolsfolder', 'dst_path')
        src = WORKDIR + r'\Setupfiles\tools'
        dst = r'C:\Automation\tools'
        command = "copy.exe "+ src +" " +dst
        print command
        os.chdir(setupfilepath)
        os.system(command)
        print_and_write("\nTools : Copied")
        
    except Exception as err:
        print_and_write('\nTools : Not Copied due to %s:' % err)
    
def InstallPython():
    #3. Installing Python 2.7
    Pythonsetup = ReadConfig('EXENAME_'+OS_BIT, 'Pythonsetup')
    try:
        if os.path.exists(HOMEDRIVE + r'\Python27\python.exe'):
            os.chdir(setupfilepath)
            os.system('regedit /s HKLM.reg')
            time.sleep(5)
            print_and_write('\nPython : Installed')

        else:
            #Copying Python installer to Desktop
            #print_and_write('\nTask 3: Installation of Python')
            os.chdir(setupfilepath)
            Popen('msiexec.exe /qr /i %s'%Pythonsetup)
            time.sleep(150)
            #print_and_write('#Python -->>> Installed\n')

            if os.path.exists(HOMEDRIVE + r'\Python27\python.exe'):
                os.chdir(setupfilepath)
                os.system('regedit /s HKLM.reg')
                time.sleep(5)
                print_and_write('\nPython : Installed')

            else:
                print_and_write('\nPython : Not Installed')

    except Exception as err:
        print_and_write('\nPython : Not Installed')

def SetPythonpath():
    #4. Setting Python Path
    PyInstaLationP = HOMEDRIVE + r'\Python27'    # C:\Python27
    regpath = 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment'
    installkey = 'PYTHONPATH'

    value =  PyInstaLationP + ';' + HOMEDRIVE + r'\Automation\utils;' \
                 +PyInstaLationP + r'\Lib\site-packages;'

    try:
        reg = CreateKey(HKEY_LOCAL_MACHINE, regpath)
        SetValueEx(reg, installkey, '', REG_SZ, value)
        os.system(r'set PYTHONHOME=C:\Python27')
        os.system(r'set PATH=%PATH%;%PYTHONHOME%;%PYTHONPATH%')
        print_and_write('\nPYTHONPATH : SET')

    except WindowsError as err:
        print_and_write("\nPYTHONPATH : Not updated due to %s" % err)

    except Exception as err:
        print_and_write("\nPYTHONPATH : Not updated due to %s" % err)
        
def dotnet():
    ## Type registration
    curDir = os.path.dirname(os.path.abspath(sys.argv[0]))
##    print curDir

    os.chdir(SYSTEMROOT + r"\Microsoft.NET\Framework\v4.0.30319")
    os.system("RegAsm.exe \"" + setupfilepath + "\\XMLLogging.dll\"")

    os.chdir(SYSTEMROOT + r"\Microsoft.NET\Framework\v4.0.30319")
    os.system("RegAsm.exe \"" + setupfilepath + "\\XMLLogging.dll\"")
    print_and_write('\nDotnetframework : Enabled')

def RunCmdAsAdmin():
    ## Run all command prompt as admin
    try:
        reg = CreateKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers')
        SetValueEx(reg, 'C:\\windows\\system32\\cmd.exe', '', REG_SZ, 'RUNASADMIN')
        print_and_write('\nRUNCMDASADMIN : SET')

    except Exception, Err:
        flag = False
        print_and_write("RUNCMDASADMIN : Not SET due to %s: " %str(Err))
        

def DisableUAC():
    ## Disable UAC
    try:
        reg = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',
                      0, KEY_ALL_ACCESS)
        SetValueEx(reg, 'EnableLUA', '', REG_DWORD, 0x0)
        print_and_write('\nUAC : Disabled')

    except Exception, Err:
        flag = False
        print_and_write("\nUAC : UAC Disabled due to %s: " %str(Err))
        
        
def InstallPywinauto():
    # "pywin32-217.win32-py2.7"
    import pdb
    os.chdir(setupfilepath)
    pywinautofoldername = ReadConfig('EXENAME_'+OS_BIT, 'pywinautofoldername')
    try:
        curDir = os.getcwd()
        os.chdir(setupfilepath + r'\%s'%pywinautofoldername)
        PythonExe = HOMEDRIVE + r'\Python27\python.exe'
        res1, err1 = Popen('%s setup.py install' % PythonExe, shell=True, stdout=PIPE, stderr=PIPE).communicate()
        time.sleep(2)
        os.chdir(curDir)
        print_and_write('\nPywinauto : Installed')

    except Exception as excp_winauto:
        print_and_write('\nPywinauto : Not Installed due to %s' % excp_winauto)
        
def InstallSendKey():
    #Installation of SendKeys-0.3.win32-py2.7
    Sendkeys_exe = ReadConfig('EXENAME_'+OS_BIT, 'sendkey_exe')
    if foundfile(Sendkeys_exe,setupfilepath):        
        if (OS_BIT == "32"):          
            if not os.path.exists(HOMEDRIVE + r'\Python27\RemoveSendKeys.exe'):                        
                try:
                    os.chdir(setupfilepath)
                    Popen(Sendkeys_exe)
                    time.sleep(5)
                    SendKeys.SendKeys("{ENTER}")
                    time.sleep(5)
                    SendKeys.SendKeys("{ENTER}")
                    time.sleep(5)
                    SendKeys.SendKeys("{ENTER}")
                    time.sleep(20)
                    SendKeys.SendKeys("{ENTER}")
                    time.sleep(10)
                    ListOfTasks = tskList()
                    if "SendKeys" in ListOfTasks:
                        tskKill(Sendkeys_exe)
                    if os.path.exists(HOMEDRIVE + r'\Python27\RemoveSendKeys.exe'):
                        print_and_write('\nSendKeys : Installed')
                    else:
                        print_and_write('\nSendKeys : NOT Installed')                       
                            
                except Exception as excp:
                    print_and_write('\nSendKeys : Not Installed due to %s' %excp)           
            else:
                print_and_write('\nSendKeys : Installed')

        else:
            if not os.path.exists(r'C:\Python27\Lib\site-packages\SendKeys.py'):
                try:
                    cmd = PIP_PATH+r'\pip install ' + '"' +setupfilepath+"\\"+ Sendkeys_exe + '"'
                    print cmd
                    Popen(cmd)
                    time.sleep(30)
                    if os.path.exists(r'C:\Python27\Lib\site-packages\SendKeys.py'):
                            print_and_write('\nSendKeys : Installed')
                    else:
                            print_and_write('\nSendKeys : NOT Installed') 
                except Exception as excp:
                        print_and_write('\nSendKeys : Not Installed due to %s' %excp) 
				
            else:
                    print_and_write('\nSendKeys : Installed')
    else:
        print_and_write('\nSendKeys : %s file not found at %s'%(Sendkeys_exe,setupfilepath))
        
def foundfile(filename,folder_path):
    if os.path.exists(folder_path+'\\'+filename):
        return True
    else:
        return False                       
            
def Installpywin32():
    #Installation of sendkeys
    time.sleep(10)
    if not os.path.exists(HOMEDRIVE + r'\Python27\Removepywin32.exe'):
        pywin32_exe = ReadConfig('EXENAME_'+OS_BIT, 'pywin32_exe')
        try:
            #print_and_write('Task 10 : Installing the pywin32 modules')
            os.chdir(setupfilepath)
            Popen(pywin32_exe)
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(20)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(10)
            ListOfTasks = tskList()
            if "pywin32" in ListOfTasks:
                tskKill(pywin32_exe)
            if os.path.exists(HOMEDRIVE + r'\Python27\Removepywin32.exe'):
                print_and_write('\npywin32 : Installed')
            else:
                print_and_write('\npywin32 : NOT Installed') 
        except Exception as excp:
            print_and_write('\npywin32 : Not Installed due to %s' %excp)

    else:
        print_and_write('\npywin32 : Installed')

def InstallWMI():
    #Installation of sendkeys
    if not os.path.exists(HOMEDRIVE + r'\Python27\RemoveWMI.exe'):
        WMI_exe = ReadConfig('EXENAME_'+OS_BIT, 'WMI_exe')
        try:
            #print_and_write('Task 11 : Installing the WMI modules')
            os.chdir(setupfilepath)
            Popen(WMI_exe)
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(20)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(10)
            ListOfTasks = tskList()
            if "WMI" in ListOfTasks:
                tskKill(WMI_exe)
            if os.path.exists(HOMEDRIVE + r'\Python27\RemoveWMI.exe'):
                print_and_write('\nWMI : Installed')
            else:
                print_and_write('\nWMI : NOT Installed') 
        except Exception as excp:
            print_and_write('\nWMI : Not Installed due to %s' %excp)

    else:
        print_and_write('\nWMI : Installed')




def Installpyserial():
    #Installation of sendkeys
    if not os.path.exists(HOMEDRIVE + r'\Python27\Removepyserial.exe'):
        pyserial_exe = ReadConfig('EXENAME_'+OS_BIT, 'pyserial_exe')
        try:
            #print_and_write('\nTask 13 : Installing the pyserial modules')
            os.chdir(setupfilepath)
            Popen(pyserial_exe)
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(5)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(20)
            SendKeys.SendKeys("{ENTER}")
            time.sleep(10)
            ListOfTasks = tskList()
            if "pyserial" in ListOfTasks:
                tskKill(pyserial_exe)
            if os.path.exists(HOMEDRIVE + r'\Python27\Removepyserial.exe'):
                print_and_write('\nPyserial : Installed')
            else:
                print_and_write('\nPyserial : NOT Installed')
        except Exception as excp:
            print_and_write('\nTask 13: Exception came while installing pyserial module: %s' %excp)

    else:
        print_and_write('\nPyserial : Installed')

def print_and_write(text):
    print text
    os.chdir(current_dir)
    with open(r"Initialsetup_log.txt","a") as fo:
        fo.write('\n'+text)


    


##import pdb
##pdb.set_trace()
print_and_write('##################### Initial Setting up started on HOST ########################')
Disablefirewall()
CreateStructure()
dotnet()
RunCmdAsAdmin()
DisableUAC()
toolscopy()
InstallPython()
SetPythonpath()
InstallSendKey()
InstallPywinauto()
Installpywin32()
InstallWMI()
Installpyserial()
print_and_write('\n##################### Initial Setting up Completed on HOST#####################')



