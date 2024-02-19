# Показати записи A та AAAA
nslookup koliasa.com

# Показати всі записи DNS
nslookup -type=all koliasa.com

# Показати детальну інформацію про записи DNS
nslookup -d koliasa.com

# Показати записи MX
nslookup -q=mx koliasa.com

# Використовувати Google Public DNS
nslookup -server 8.8.8.8 koliasa.com

# Показати список серверів DNS
nslookup -l koliasa.com

# Показати запис SOA
nslookup -type=soa koliasa.com

# Показати записи NS
nslookup -type=ns koliasa.com

# Показати записи TXT
nslookup -type=txt koliasa.com

# Показати записи SRV для SIP
nslookup -type=srv _sip._udp.kolia.com