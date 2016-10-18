#!/bin/bash

# TODO: update all packages? Would that require a restart (kernel updates etc.)?

# Post install script. Executed as root, do not use sudo (will fail).
yum -y install netcdf-fortran-devel


# On centos ami-d5f52eb6, you can't' serve directories with sshfs. Fix by softlinking
FILE=/usr/libexec/sftp-server
if [ ! -f $FILE ]; then
    ln -s /usr/libexec/openssh/sftp-server $FILE
fi

# get the cfn_node_type
. /opt/cfncluster/cfnconfig
if [ "$cfn_node_type" == "MasterServer" ]; then
    # TODO don't hardcode these variables
    MYUSER=centos
    USERHOME=/home/$MYUSER

    function myget {
        # execute commands as non-root to get the right permissions
        su $MYUSER -c "wget $1"
        BNAME=$(basename $1)
        SUFFIX="${BNAME##*.}"
        case $SUFFIX in
        gz)
            expr $BNAME : '.*\(tar.gz$\)'
            case $? in
            0)
                su $MYUSER -c "tar -xf $BNAME"
                ;;
            *)
                echo "unknown extension in \""$BNAME"\""
                ;;
            esac
        esac
    }

    # TODO: do this in parallel
    cd $USERHOME
    myget https://github.com/poidl/awsroms/archive/master.tar.gz
    myget https://s3-ap-southeast-1.amazonaws.com/romsaws/roms.tar.gz

fi



