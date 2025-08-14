# Docker Command Reference Guide  

## Image Management  
### Build Images  
docker build [OPTIONS] PATH  
-t name:tag → Tag the image  
--no-cache → Ignore cache  
-f Dockerfile → Specify alternate Dockerfile  

### Search Images  
docker search [OPTIONS] TERM  
--filter  
--limit [number]  

### List Images  
docker image ls [OPTIONS]  
--format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}\t{{.Size}}"  
--filter  

### Remove Images  
docker rmi IMAGE [IMAGE...]  
-f → forced removal  

## Container Operations  
### Run Containers  
docker run [OPTIONS] IMAGE [COMMAND]  
-d → Detached mode  
-p 80:80 → Port mapping  
-v /host:/container → Volume mount  
-e VAR=value → Set env vars  

### Container Management  
docker start|stop|restart|kill CONTAINER  

### List Containers  
docker ps [OPTIONS]  
--filter "status=exited"  
--filter "ancestor=[name]"  

## Registry Operations  
### Authentication  
docker login [SERVER]  

### Push/Pull Images  
docker pull IMAGE[:TAG]  
docker push IMAGE[:TAG]  

### Tagging  
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]  

## Inspection & Logs  
### Inspect Objects  
docker inspect [OPTIONS] NAME|ID  
Format Examples:  
--format='{{.NetworkSettings.IPAddress}}'  
--format='{{json .Config}}'  

### View Logs
docker logs [OPTIONS] CONTAINER  
--tail 100 → Last N lines  
-f → Follow logs  
--since [time]

## Cleanup Commands  
### Prune Resources  
docker image|container|volume|network prune [OPTIONS]  
-a → Remove all unused  
-f → Force removal  
--filter  

### Full System Cleanup  
docker system prune -a --volumes  

## Exit Codes  
Code | Description  
0 | Normal termination  
1 | Application error  
125 | Docker run error  
137 | SIGKILL (forced stop)  
143 | SIGTERM (graceful shutdown)  

## Formatting Reference  
JSON Output  
--format '{{json .}}'  

## Table Output  
--format "table {{.ID}}\t{{.Names}}\t{{.Status}}"  

## Filter Types  
reference=name*  
status=running|exited  
before|since=timestamp  
until=[time]  
label=key=value  
