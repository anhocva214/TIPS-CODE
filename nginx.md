
# SETUP NGINX
### Install
``` bash
    sudo apt-get install nginx
```
### Create "your_domain" file 
``` bash
    cd /etc/nginx/sites-available
    touch your_domain
```
### Create "your_domain" file 
``` bash
    cd /etc/nginx/sites-available
    touch your_domain
```
### Config server in file "your_domain"
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

### Enable your server blocks 
```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

### Check error and restart  after config
``` bash
sudo nginx -t && sudo systemctl restart nginx
```

# SETUP SSL (HTTPS)

### Create the SSL certificate in /etc/nginx

``` bash
cd /etc/nginx
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt

```
### Install certbot
```bash
apt-get update && sudo apt-get install certbot && apt-get install python-certbot-nginx
```
### Generate certificates by certbot

```bash
sudo certbot --nginx -d example.com -d www.example.co
```
### Automatically renew Let’s Encrypt certificates
Let’s Encrypt certificates expire after 90 days. We encourage you to renew your certificates automatically. Here we add a cron job to an existing crontab file to do this.
1. Open the crontab file
```bash
crontab -e
```
2. Add the certbot command to run daily. In this example, we run the command every day at noon. The command checks to see if the certificate on the server will expire within the next 30 days, and renews it if so. The --quiet directive tells certbot not to generate output.
```bash
0 12 * * * /usr/bin/certbot renew --quiet
```
3. Save and close the file. All installed certificates will be automatically renewed and reloaded.


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
