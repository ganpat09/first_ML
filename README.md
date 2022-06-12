creating conda enviornment

'''

conda create -p  venv python==3.7 -y

conda activate venv/


'''
pip install -r requirements.txt 
'''

``` status check git 
git log 
``` 


To check remote url
```
git remote -v 

```

To check git branch

```
git branch
```

To setup CI/CD pipline in heroku we need 3 info

```
1. HEROKU ACOOUNT EMAIL
2. HEROKU API KEY = 42c52845-1b21-4069-9acd-90d8cc0156ae
3. HEROKU APP_NAME = firstml09


BUILD DOCKER IMAGE 

```
docker build -t <image_name>:<tag_name> .

```

Note : image_name will be in lowercase

docker images
```
docker images
```

run docker image
```
docker run -p 5000:5000 -e PORT=5000 img_name
```

to check running containers

```
docker ps
```

stop container
```
docker stop container_id
``
