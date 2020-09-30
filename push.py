import os
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(os.system("git add ."))
print(os.system("""git commit -m " """+date_time+""" " """))
print(os.system("git push origin master"))