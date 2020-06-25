Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "M49Client.exe" & Chr(34), 0
Set WshShell = Nothing