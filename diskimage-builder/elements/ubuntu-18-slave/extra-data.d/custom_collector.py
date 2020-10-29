import socket
import time
import yaml
import os

from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY


def connection_check(address):
    exit_code = os.system("ping -c1 -w2 {} > /dev/null 2>&1".format(address))
    return not exit_code


class CustomCollector(object):
    def __init__(self):
        with open('/home/ubuntu/monitoring/customCollector/collector_config.yaml') as conf:
            self.config = yaml.safe_load(conf)
            self.hostname = str(socket.gethostname())

    def collect(self):
        g = GaugeMetricFamily("internet_access", "Access to the internet from the current node", labels=['instance',
                                                                                                         'unavailable'
                                                                                                         'Addresses'])
        access = 1
        unavailable_addresses = []
        for host in self.config['config']['hosts']:
            if not connection_check(host):
                access = 0
                unavailable_addresses.append(host)
        if access:
            g.add_metric([self.hostname], access)
        else:
            g.add_metric([self.hostname, ", ".join(unavailable_addresses)], access)
        yield g


if __name__ == '__main__':
    start_http_server(port=8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(10)
