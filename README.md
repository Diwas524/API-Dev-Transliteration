# API-Dev-Transliteration
FastAPI is an excellent tool for putting your machine learning models into production. In this article, I briefly explain how you can easily put your FastAPI in production to an AWS EC2 instance using Nginx.

Website : [Click Here for Tutorial](https://lcalcagni.medium.com/deploy-your-fastapi-to-aws-ec2-using-nginx-aa8aa0d85ec7)

# Important code to deploy


python3 -m uvicorn main:app

sudo service nginx restart

fuser -k 8000/tcp #kill or restart port

# To run api in background

sudo apt install npm

sudo npm install pm2@latest -g   #install pm2

pm2 start "uvicorn main:app" --name=process1

pm2 delete 0 1 2 

pm2 log 0

pm2 startup

pm2 save

sudo env PATH=$PATH:/usr/bin /usr/local/lib/node_modules/pm2/bin/pm2 startup systemd -u ubuntu --hp /home/ubuntu #sample

pm2 save

pm2 list

