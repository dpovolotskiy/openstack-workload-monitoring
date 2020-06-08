import socket
import time
import yaml

from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY


def connection_check(address, port):
    try:
        host = socket.gethostbyaddr(address)
        con = socket.create_connection((host[0], port), 0.1)
        con.close()
        return True
    except:
        pass
    return False


class CustomCollector(object):
    def __init__(self):
        with open('config.yaml') as conf:
            self.config = yaml.safe_load(conf)
            self.hostname = str(socket.gethostname())

    def collect(self):
        g = GaugeMetricFamily("internet_access", "Access to the internet from the current node", labels=['instance',
                                                                                                         'unavailable'
                                                                                                         'Addresses'])
        access = 1
        unavailable_addresses = []
        for host in self.config['config']['hosts']:
            address, port = host.split(":")
            if not connection_check(address, port):
                access = 0
                unavailable_addresses.append(host)
        if access:
            g.add_metric([self.hostname], access)
        else:
            g.add_metric([self.hostname, ", ".join(unavailable_addresses)], access)
        yield g


if __name__ == '__main__':
    start_http_server(9721)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(10)
