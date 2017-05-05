# Fast DNS Scanner
Async DNS bruteforce wordlist scanner.

## Installing

* Requires Python >= 3.3
* Requires Pip
* Tested on Python 3.5.3

For installing python requirements run:

```
pip install -r requirements.txt
```


## Using the tool

### Help

```bash
$ ./fast_dns_scan -h
usage: fast_dns_scan [-h] [-r RESOLVERS] [-w WORDLIST] [--timeout TIMEOUT]
                     domains [domains ...]

positional arguments:
  domains               one or more domains

optional arguments:
  -h, --help            show this help message and exit
  -r RESOLVERS, --resolvers RESOLVERS
                        file with DNS servers (one on each line)
  -w WORDLIST, --wordlist WORDLIST
                        wordlist file with host to search on domains
  --timeout TIMEOUT     Timeout for queries in seconds (float).
```

### Samples

Run scan on example.com

```
$ ./fast_dns_scan -w wordlists/big.txt -r wordlist/resolvers.txt example.com
```

Run scan on multiple domains

```
$ ./fast_dns_scan -w wordlists/big.txt -r wordlist/resolvers.txt example.com example.net
```

