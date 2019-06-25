```bash
$ apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)

$ echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
$ apt-get update
$ apt-get install -y mongodb-org
# This command will install several packages containing latest stable version of MongoDB along with helpful management tools for the MongoDB server.

$ systemctl start mongod
$ systemctl status mongod
$ systemctl enable mongod
# The last step is to enable automatically starting MongoDB when the system starts.
```

