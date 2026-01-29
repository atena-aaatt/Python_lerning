## Çarpım tablosu uygulaması:

import time
for a in range(1,11):    
    print("\t")
    for b in range(1,11):
        time.sleep(1)
        print(f"{a}x{b}={a*b}", end="\t")
	#print("{}x{}={}".format(a,b,a*b)) 
