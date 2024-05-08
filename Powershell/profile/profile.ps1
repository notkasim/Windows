#Aliases #Aliases #Aliases
set-alias vim nvim-qt.exe
set-alias vi nvim
set-alias netip Get-NetIPConfiguration
set-alias p ping
set-alias reboot computer-restart
set-alias shutdown computer-stop
set-alias nic get-netadapter
set-alias touch new-item



#Remap #Remap #Remap
Set-PSReadLineKeyHandler -Chord "alt+k" -Function AcceptSuggestion #Chooses the whole suggested command.
set-PSReadlineKeyHandler -chord "alt+l" -Function Forwardword #Chooses the next suggested word.


#Functions #Functions #Functions



# Systems
##---------------------------------------------------------------------------------------
Function Powershell_admin {
Start-Process wt powershell -verb runas }
set-alias -name sudo -value Powershell_admin
#---------------------------------------------------------------------------------------
Function tree_f {
tree /f}
set-alias -name geed -value tree_f
#---------------------------------------------------------------------------------------




# Navigation
Function ps_profile {
Set-Location C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1}
set-alias psprofile  -value ps_profile
#---------------------------------------------------------------------------------------
Function Home_Directory {
Set-Location c:\users\k4s\ }
Set-Alias -Name home -Value Home_Directory
#---------------------------------------------------------------------------------------
Function Desktop {
Set-Location C:\Users\k4s\OneDrive\Skrivbord\ }
Set-Alias -name desk -value Desktop
#---------------------------------------------------------------------------------------
Function ssh_config_file {
vim C:\Users\k4s\.ssh\config}
Set-Alias -name sshconfig -value ssh_config_file
#---------------------------------------------------------------------------------------
Function SSH_directory {
Set-Location C:\Users\k4s\.ssh\ }
Set-Alias -name .ssh -value SSH_directory
#---------------------------------------------------------------------------------------
Function VMS_Location {
Set-Location C:\vms }
Set-Alias -name vms -value VMS_Location
#---------------------------------------------------------------------------------------
Function nvim_runtimepath {
Set-Location C:\Users\k4s\AppData\Local\nvim\lua }
Set-Alias -name vimrc -value nvim_runtimepath
#---------------------------------------------------------------------------------------


# Network Configuration
Function ipconfig_all {
ipconfig /all }
set-alias -name ipall -value ipconfig_all
#---------------------------------------------------------------------------------------
Function ipconfig_release {
ipconfig /release }
Set-Alias -name ipre -value ipconfig_release
#---------------------------------------------------------------------------------------
Function ipconfig_renew {
ipconfig /renew }
Set-Alias -name ipnew -value ipconfig_renew
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------