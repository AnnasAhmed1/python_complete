# import module
import os

# scan available Wifi networks
os.system('cmd /c "netsh wlan show networks"')

# input Wifi name
name_of_router = "realme_C21"

# connect to the given wifi network
os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

print("If you're not yet connected, try connecting to a previously connected SSID again!")
