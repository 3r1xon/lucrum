# Lucrum
Lucrum is an open-source project made using PyQt5 Framework, written in Python and Powershell.

# What does Lucrum do?
Lucrum can debloat Windows 10 (thanks to a script that I DID NOT MAKE but Sycnex did https://github.com/Sycnex/Windows10Debloater) and clean your PC by deleting all the content in the Temp and Prefetch folders. It also has a download manager, which stores alle the names of the application and the URLs that you put via Lucrum in JSON file. The idea is to make it portable in order to install softwares easily once you make a clean install of Windows.
1 - Wipe Windows 10
2 - Install Windows 10
3 - Use Lucrum to debloat and Install all the softwares easily. That's it.

# How to make it executable
Download or clone all the files from GitHub.
Once the folder is on your desktop, or wherever you want, open the cmd on that path and simply write "pyinstaller.exe --onefile --icon="icon_path.ico" __main__.py" or you can use https://pypi.org/project/auto-py-to-exe/ which makes all easier.
