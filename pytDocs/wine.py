import os

os.system("sudo rm /etc/environment")
os.system("sudo cp environment /etc/")
try:
	os.system("sudo rm /etc/apt/sources.list.d/webupd8team-ubuntu-atom-focal.list")
finally:
	pass
os.system("sudo dpkg --add-architecture i386")
os.system("sudo apt update -y")
os.system("sudo apt install wine64 wine32 -y")
os.system("wine --version")
os.system("sudo apt install openssh-server -y")
os.system("sudo systemctl enable ssh")
os.system("sudo apt install wakeonlan -y")
os.system("sudo apt install bison -y")
os.system("sudo apt install flex -y")
os.system("sudo dpkg -i pkt.deb")
os.system("sudo apt install -f -y")
os.system("sudo dpkg -i pkt.deb")
os.system("sudo rm /etc/environment")
os.system("sudo cp en/environment /etc/")
os.system("wine setup.exe")
#os.system("rm -r en")
#os.system("rm environment")
