
# NGINX
* Install
``` bash
    sudo apt-get install nginx
```
* Create "your_domain" file 
``` bash
    cd /etc/nginx/sites-available
    touch your_domain
```
* Create "your_domain" file 
``` bash
    cd /etc/nginx/sites-available
    touch your_domain
```
* Config server in file "your_domain"
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
```bash
    server {
    listen 80;
    listen [::]:80;
    server_name host_name;
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        }
    }
```

* Enable your server blocks 
```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

* Check error and restart  after config
``` bash
sudo nginx -t
sudo systemctl restart nginx
```