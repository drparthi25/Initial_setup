#Requireadmin
WinMinimizeAll()
Send("#r")
sleep(2000)
Local $windows = "Advanced sharing settings"
WinClose($windows)
Send("control.exe /name Microsoft.NetworkAndSharingCenter /page Advanced")
Send("{ENTER}")
Sleep(5000)
Local $hwd = WinWait("[CLASS:CabinetWClass]","",5)
WinSetState($hwd ,"",@SW_MAXIMIZE)

If StringInStr(ControlGetText($windows, "", "[CLASS:Button;INSTANCE:1]"), "Next") Then
	ControlClick($windows, "", "[CLASS:Button;INSTANCE:1]")
Else
	Send("{TAB 3}")
    sleep(2000)
    Send("{SPACE}")
    Sleep(5000)
	ControlClick($windows, "", "[CLASS:Button;INSTANCE:1]")
 EndIf
Send("{TAB 4}")
sleep(2000)
Send("{SPACE}")
Sleep(2000)
ControlClick($windows, "", "[CLASS:Button;INSTANCE:153]")
Sleep(2000)
ControlClick($windows, "", "[CLASS:Button;INSTANCE:161]")
Sleep(2000)
WinClose($windows)


