import os
print('''\033[1;36;40mWifi_Hack Installer By THBD
Your Device Must Be Rooted
If Any Question,
Contact Me On Telegram
Tg_User:@biri_baba \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/nomankarim8/Wifi_Hack.git")

os.system("cd ..;chmod +x Wifi_Hack/birihack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python Wifi_Hack/birihack.py -i wlan0 -K")