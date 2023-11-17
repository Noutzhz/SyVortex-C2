from lib.textColor import textGen
from time import sleep
import json

global R,B,C,G,Y,Q
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; G='\033[1;32m'; Y='\033[1;33m'; Q='\033[1;36m'

with open('./infos.json') as file:
    scriptInfos = json.load(file)

creator = scriptInfos['creator']; discord = scriptInfos['discord']; tiktok = scriptInfos['tiktok']; github = scriptInfos['github']

banner = '''
   ______                       __   _   _          
 .' ___  |                     |  ] (_) / |_        
/ .'   \_| _ .--.  .---.   .--.| |  __ `| |-'.--.   
| |       [ `/'`\]/ /__\\/ /'`\' | [  | | | ( (`\]  
\ `.___.'\ | |    | \__.,| \__/  |  | | | |, `'.'.  
 `.____ .'[___]    '.__.' '.__.;__][___]\__/[\__) ) 

'''

logo = textGen(banner)

def scriptCredits():
    print(f'''{logo}
{B}Creator{G} : noutz {creator}
{B}Discord{G} : noutzhz {discord}
{B}Tiktok{G}  : @eaenoutz {tiktok}
{B}Github{G}  : noutzhz {github}
'''+f'\33]0;Kusty on Top 🚀\a')
    sleep(2)
    return input('%s< %sPress enter to continue%s > '%(C,Q,C))