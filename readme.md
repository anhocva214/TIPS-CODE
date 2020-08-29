# PM2
* Install
``` bash
    sudo npm install -g pm2
```
* View list projects runing
``` bash
    sudo npm list
```
* Stop project
``` bash
    sudo npm stop <project_name or project_id> 
```
* Restart project
``` bash
    sudo npm restart <project_name or project_id> 
```
* Info project
``` bash
    sudo npm info <project_name or project_id> 
```
# NGINX
* Install
``` bash
    sudo apt-get install nginx
```
* Edit file default
``` bash
    sudo vi /etc/nginx/sites-available/default
```

* Config server in file default
``` bash
    server {
    listen 80;
    listen [::]:80;
    server_name localhost;
    location /app1 {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
    location /app2 {
        proxy_pass http://localhost:3002;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
    
    location / {
        proxy_pass http://localhost:3003;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
* Check error and restart  after config
``` bash
    sudo nginx -t
    sudo systemctl restart nginx
```
# DEPLOY
* Node Js (Express) to VPS
``` bash
    pm2 start ./bin/www
```
* Next Js to VPS
``` bash
    npm run build
    pm2 start npm --name <project_name> --start
```
* React Js to VPS
``` bash
    npm run build
    pm2 start ./node_modules/react-scripts/scripts/start.js --name "project_name"
```
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



