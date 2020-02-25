#!/bin/bash

export ARCH="amd64"
export BASE_ELEMENTS="bootloader cloud-init-datasources ubuntu ubuntu-18-slave"
export DIB_CLOUD_INIT_DATASOURCES="ConfigDrive, Ec2"
export DIB_RELEASE="bionic"
export ELEMENTS_PATH="./elements/"
export IMAGE_PATH="./images/ubuntu-18.04-slave"
export DIB_MIN_TMPFS=10

disk-image-create vm $BASE_ELEMENTS -t qcow2 -o $IMAGE_PATH
