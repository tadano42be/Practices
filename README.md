Docker Commands List
===================================================================================

docker build [OPTIONS] PATH | URL | -

docker build
  -f [dockerfile]
  --force-rm=true
  --rm=true
  --no-cache
  --help
  -t SOURCE_IMAGE[:TAG]

docker search 
  --filter is-official=true 
            stars=100
            is-official=true
  --limit [number]
  --no-trunc
  --format "{{.Name}}: {{.Description}}"
            "table {{.Name}}\t{{.IsAutomated}}\t{{.IsOfficial}}\t{{.Description}}\t{{.StarCount}}"
  --help

docker image pull
  --help

docker image ls [OPTIONS] [REPOSITORY[:TAG]]
  --all
  --no-trunc
  --quiet
  --digests
  --filter reference='name*'
            before='image_name'
            since='image_name'
            dangling=true
            label='label'
  --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}\t{{.CreatedAt}}\t{{.Digest}}"
  --help

docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
          SOURCE_IMAGE_ID TARGET_IMAGE[:TAG]
          # :latest will be used as default when no tag was specified

docker login

docker push [OPTIONS] [REGISTRY_HOST/][USERNAME/]REPOSITORY[:TAG]
docker pull [OPTIONS] [REGISTRY_HOST/][USERNAME/]REPOSITORY[:TAG]

docker image inspect IMAGE_ID
  --format='{{json .Config.Labels}}'

docker inspect [OPTIONS] NAME|ID [NAME|ID...]
  --format='{{.Config.Image}}' [NAME|ID]
            '{{.Id}}' [NAME|ID]
            '{{.LogPath}}' [NAME|ID]
            '{{json .Config}}' [NAME|ID]

docker rmi [OPTIONS] IMAGE [IMAGE...]
  -f IMAGE_ID

docker start [OPTIONS] CONTAINER [CONTAINER...]
docker run [OPTIONS] IMAGE[:TAG] [COMMAND] [ARG...]
  -it -d -p 5000:5000 -v ${PWD}:/app/code

docker stop [OPTIONS] CONTAINER [CONTAINER...]
docker kill [OPTIONS] CONTAINER [CONTAINER...]

docker ps [OPTIONS]
  -a
  -n 1
  -q
  -s
  -l
  --no-trunc
  --filter label=""
            'exited=0'
            ancestor=''
  --format json
            "table {{.ID}}\t{{.Names}}"
    
>> COMMON DOCKER CONTAINER EXIT CODES <<
Exit Code 0	    Purposely stopped
Exit Code 1	    Application error
Exit Code 125	Container failed to run error
Exit Code 126	Command invoke error
Exit Code 127	File or directory not found
Exit Code 128	Invalid argument used on exit
Exit Code 134	Abnormal termination (SIGABRT)
Exit Code 137	Immediate termination (SIGKILL)
Exit Code 139	Segmentation fault (SIGSEGV)
Exit Code 143	Graceful termination (SIGTERM)
Exit Code 255	Exit Status Out Of Range

docker logs [OPTIONS] CONTAINER[NAME|ID]
  --tail [number]
  -f
  --details
  --since [timestamp]
  --until [timestamp]
  # use number (e.g. 60) for relative format
  -t (or --timestamps)

docker volume create
  ls
  inspect
  rm

docker image prune
docker container prune
docker volume prune
  -a (--all)
  -f (--force)
  --filter

>> Key Filters <<
until
label
status

docker system prune -a -f --volumes 
# all unused resources
