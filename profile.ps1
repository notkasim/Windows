#Aliases #Aliases #Aliases
set-alias vim nvim-qt.exe
set-alias ifconfig Get-NetIPConfiguration
set-alias p ping 
set-alias reboot computer-restart
set-alias shutdown computer-stop
set-alias nic get-netadapter
set-alias touch new-item 
set-alias mv rename-item




#Remap #Remap #Remap
Set-PSReadLineKeyHandler -Chord "tab" -Function AcceptSuggestion #Chooses the whole suggested command.
set-PSReadlineKeyHandler -chord "alt +l" -Function Forwardword #Chooses the next suggested word. 



#Functions #Functions #Functions

#Function  {
#}
#set-alias -name  -value 
#---------------------------------------------------------------------------------------


# Systems
#---------------------------------------------------------------------------------------
Function reboot_machine {
computer-restart }
Set-Alias -name reboot now -value reboot_machine
#---------------------------------------------------------------------------------------
Function Powershell_admin {
Start-Process wt powershell -verb runas }
set-alias -name sudo -value Powershell_admin
#---------------------------------------------------------------------------------------



# Navigation
Function ps_profile {
Set-Location C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1}
set-alias psprofile  -value ps_profile
#---------------------------------------------------------------------------------------
Function tree_structur {
tree /f}
set-alias tree  tree_structur
#---------------------------------------------------------------------------------------
Function Home_Directory {
Set-Location c:\users\k4s\ }
Set-Alias -Name cd -Value Home_Directory
#---------------------------------------------------------------------------------------
Function Desktop {
Set-Location C:\Users\k4s\OneDrive\Skrivbord\ }
Set-Alias -name desk -value Desktop
#---------------------------------------------------------------------------------------
Function ssh_config_file {
vim C:\Users\k4s\.ssh\config}
Set-Alias -name ssh_config -value ssh_config_file
#---------------------------------------------------------------------------------------
Function SSH_directory {
Set-Location C:\Users\k4s\.ssh\ }
Set-Alias -name .ssh -value SSH_directory
#---------------------------------------------------------------------------------------
Function VMS_Location {
Set-Location C:\vms }
Set-Alias -name vms -value VMS_Location
#---------------------------------------------------------------------------------------



# Network Configuration
Function ipconfig_all {
ipconfig /all }
set-alias -name ipall -value ipconfig_all 
#---------------------------------------------------------------------------------------
Function ipconfig_release {
ipconfig /release }
Set-Alias -name ifdown -value ipconfig_release 
#---------------------------------------------------------------------------------------
Function ipconfig_renew {
ipconfig /renew }
Set-Alias -name ifup -value ipconfig_renew 
#---------------------------------------------------------------------------------------
Function _vimrc {
vim C:\Users\k4s\AppData\Local\nvim\init.vim  }
Set-Alias -name vimrc -value _vimrc
#---------------------------------------------------------------------------------------
