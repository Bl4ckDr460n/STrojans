import os,sys,time,requests
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = R+"""
   ___________             _
  / ___/_  __/________    (_)___ _____  _____
  \__ \ / / / ___/ __ \  / / __ `/ __ \/ ___/
 ___/ // / / /  / /_/ / / / /_/ / / / (__  )
/____//_/ /_/   \____/_/ /\__,_/_/ /_/____/
     """+G+"""BL4CK DR460N"""+R+"""   /___/"""

def run(x):
	for n in x+"\n":
		sys.stdout.write(n)
		sys.stdout.flush()
		time.sleep(0.1)
def main():
	os.system('clear')
	print logo
	print
	no = raw_input(Y+"["+W+"?"+Y+"]["+W+"TARGET"+Y+"]>> "+G)
	run(Y+"[!] Checking Target ...")
	time.sleep(4)
	if no < 5:
		print R+"[!] Target Not Found"
		sys.exit()
	elif '62' in no or '+62' in no or '08' in no:
		print Y+"["+W+"LOCATION"+Y+"]: "+W+"Indonesian"
		time.sleep(4)
		serang(no)
	else:
		print R+"[!] Tool Not Support "+no
		print G+"[!] Tool Support Indonesian Number"
		sys.exit()

def serang(no):
	os.system('clear')
	print logo
	print
	run(Y+"[!] Attack ...")
	time.sleep(2)
	while True:
		try:
			print G+"Success Send Trojans To: "+Y+no
		except:
			pass

if __name__ == '__main__':
	try:
		main()
	except requests.exceptions.ConnectionError:
		print R+"[x] No Connection"
		sys.exit()
