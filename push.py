import os
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
os.system("git add .")
os.system("""git commit -m " """+date_time+""" " """)
os.system("git push origin master")