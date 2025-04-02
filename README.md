使用python版本3.11.2，python库依赖在requirements.txt中
client是前端目录，server是后端目录，common是双端共用

双端通信需要使用docker启动WAMP中继器，暴露端口8093
sudo docker run -it -p 8093:8080 crossbario/crossbar