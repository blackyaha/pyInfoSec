## Windows Reverse Shell
### Windows Reverse Shell Listener
Attacker put backdoor script to victim's computer, and waiting for victim triggers backdoor script.

### Windows Reverse Shell Victim
Victim triggers backdoor script connecting to attacker's computer.

### Package Victim script to Executable File
Use pyinstaller package python program into executables

##### Installation
> pip install pyinstaller

##### Package Python Program into Single File without Console
> pyinstaller -w -F win-reverse-shell-victim.py
