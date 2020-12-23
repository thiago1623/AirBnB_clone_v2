#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['34.75.156.173', '35.243.219.163']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = time.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(dt))
        return ("versions/web_static_{}.tgz".format(dt))
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        file = archive_path.split('/')[-1]
        new_folder = ("/data/web_static/releases/" + file.split(".")[0])
        # Upload the archive to the /tmp/
        put(archive_path, "/tmp/")
        # Uncompress the archive to the folder /data/web_static/releases/
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".format(file, new_folder))
        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(file))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        # Delete the symbolic link
        run('sudo rm -rf /data/web_static/current')
        # Create a new the symbolic link
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    try:
        archive_address = do_pack()
        val = do_deploy(archive_address)
        return val
    except:
        return False
