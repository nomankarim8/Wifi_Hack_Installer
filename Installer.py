import os
print('''\033[1;36;40mWifi_Hack Installer By NOMAN
Your Device Must Be Rooted
If Any Question,
Contact Me On Facebook
Fb_User:@noman.karim.8 \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/nomankarim8/Wifi_Hack.git")

os.system("cd ..;chmod +x Wifi_Hack/nomanhack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python Wifi_Hack/nomanhack.py -i wlan0 -K")