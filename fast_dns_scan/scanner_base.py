from abc import ABCMeta, abstractmethod

class ScannerBase(metaclass=ABCMeta):

    def __init__(self, resolvers, hostnames, domains, timeout):
        self.resolvers = resolvers
        self.hostnames = hostnames
        self.domains = domains
        self.timeout = timeout

    @abstractmethod
    def run(self):
        pass