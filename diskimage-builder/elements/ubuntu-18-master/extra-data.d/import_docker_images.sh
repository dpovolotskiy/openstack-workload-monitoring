#!/bin/bash

docker load -i /prom_prometheus.tar
rm -f /prom_prometheus.tar
docker load -i /prom_alertmanager.tar
rm -f /prom_alertmanager.tar
docker load -i /alerta_alerta-web.tar
rm -f /alerta_alerta-web.tar
docker load -i /library_mongo.tar
rm -f /library_mongo.tar

rm -f /import_docker_images.sh
