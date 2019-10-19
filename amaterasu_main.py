import os
try:
 x=raw_input("""
LHOST= """)
 print("""
Send the direct link to victim:
""")
 print("http://"+x+""":8080/fuck.html
""")
 os.system("apachectl") 
except:
 print("you have not installed or you written the lhost")

