# Audo Push Code To Github By Python
* [Install Python](https://www.python.org/)
* Create file pushGit.py or name orther
* Copy and paste code below into your file
``` python
import os
from datetime import datetime
import shutil


now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

msg = input("Enter message: ")

os.system("git add .")
os.system("""git commit -m " """+msg+""" " """)
os.system("git push origin master")
```
* Run file follow code below:
```bash
python <filename your>
```
Example: ``` python pushGit.py ```



