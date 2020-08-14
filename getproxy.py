print("""
 ▄          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌        ▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌        ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌        ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌          ▐░▌          ▐░▌
▐░▌        ▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░▌        ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌   ▀   ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌          ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄▄▄▀▀▀▀▀▀█░█▀▀ ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌      ▐░▌  ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀        ▀    ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
Instagram:lqm33.sec | https://turkrepo.com                                                               
""")
import requests,re,sys,os
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
r=requests.get("https://hidemy.name/en/proxy-list/",headers=headers)
kirp=re.findall("<i(.*?)</div></div>",r.text),

kirp=str(kirp)

kirpik=r.text.replace(kirp,"")
proxy=re.findall("<tr><td>(.*?)</td><td><i",kirpik)
tytpe=re.findall("</div></div></td><td>(.*?)</td><td>",kirpik)

sa=0#coder:lqm33 turkrepo.com
print("""
1# HTTP REPLACE
2# HTTPS REPLACE
3# SOCKS 4 REPLACE
4# SOCKS 5 REPLACE
""")
islem=int(input("hangi islemi yapmak istersiniz...:"))
if islem==1:
    oa="HTTP"
elif islem==2:
    oa="HTTPS"
elif islem==3:
    oa="SOCKS4"
elif islem==4:
    oa="SOCKS5"  
for i in range(0,64):
        #for t in type:
        #i=i.replace("</td><td>",":")
        #i=i.replace("""IP address:Port:Country, City</td><td class=speed_col>Speed:Type:Anonymity:Latest update</td></tr></thead> <tbody><tr><td>""",":")
    #sa+=1
    a=(tytpe[i]+""+proxy[i])
    a=str(a)
    a=a.replace("</td><td>",":")
    a=a.replace(",","")
    a=a.replace("""IP address:Port:Country, City</td><td class=speed_col>Speed:Type:Anonymity:Latest update</td></tr></thead> <tbody><tr><td>""",":")
    
    
#print(a)

    for t in a.split():


        if t.startswith(oa):
            t=t.replace(oa,"")
            t=t.replace("S","")
            
            print(t)
            
  
            
            
        
     
