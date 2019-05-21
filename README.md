## Quick use
```bash
sudo mylab help
sudo mkdir bar && cd bar
sudo mylab init foo bar
sudo mylab all
sudo mylab start
```


## Step by step use

Create new directory and go to it.
```bash
sudo mkdir bar && cd bar
```



Init ```config.json``` with arguments.


```bash
sudo mylab init foo bar
```
> "foo" it is owner **https://github.com/foo**,
> "bar" it is repository **https://github.com/foo/bar**,


Clone project from github **https://github.com/foo/bar**:
```bash
sudo mylab clone
```



Create environment and install pip modules.
```bash
sudo mylab install
```



Create databases and migrate data.
```bash
sudo mylab migrate
```



Load data from ```xml``` to database.
```bash
sudo mylab load
```


Copy media.
```bash
sudo mylab media
```


Change password for superuser.
```bash
sudo mylab perm
```


Start project.
```bash
sudo mylab start
```
or
```bash
sudo mylab start 8002
```
or
```bash
sudo mylab manage runserver_plus 0.0.0.0:8002 --settings dj.settings_nsk
```
> port from ```8000``` to ```8500```

Running on: **http://mylab.babah24.ru:8002**
