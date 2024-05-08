# One powershell profile for all users

Profile.ps1 file is commonly referred to as a "profile" script in PowerShell. It is a script file that can contain various PowerShell commands and settings that are automatically executed when you start a PowerShell session. Profiles are used to customize your PowerShell environment and configure settings according to your preferences. $PROFILE: This is your USERS profile script that is loaded every time you start a PowerShell session. you can find the file in: "C:\Users\k4s\OneDrive\Dokument\powershell"

## Creating powershell profile
```powershell
start-process powershell -verb runs #run powershell as admin
```

```powershell
new-item -path $PROFILE.AllUsersAllHosts -type file -force #creates a profile for allhosts&users
```


```powershell
nvim -path $PROFILE.AllUsersAllHosts            #paste you Ps config in this file
```

```powershell
set-exectinpolicy RemoteSigned                  #Ps will only allow localy created scripts
```

#### Exampal of content in powershell profile
##### Create Alias
Set-Alias is used in PowerShell. It allows you to create shortcuts or aliases for longer commands, making it easier to type and execute those commands.
###### Exampel
```powershell
Set-Alias p ping
Set-Alias vi nvim   #vim in powershell
Set-Alias vim nvim-qt.exe #vim in GUI
Set-Alias ipcon Get-NetIPConfiguration
```

###### Create a Function
Functions are used to encapsulate a set of instructions into a reusable unit, enabling you to perform specific tasks efficiently. Here are some common use cases for functions in PowerShell:
###### Exampel
```powershell
#Functions
function cd-desk {
		cd C:\Users\k4s\OneDrive\Skrivbord\	
}
set-alias -name desk -value cd-desk

function home-dic {
		cd c:\users\k4s\
}
set-alias -Name home -Value home-dic

function ssh-pihole {
		ssh username@10.0.0.254
}
set-alias -name pihole -value ssh-pihole
```