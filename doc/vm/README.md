# VM and Docker Setup

# 1. To access your instance:

- Open an SSH client. (find out how to connect using PuTTY)
- Locate your private key file (video360.pem). The wizard automatically detects the key you used to launch the instance.

# 2. Your key must not be publicly viewable:
```
$ chmod 400 video360.pem
```

# 3. Connect to your instance using its Public DNS:
```
$ ssh -i "video360.pem" ubuntu@ec2-184-72-106-84.compute-1.amazonaws.com
```
OR
```
$ ssh -i "video360.pem" ubuntu@184.72.106.84
```
