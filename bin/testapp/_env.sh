ctlid=2409141847
dockertag=jgwill/orpheus:testapp

containername=orpheustestapp
dkhostname=$containername

# PORT
#dkport=4000:4000

#xmount=/tmp:/a/tmp
#xmount2=/var:/a/var


dkcommand=bash #command to execute (default is the one in the dockerfile)

ODISPLAY=1

#dkextra=" -v \$dworoot/x:/x -p 2288:2288 "
dkextra=" -v $(realpath $(pwd)/../..):/app "

# Set DISPLAY environment variable
# dkextra="$dkextra -e DISPLAY=172.17.0.1:0"
dkextra="$dkextra -e DISPLAY=:99"
# dkextra="$dkextra -e DISPLAY=gaia.jgwill.com:0"
#-v /tmp/.X11-unix:/tmp/.X11-unix 
dkextra="$dkextra -v /tmp/.X11-unix:/tmp/.X11-unix "

QT_DEBUG_PLUGINS=1
dkextra="$dkextra -e QT_DEBUG_PLUGINS=1"

#dkmounthome=true


##########################
############# RUN MODE
#dkrunmode="bg" #default fg
#dkrestart="--restart" #default
#dkrestarttype="unless-stopped" #default


#########################################
################## VOLUMES
#dkvolume="myvolname220413:/app" #create or use existing one
#dkvolume="$containername:/app" #create with containername name



#dkecho=true #just echo the docker run


# Use TZ
#DK_TZ=1



#####################################
#Build related
#
##chg back to that user
#dkchguser=vscode

######################## HOOKS BASH
### IF THEY EXIST, THEY are Executed, you can change their names

dkbuildprebuildscript=dkbuildprebuildscript.sh
dkbuildbuildsuccessscript=dkbuildbuildsuccessscript.sh
dkbuildfailedscript=dkbuildfailedscript.sh
dkbuildpostbuildscript=dkbuildpostbuildscript.sh

###########################################
# Unset deprecated
unset DOCKER_BUILDKIT

