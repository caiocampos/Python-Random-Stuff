"""
Adicionar DNSs ao arquivo de configuração
"""

RESOLV_CONF_LOCATION = "/etc/resolv.conf"

NEW_DNS = """
nameserver 1.1.1.1
nameserver 1.0.0.1
nameserver 8.8.8.8
nameserver 8.8.4.4
"""

with open(RESOLV_CONF_LOCATION, "r", encoding="utf-8") as file:
    resolv = file.read()

nameserver_pos = resolv.find("nameserver")

resolv = resolv[:nameserver_pos] + NEW_DNS + resolv[nameserver_pos:]

with open(RESOLV_CONF_LOCATION, "w", encoding="utf-8") as file:
    file.write(resolv)
