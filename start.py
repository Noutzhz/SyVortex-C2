import time
import os

global R,B,C,G,Y,Q
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; G='\033[1;32m'; Y='\033[1;33m'; Q='\033[1;36m'

syst = {'nt':'python panel.py','posix':'python3 panel.py'}[os.name]

def install():
    try:
        import requests
        import cloudscraper
        import fake_useragent
    except:
        try:
            os.system('pip install -r requrements.txt')
        except:
            print('%s[ %s!%s ] Manually install the module(s).'%(C,R,C));exit()

def exec(clean) -> None:
	return os.system(clean)

def checkInternet():
    import requests

    #print('\n[%s-%s] Checking your internet connection!\n'%(Y,C))
    time.sleep(0.5)
    try:
        r = requests.get('https://example.com/').status_code

        if r == 200:
            return True
        else:
            return False
    except:
        return "\n[%sX%s] 📌 You don't have an internet connection!\n"%(R,C)

def start():
    try:
        install()

        print('\n[%s!%s] 🔨 Starting the tool...\n'%(Y,C))

        time.sleep(1)
        
        if checkInternet() == True:
            exec(syst)
        else:
            try:
                print(checkInternet())
            except:
                pass

    except:
        print('\n[%s+%s] 📁 Installing the dependencies :)\n'%(G,C))

        time.sleep(2)

        install()

        print('\n[%s*%s] 📁 Installed dependencies!\n'%(G,C))

        print('\n[%s!%s] 🔨 Starting the tool...\n'%(Y,C))
        
        time.sleep(1)

        if checkInternet() == True:
            exec(syst)
        else:
            try:
                print(checkInternet())
            except:
                pass

if __name__ == '__main__':
    print('\33]0;SyVortex C2 🍀,  Starting tool...\a')
    start()
