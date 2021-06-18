from os import getenv
import srv_hijacker


def requests_use_srv_records():
    srv_hijacker.hijack(
        host_regex=r".consul$",
        srv_dns_host=getenv("NET_BRIDGE_GW_IP"),
        libraries_to_patch=[
            "psycopg2"
        ],  # remove psycopg2 dependency if app is not using databse
    )
