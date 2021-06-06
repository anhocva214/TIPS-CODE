# Audo Push Code To Github By Python
* [Install Python](https://www.python.org/)
* Create file pushGit.py or name orther
* Copy and paste code below into your file
``` python
import os
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
os.system("git add .")
os.system("""git commit -m " """+date_time+""" " """)
os.system("git push origin master")
```
* Run file follow code below:
```bash
python <filename your>
```
Example: ``` python pushGit.py ```



