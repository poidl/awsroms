#!/bin/bash

sudo yum -y install netcdf-fortran-devel
wget https://s3-ap-southeast-1.amazonaws.com/romsaws/roms.tar.gz
tar -xf roms.tar.gz
wget https://github.com/poidl/awsroms/archive/master.tar.gz
tar -xf master.tar.gz

#TODO install netcdf on nodes

# On centos ami-d5f52eb6, you can't' serve directories with sshfs. Fix by softlinking
sudo ln -s /usr/libexec/openssh/sftp-server /usr/libexec/sftp-server
