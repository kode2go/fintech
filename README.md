# fintech

# Setup

```
sudo ufw app list 
sudo ufw allow OpenSSH
sudo ufw enable 
```

Must use a virtual env


```
sudo apt update
sudo apt install python3-pip
python -m venv .venv
pip3 install streamlit
```

```
sudo apt install nginx
```

## Setup Nginx Config - Option 1 - port 8501

`(.venv) ubuntu@SERVERNAME:~/sapp$ sudo nano /etc/nginx/sites-available/streamlit`

```
server {
    listen 80;
    server_name x.x.x.x;  # Change this to your domain


    location / {
        proxy_pass http://0.0.0.0:8501/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

}
```

## Setup Streamlit Config - Option 2 - port 8502

`(.venv) ubuntu@SERVERNAME:~/sapp$ cat ~/.streamlit/config.toml`

```
[server]
port=8502 # change port number. By default streamlit uses 8501 port
headless=true # This will eliminate automatically open browser

[browser] # This ip and port will show in command prompt
serverAddress = "154.114.57.34" # Put your Local IP or Domain Name
serverPort = 8502
```

## Setup Nginx Config - Option 2 - 8502

`(.venv) ubuntu@SERVERNAME:~/sapp$ cat /etc/nginx/sites-available/streamlit`

```
server {
    listen 80;
    server_name 154.114.57.34;  # Change this to your domain


    location / {
        proxy_pass http://0.0.0.0:8502/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

}
```

```
sudo ln -s /etc/nginx/sites-available/NEW_ONE /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw allow 'Nginx Full'
```

## Running

```
nohup streamlit run main.py &
```


## References

https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-macoslinux
https://medium.com/featurepreneur/streamlit-with-nginx-bde7a9a41e6c

https://github.com/marcskovmadsen/awesome-streamlit
