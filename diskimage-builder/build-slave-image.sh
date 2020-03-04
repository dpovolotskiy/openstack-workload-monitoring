#!/bin/bash

RequiredPackages="qemu-utils
kpartx"

for package in $RequiredPackages; do
        dpkg-query -l $package >/dev/null 2>&1
        if [[ $? -eq 1 ]]; then
                echo -e "Required to install the following packages:\n$RequiredPackages"
                exit 1
        fi
done

export ARCH="amd64"
export BASE_ELEMENTS="bootloader cloud-init-datasources ubuntu ubuntu-18-slave"
export DIB_CLOUD_INIT_DATASOURCES="ConfigDrive, Ec2"
export DIB_RELEASE="bionic"
export ELEMENTS_PATH="./elements/"
export IMAGE_PATH="./images/ubuntu-18.04-slave"

disk-image-create vm $BASE_ELEMENTS -t qcow2 -o $IMAGE_PATH
