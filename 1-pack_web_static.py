#!/usr/bin/python3
"""
Fabric script that generates a .tgz
"""
from fabric.api import *
import time


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = time.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(dt))
        return ("versions/web_static_{}.tgz".format(dt))
    except:
        return None
