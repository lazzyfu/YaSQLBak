  * [说明](#说明)
  * [初始化系统](#初始化系统)
     * [推荐系统环境](#推荐系统环境)
     * [安装系统依赖包](#安装系统依赖包)
     * [安装python37](#安装python37)
     * [创建python37虚拟环境](#创建python37虚拟环境)
     * [克隆项目](#克隆项目)
  * [部署前端服务](#部署前端服务)
     * [安装Nginx](#安装nginx)
     * [编辑Nginx配置文件](#编辑nginx配置文件)
     * [启动Nginx服务](#启动nginx服务)
     * [访问前台页面](#访问前台页面)
  * [部署后端服务](#部署后端服务)
     * [安装Django项目依赖包](#安装django项目依赖包)
     * [安装UWSGI和GUNICORN服务](#安装uwsgi和gunicorn服务)
     * [收集Django静态文件](#收集django静态文件)
     * [部署Redis服务](#部署redis服务)
     * [初始化库表结构](#初始化库表结构)
     * [部署supervisor服务](#部署supervisor服务)
     * [配置supervisor服务](#配置supervisor服务)
     * [启动服务](#启动服务)


## 说明
本系统采用的是最简单粗暴的安装方式，适用于有一定基础Linux系统使用的人员

请按照下面的文档操作，谢谢...

## 初始化系统
### 推荐系统环境
* 系统：CentOS Linux release 7.6
* 配置：4核心/8GB内存

### 安装系统依赖包
```bash
yum -y install epel-release

yum -y install \
net-tools bzip2-devel gcc gcc-c++ make automake unzip curl curl-devel \
libffi-devel perl perl-devel expat expat-devel zlib zlib-devel asciidoc \
xmlto gettext-devel openssl openssl-devel mlocate python-devel openldap-devel \
readline-devel git mysql-devel p7zip
```

### 安装python37
```bash
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
tar -zxf Python-3.7.9.tgz
cd Python-3.7.9/
./configure
make -j 4 && make install
```

### 创建python37虚拟环境
```bash
/usr/local/bin/python3.7 -m pip install --upgrade pip
/usr/local/bin/pip3.7 install virtualenv -i https://mirrors.aliyun.com/pypi/simple
/usr/local/bin/virtualenv /venvyasql --python=/usr/local/bin/python3.7
```

### 克隆项目
```bash
mkdir /data/www
git clone https://github.com/lazzyfu/YaSQL.git yasql
```


## 部署前端服务
### 安装Nginx
```bash
yum -y install nginx                    
useradd www -s /bin/bash
chown -R www. /data/www/
chown -R www. /venvyasql/
```

### 编辑Nginx配置文件
`vim /etc/nginx/conf.d/yasql.conf`
```editorconfig
server {
    listen      80;
    server_name yasql.examplexx.net;   # 此处更换为自己的域名
    charset     utf-8;

    root /data/www/yasql/yasql-fe/dist;
    index index.html;
    access_log   /var/log/nginx/yasql.log;

    location / {
       try_files $uri $uri/ /index.html;
    }

    location /api {
       proxy_pass http://127.0.0.1:8000;
    }

    location /admin {
       proxy_pass http://127.0.0.1:8000;
    }

    location /statics {
       expires 30d;
       alias /data/www/yasql/yasql/static;
    }

    location /ws {
      proxy_pass http://127.0.0.1:8001;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
      proxy_redirect     off;
      proxy_set_header   Host $host;
      proxy_set_header   X-Real-IP $remote_addr;
      proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Host $server_name;
      proxy_read_timeout  36000s;
      proxy_send_timeout  36000s;
    }
}
```

### 启动Nginx服务
```bash
systemctl enable nginx.service
systemctl start nginx.service
```

### 访问前台页面
在浏览器访问：http://yasql.examplexx.net/ （此处应该是你在nginx里面配置的server_name）
>如果访问不了，本地先加下dns解析或者绑定下hosts
>如果nginx启动不了，检查下错误日志

## 部署后端服务
### 安装Django项目依赖包
```bash
cd /data/www/yasql/yasql
/venvyasql/bin/pip3.7 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```
>最好选择一个干净的系统，最好本地不要有自己安装的mysql包，否则在安装mysql-client时报ln类的错误。当然您也可以ln解决

### 安装UWSGI和GUNICORN服务
```bash
/venvyasql/bin/pip3.7 install gunicorn -i https://mirrors.aliyun.com/pypi/simple
/venvyasql/bin/pip3.7 install uwsgi -i https://mirrors.aliyun.com/pypi/simple
```

### 收集Django静态文件
```bash
cd /data/www/yasql/yasql
mkdir static
/venvyasql/bin/python3.7 manage.py collectstatic
```

### 部署Redis服务
>你也可以使用远程redis，本地不需要部署。我为了省事，就部署在本地了

```bash
yum -y install redis

# 更改redis配置
vim /etc/redis.conf
----------------------------
# 配置改为如下，此处设置密码
bind 127.0.0.1
requirepass 1234.com
----------------------------

# 启动redis服务
systemctl enable redis.service
systemctl start redis.service
```

### 初始化库表结构
a. 编辑配置文件config.py，分别配置MySQL和Redis
>请按照要求进行修改

`vim /data/www/yasql/yasql/config.py`

b. 执行migrate生成表结构，该操作会连接到上面的数据库创建表结构
>如果报数据库无法连接，请检查config.py里面的MySQL配置是否正确

`/venvyasql/bin/python3.7 manage.py migrate`

### 部署supervisor服务
```bash
/usr/local/bin/pip3.7 install supervisor
/usr/local/bin/echo_supervisord_conf > /etc/supervisord.conf
```

```editorconfig
vim /etc/supervisord.conf
------------------------------
# 更改为
[include]
files = supervisord.d/*.conf
------------------------------
```

```bash
mkdir /etc/supervisord.d
cd  /etc/supervisord.d
```


### 配置supervisor服务
vim /etc/supervisord.d/yasql.conf
```editorconfig
[program:yasql-server]
user=www
autorestart=true
environment=DJANGO_SETTINGS_MODULE="yasql.settings"
directory=/data/www/yasql/yasql
command=/venvyasql/bin/python3 /venvyasql/bin/gunicorn -w 8 -b 127.0.0.1:8000 yasql.wsgi:application
redirect_stderr=true
stdout_logfile=/data/www/yasql/yasql/logs/yasql-server.log

[program:yasql-daphne]
user=www
autorestart=true
environment=DJANGO_SETTINGS_MODULE="yasql.settings"
directory=/data/www/yasql/yasql
numprocs=1
command=/venvyasql/bin/daphne -b 127.0.0.1 -p 8001 --proxy-headers -v2 yasql.asgi:application
redirect_stderr=true
stdout_logfile=/data/www/yasql/yasql/logs/yasql-daphne.log

[program:yasql-celery-dbtask]
user=www
environment=DJANGO_SETTINGS_MODULE="yasql.settings"
directory=/data/www/yasql/yasql
command=/venvyasql/bin/celery worker -A yasql -n localhost -Q dbtask -l info --time-limit=86400 --concurrency=20
redirect_stderr=true
stdout_logfile=/data/www/yasql/yasql/logs/yasql-celery-dbtask.log
numprocs=1
autostart=true
autorestart=true
startsecs=10
stopwaitsecs = 600
stopasgroup=true
priority=1000
```

### 启动服务
```bash
cd /data/www/yasql/yasql

# 按照要求进行修改
vim config.py
 
# 创建日志目录
mkdir /data/www/yasql/yasql/logs

# 启动supervisor进程
/usr/local/bin/supervisord -c /etc/supervisord.conf
```



