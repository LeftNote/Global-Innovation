import os
import paramiko

transport = paramiko.Transport((os.environ['HOST_IP'], 2222))
transport.connect(username=os.environ['HOST_USER'], password=os.environ['HOST_PASSWORD'])
sftp = paramiko.SFTPClient.from_transport(transport)

dir_remote = ''
for dirpath, dirnames, filenames in os.walk('www'):
    remote_path = os.path.join(dir_remote, dirpath)
    # make remote directory ...
    for filename in filenames:

        local_path = os.path.join(dirpath, filename)
        remote_filepath = os.path.join(remote_path, filename)
        print(local_path, remote_path)
        sftp.put(local_path, remote_filepath)