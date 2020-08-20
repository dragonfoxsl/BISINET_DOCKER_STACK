In some Images you will need to install software to do this make a Dockerfile and
use that file to create docker-compose.yml file as bellow

build: 
    context: .
    dockerfile: Dockerfile-cops

build: 
    context: .
    dockerfile: Dockerfile-ubooquity

IMPORTANT - These kinds of images had to be manually built again for updates as watchtower cannot update such images

For HEALTHCHECKS:
Use wget instead of curl as bellow example

test: curl --fail -s http://10.10.10.134:8051/ || exit 1
test: wget --quiet --tries=1 --spider http://10.10.10.134:8051/ || exit 1