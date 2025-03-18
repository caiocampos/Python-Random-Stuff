from time import localtime, strftime


"""
Adicionar DNSs e hosts ao arquivo de configuração
"""

RESOLV_CONF_LOCATION = "/etc/resolv.conf"
HOSTS_LOCATION = "/etc/hosts"

NEW_DNS = """
nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 1.1.1.1
nameserver 1.0.0.1
"""

NEW_HOSTS = """
"""


def log(text):
    print(strftime("%H:%M:%S > ", localtime()) + text)


def change_dns():
    with open(RESOLV_CONF_LOCATION, "r", encoding="utf-8") as file:
        resolv = file.read()

    new_dns_pos = resolv.find(NEW_DNS.strip())

    if new_dns_pos > 0:
        log("The resolv file don't need changes")
    else:
        log("Changing resolv file")

        nameserver_pos = resolv.find("nameserver")

        resolv = resolv[:nameserver_pos] + NEW_DNS + resolv[nameserver_pos:]

        with open(RESOLV_CONF_LOCATION, "w", encoding="utf-8") as file:
            file.write(resolv)


def change_hosts():
    with open(HOSTS_LOCATION, "r", encoding="utf-8") as file:
        hosts = file.read()

    hosts_pos = hosts.find(NEW_HOSTS.strip())

    if hosts_pos > 0:
        log("The hosts file don't need changes")
    else:
        log("Changing hosts file")
        hosts = hosts + NEW_HOSTS
        with open(HOSTS_LOCATION, "w", encoding="utf-8") as file:
            file.write(hosts)


def process():
    if NEW_DNS.strip():
        change_dns()

    if NEW_HOSTS.strip():
        change_hosts()
