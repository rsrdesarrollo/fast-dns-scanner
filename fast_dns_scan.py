import argparse
from fast_dns_scan.aiodns_scanner import AiodnsScanner

parser = argparse.ArgumentParser("Fast dns bruteforce subdomain scanner")
parser.add_argument('-r', '--resolvers', required=False)
parser.add_argument('-w', '--wordlist')
parser.add_argument('--timeout', type=float, default=1.0, help="Timeout for queries in seconds (float).")
parser.add_argument('domains', nargs='+')


ops = parser.parse_args()
if __name__ == '__main__':
    if ops.resolvers:

        resolvers = set()
        with open(ops.resolvers, 'r') as fh:
            resolvers = set((l.strip() for l in fh.readlines()))

        hostnames = set()
        with open(ops.wordlist, 'r') as fh:
            hostnames = set((l.strip() for l in fh.readlines()))

        scanner = AiodnsScanner(resolvers, hostnames, ops.domains, ops.timeout)

        scanner.run()

