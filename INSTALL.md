# 部署流程
本系统采用的是最简单粗暴的安装方式，适用于有一定基础Linux系统使用的人员

请按照下面的文档操作，谢谢...

## 推荐系统环境
* 系统：CentOS Linux release 7.6
* 配置：4核心/8GB内存

## 部署依赖包
```bash
yum -y install epel-release

yum -y install \
net-tools bzip2-devel gcc gcc-c++ make automake unzip curl curl-devel libffi-devel \
perl perl-devel expat expat-devel zlib zlib-devel asciidoc xmlto gettext-devel openssl openssl-devel \
mlocate python-devel openldap-devel readline-devel git mysql-devel p7zip
```

## 安装python37
```bash
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
tar -zxf Python-3.7.9.tgz
cd Python-3.7.9/
./configure
make -j 4 && make install
```

## 激活python虚拟环境
```bash
/usr/local/bin/python3.7 -m pip install --upgrade pip
/usr/local/bin/pip3.7 install virtualenv -i https://mirrors.aliyun.com/pypi/simple
/usr/local/bin/virtualenv /venvyasql --python=/usr/local/bin/python3.7
```

## 克隆项目
```bash
mkdir /data/www
git clone https://github.com/lazzyfu/YaSQL.git yasql
```

### 目录结构
```bash
[root@localhost yasql]# tree /data/www/yasql/ -L 1
/data/www/yasql/
├── LICENSE
├── README.md
├── yasql            # 后端文件目录，django程序
└── yasql-fe         # 前端文件目录，vue程序

2 directories, 2 files
```


## 部署前端
### 1.安装Nginx
```bash
yum -y install nginx                    
useradd www -s /bin/bash
chown -R www. /data/www/
chown -R www. /venvyasql/
```

### 2.编辑Nginx配置文件
`vim /etc/nginx/conf.d/yasql.conf`
```editorconfig
server {
    listen      80;
    server_name yasql.examplexx.net;
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

### 3.启动Nginx服务
```bash
systemctl enable nginx.service
systemctl start nginx.service
```

### 4.访问前台页面
在浏览器访问：http://yasql.examplexx.net/ 
>如果访问不了，本地先加下dns解析或者绑定下hosts
>如果nginx启动不了，检查下错误日志

## 部署后端
### 1.安装python依赖包
```bash
cd /data/www/yasql/yasql
/venvyasql/bin/pip3.7 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```
>最好选择一个干净的系统，最好本地不要有自己安装的mysql包，否则在安装mysql-client时报ln类的错误。当然您也可以加ln解决

### 2.安装UWSGI服务
`/venvyasql/bin/pip3.7 install uwsgi -i https://mirrors.aliyun.com/pypi/simple`

### 3.收集django静态文件
```bash
cd /data/www/yasql/yasql
mkdir static
/venvyasql/bin/python3.7 manage.py collectstatic
```

### 4.部署Redis服务
>你也可以使用远程redis，本地不需要部署。我为了省事，就部署在本地了

```bash
yum -y install redis
vim /etc/redis.conf
```

```editorconfig
# 配置改为如下，增加密码
bind 127.0.0.1
requirepass 1234.com
```

```bash
systemctl enable redis.service
systemctl start redis.service
```







