# Rango webapp in Django


## Commands

### Git

git pull

git add .
git commit -m "commit"
git push

#### Switching to an older commit 
git checkout -b <branchname> <hash>
git checkout master

### Django
python manage.py runserver
python manage.py makemigrations rango
python manage.py migrate

systemctl daemon-reload

### CentOS

#### ps - (processes) - [guide](https://www.lifewire.com/uses-of-linux-ps-command-4058715)

##### -ef ((-e)all processes, (f)ull details)
ps -ef | grep 'service'

##### faux

ps faux | grep 'service
#### Show network info which app on port/running
netstat -tulnp
#### Show last 30 lines
tail -30 /var/log/nginx/error.log
#### Permissions
ls -la  
#### Remove a directory
rm -rf mydir  


#### Open a port on firewall
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --reload