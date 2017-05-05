import asyncio
import uvloop
import aiodns
import random
import sys

from fast_dns_scanner.scanner_base import ScannerBase


class AiodnsScanner(ScannerBase):
    def __init__(self, *args, **kwargs):
        ScannerBase.__init__(self, *args, **kwargs)

        self.loop = uvloop.new_event_loop()
        self.n = 0
        self.dns_handlers = []

    @asyncio.coroutine
    def _run(self, domain):
        self.n = len(self.hostnames)

        done = self.loop.create_future()

        for hostname in self.hostnames:
            asyncio.ensure_future(self._do_request(hostname, domain, 'A', done), loop=self.loop)

        yield from done

    @asyncio.coroutine
    def _do_request(self, hostname, domain, qtype, done):
        resolver = random.choice(self.dns_handlers)
        fqdn = '{}.{}'.format(hostname, domain).strip('.')

        try:
            res = yield from resolver.query(fqdn, qtype)
            print("\n", fqdn, res[0].host)
        except aiodns.error.DNSError as ex:
            if ex.args[0] != 4: #if error is not Domain name not found
                self.n += 1
                asyncio.ensure_future(self._do_request(hostname, domain, qtype, done), loop=self.loop)
        except UnicodeError:
            print("Failed", fqdn)
        except Exception as ex:
            print("Unhandled exception", ex)

        self.n -= 1

        if self.n <= 0:
            if not done.done():
                done.set_result(True)
        else:
            sys.stderr.write("\rpending req: {}".format(self.n))

    def run(self):
        for nameserver in self.resolvers:
            self.dns_handlers.append(
                aiodns.DNSResolver(nameservers=[nameserver], loop=self.loop, timeout=self.timeout, tries=1)
            )

        if not self.dns_handlers:
            self.dns_handlers.append(aiodns.DNSResolver(loop=self.loop))

        for domain in self.domains:
            self.loop.run_until_complete(self._run(domain))