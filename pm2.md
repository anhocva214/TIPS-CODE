# PM2
### Install
``` bash
sudo npm install -g pm2
```
### View list projects runing
``` bash
sudo npm list
```
### Stop project
``` bash
sudo npm stop <project_name or project_id> 
```
### Restart project
``` bash
sudo npm restart <project_name or project_id> 
```
### Info project
``` bash
sudo npm info <project_name or project_id> 
```


# DEPLOY
### Node Js (Express) to VPS
``` bash
pm2 start "yarn start" --name <project_name>
```
### Next Js to VPS
``` bash
npm run build
pm2 start "yarn start" --name <project_name>
```
### React Js to VPS
``` bash
npm run build
pm2 start "yarn start" --name <project_name>
```
