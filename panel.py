from methods.ddospw import attack_DNS_NTP_TCPMB
from lib.textColor import textGen, text2Gen
from methods.iostresser import ioStresser
from lib.credits import scriptCredits
from os import name, system
import os
import json

global R,B,C,G,Y,Q
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; G='\033[1;32m'; Y='\033[1;33m'; Q='\033[1;36m'

with open('./infos.json') as file:
    scriptInfos = json.load(file)

creator = scriptInfos['creator']; discord = scriptInfos['discord']; scriptVersion = scriptInfos['scriptVersion']

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
methods = textGen("DoS Methods")
inputUser = text2Gen("input > ")
creator = textGen(creator)
discord = textGen(discord)
scriptVersion = textGen(scriptVersion)

menu = '''%s

╭───────────────────────────╮
|      %sCreator%s: Noutz %s|
|    %sDiscord%s: noutzhz%s |
|      %sVersion%s: V1%s    |
│───────────────────────────│
│   💣 %s SyVortex C2 💣   │
|                           |
│ [ %s1%s ] %sNoutz%s       │
│ [ %s2%s ] %sSyVortex C2%s │
│───────────────────────────│
│ [ %s99%s ] %sCredits%s    │
│ [ %s00%s ] %sExit%s       │
╰───────────────────────────╯

'''%(logo, B,C,creator, B,C,discord, B,C,scriptVersion, methods,G,C,Q,C,G,C,Q,C,Y,C,Q,C,R,C,Q,C)

inputMenu = (menu)

def clear(clean) -> None:
	return system(clean)

Exit = False

def exit() -> None:
	global Exit
	Exit = True

MatchCase = {
'1': attack_DNS_NTP_TCPMB,
'2': ioStresser
}

MatchCase_Function = {
'99': scriptCredits,
'00': exit
}

def main():
	while Exit == False:
		clear(clean)
		option = str(input('\33]0;SyVortex C2 🌌,  Connection Crasher!\a' + menu + inputUser))
		clear(clean)
		try:
			res = '%s\n%s'%(MatchCase[option](),'\n%s< %sPress enter to continue%s > '%(C,Q,C))
			input(res)
		except Exception:
			try:
				MatchCase_Function[option]()
			except:
				pass

if __name__ == '__main__':
	global clean
	clean = {'nt':'cls','posix':'clear'}[name]
	main()
