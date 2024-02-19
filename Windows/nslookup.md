## Показати записи A та AAAA## 
```bash
nslookup koliasa.com
```
## Показати всі записи DNS
```bash
nslookup -type=all koliasa.com
```
## Показати детальну інформацію про записи DNS
```bash
nslookup -d koliasa.com
```
## Показати записи MX
```bash
nslookup -q=mx koliasa.com
```
## Використовувати Google Public DNS
```bash
nslookup -server 8.8.8.8 koliasa.com
```
## Показати список серверів DNS
```bash
nslookup -l koliasa.com
```
## Показати запис SOA
```bash
nslookup -type=soa koliasa.com
```
## Показати записи NS
```bash
nslookup -type=ns koliasa.com
```
## Показати записи TXT
```bash
nslookup -type=txt koliasa.com
```
## Показати записи SRV для SIP
```bash
nslookup -type=srv _sip._udp.kolia.com