rem - lines that start with rem are tread as a comment. 
@echo off

rem - runs powershell as admin

rem - this line confs ip, mask & gateway 
netsh interface ip set address "ethernet" static 193.10.161.74 255.255.254.0 193.10.160.1

rem - these two lines conf the dns-servers
netsh interface ip set dns "ethernet" static 193.10.31.164 
netsh interface ip add dns "ethernet" 193.10.31.190