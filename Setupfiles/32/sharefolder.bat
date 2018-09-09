
:: Sharing Automation and TWS folder to everyone
net share Automation=C:\Automation /grant:everyone,FULL
cacls C:\Automation /E /T /C /G Everyone:F
net share TWS=C:\TWS /grant:everyone,FULL
cacls C:\TWS /E /T /C /G Everyone:F

:: adding registry settings for disabling "turn on fast startup"
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /V HiberbootEnabled /T REG_dWORD /D 0 /F


::Disable ipv6
REG ADD "hklm\system\currentcontrolset\services\tcpip6\parameters" /v DisabledComponents /t REG_DWORD /d 0xFFFFFFFF /F


::Secure_boot_Rework
reg add "HKLM\System\CurrentControlSet\Control\CI\Policy" /v UpgradedSystem /t REG_DWORD /d 0x1 /f



::Power settings set to never
powercfg -change monitor-timeout-ac 0

powercfg -change disk-timeout-ac 0

powercfg -change standby-timeout-ac 0

powercfg -change hibernate-timeout-ac 0

powercfg -change monitor-timeout-dc 0

powercfg -change disk-timeout-dc 0

powercfg -change standby-timeout-dc 0

powercfg -change hibernate-timeout-dc 0

powercfg -setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0

powercfg -setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0

powercfg -setacvalueindex SCHEME_CURRENT SUB_SLEEP HYBRIDSLEEP 000

powercfg -setacvalueindex SCHEME_CURRENT SUB_BUTTONS PBUTTONACTION 000

powercfg -setacvalueindex SCHEME_CURRENT SUB_BUTTONS SBUTTONACTION 000

powercfg -setacvalueindex SCHEME_CURRENT SUB_BUTTONS UIBUTTON_ACTION 000

powercfg -setdcvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0

powercfg -setdcvalueindex SCHEME_CURRENT SUB_SLEEP HYBRIDSLEEP 000

powercfg -setdcvalueindex SCHEME_CURRENT SUB_BUTTONS PBUTTONACTION 000

powercfg -setdcvalueindex SCHEME_CURRENT SUB_BUTTONS SBUTTONACTION 000

powercfg -setdcvalueindex SCHEME_CURRENT SUB_BUTTONS UIBUTTON_ACTION 000