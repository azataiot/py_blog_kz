# how to deploy on the server ?

Run Blog with port 80:	

```	python 	
(venv)xpleaf@leaf:~/project/Blog_mini$ gunicorn -b 0.0.0.0:80  manage:app
[2016-03-08 11:50:43 +0000] [7202] [INFO] Starting gunicorn 19.4.5
[2016-03-08 11:50:43 +0000] [7202] [INFO] Listening at: http://0.0.0.0:80 (7202)
[2016-03-08 11:50:43 +0000] [7202] [INFO] Using worker: sync
[2016-03-08 11:50:43 +0000] [7207] [INFO] Booting worker with pid: 7207			
```	