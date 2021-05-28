# GITHUB
* Clone a repository on the command line
``` bash
git clone  <Link github my project>
```

* Create a new repository on the command line
``` bash
git init
git commit -m "first commit"
git branch -M master
git remote add origin <Link github my project>
git push -u origin master
```
* Push **an existing** repository from the command line
``` bash
git remote add origin <Link github my project>
git branch -M master
git push -u origin master
```
* Push **replace** an existing repository
``` bash
git remote add origin <Link github my project>
git push -f origin master
```

#  Set Up Basic HTTP Authentication With Nginx on Ubuntu - [Link](https://www.digitalocean.com/community/tutorials/how-to-set-up-basic-http-authentication-with-nginx-on-ubuntu-14-04)
* Installing Apache Tools
``` bash
sudo apt-get install apache2-utils
```
* Setting Up HTTP Basic Authentication Credentials

``` bash
sudo htpasswd -c /etc/nginx/.htpasswd nginx
```
You can check the contents of the newly-created file to see the username and hashed password.
``` bash
cat /etc/nginx/.htpasswd
```
* Updating the Nginx Configuration
``` bash
sudo nano /etc/nginx/sites-available/default
```
``` bash
. . .
server_name localhost;

location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
        # Uncomment to enable naxsi on this location
        # include /etc/nginx/naxsi.rules
        auth_basic "Private Property";
        auth_basic_user_file /etc/nginx/.htpasswd;
}
. . .
```
* Testing the Setup
``` bash
sudo service nginx reload
```

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

# Publish Npm Package
* Inittialize and setting info your project npm follow code below:
```bash
npm init
```
* Publish:
```bash
npm publish
```
* Update

Change version in your project and publish again
```bash
npm publish
```
# Block Action Devloper For Website
* Copy and paste follow code below into <script> tag:
```javascript
 document.addEventListener('contextmenu', event => event.preventDefault());
document.addEventListener("keydown", function (e) {
    //document.onkeydown = function(e) {
    // "I" key
    if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
        alert("Hành động đã bị chặn !");
        e.preventDefault();
    }
    // "J" key
    if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
        alert("Hành động đã bị chặn !");
        e.preventDefault();
    }
    // "S" key + macOS
    if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
        alert("Hành động đã bị chặn !");
        e.preventDefault();
    }
    // "U" key
    if (e.ctrlKey && e.keyCode == 85) {
        alert("Hành động đã bị chặn !");
        e.preventDefault();
    }
    // "F12" key
    if (event.keyCode == 123) {
        alert("Hành động đã bị chặn !");
        e.preventDefault();
    }
}, false);
```