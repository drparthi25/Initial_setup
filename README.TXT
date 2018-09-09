
Initialsetup_SUT_V0.06.exe: (For SUT)
	"Initialsetup_SUT_V0.06.exe" will do initial settings and install Python (32 or 64 bit) with below python modules & tool in SUT/DUT


	Initial Settings:
		1. Firewall disable
		2. Folders(Automation and TWS) Created and shared
		3. Dotnetframwork Enabled
		4. RUNCMDASADMIN was set.
		5. Diable Password on startup
		6. Network Password Protected Sharing turned off
		7. Tools copied from \\..\Initial_setup_V0.04\Setupfiles\tools to SUT C:\Automation\tools
		8. "Turn off fast startup" is enabled
		9. IPV6 disabled
		10. Power options made as never
		11. Driver signing enabled


	Python Modules: (All setup file name referred in "Initialsetup_Config.ini")

		1.PIL (both 32 & 64 bit available)
		2.pywin32 (both 32 & 64 bit available)
		3.sendkey (both 32 & 64 bit available)
		4.WMI (Unified)
		5.pyserial (Unified)
		6.HWAPI (both 32 & 64 bit available)
		7.pywinauto (Unified)


Initialsetup_HOST_V0.06.exe:(For HOST)
	"Initialsetup_HOST_V0.06.exe" will do initial settings and install Python (32 or 64 bit) with below python modules & tool in SUT/DUT


	Initial Settings:
		1. Firewall disable
		2. Folder Created and shared
		3. Dotnetframwork Enabled
		4. RUNCMDASADMIN was set.
		5. Tools copied from \\..\Initial_setup_V0.04\Setupfiles\tools to SUT C:\Automation\tools


	Python Modules: (All setup file name referred in "Initialsetup_Config.ini")


		1.pywin32 (both 32 & 64 bit available)
		2.sendkey (both 32 & 64 bit available)
		3.WMI (Unified)
		4.pyserial (Unified)
		5.pywinauto (Unified)

----------------------------------------------------------------------------

Steps :

	1. Run "Initialsetup_HOST_V0.06.exe" or "Initialsetup_SUT_V0.06.exe" in adminstrator mode.
	2. Check the "Initialsetup_log.txt" after the installation completes.


----------------------------------------------------------------------------

Notes: 

1. DLL load failed: %1 is not a valid Win32 application.
	Can be resolved by installing Python and pywin32 of same architecture (either 32 or 64 bit version).

2. Sendkeys for 64 bit available only in .whl file which can be installed by PIP, from python 2.7.9 version PIP supports by default.
   So for 64 bit OS , need to use python 2.7.9 or above.

3. Python 2.6 or 2.7 with correct bitness is required for this installation(HWAPI)
	or No python installation found in the registry(For any module)
   Above issues can resolved by adding registry "HKLM.reg" available @ Initial setup V0.04\Setupfiles\64.
   


