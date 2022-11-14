import winreg as winreg
import wmi

wmi_obj = wmi.WMI()
wmi_sql = 'select DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE'
wmi_out = wmi_obj.query( wmi_sql )

INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
	r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, 
	winreg.KEY_ALL_ACCESS)

def set_key(name, value):
	_, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
	winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

print('Enter 1 to turn on\n      0 to turn off')
      
proxyIsEnableInput = input()

set_key('ProxyEnable', int(proxyIsEnableInput))
#set_key('ProxyOverride', u'*.local<local>')
gatewayIP = 1
for dev in wmi_out:
        gatewayIP = dev.DefaultIPGateway[0] + ":8282"
        set_key('ProxyServer', gatewayIP)
    #print(dev.DefaultIPGateway[0])

