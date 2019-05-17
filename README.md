## How to use


Create new directory and go to it.
```bash
mkdir foo && cd foo
```



Init ```config.json``` with arguments.


```bash
mylab init foo bar
```
> "foo" it is owner **https://github.com/foo**,
> "bar" it is repository **https://github.com/foo/bar**,


Clone project from github **https://github.com/foo/bar**:
```bash
mylab clone
```



Create environment and install pip modules.
```bash
mylab install
```



Create databases and migrate data.
```bash
mylab migrate
```



Load data from ```xml``` to database.
```bash
mylab load
```

Copy media.
```bash
mylab media
```



Copy media.
```bash
mylab media
```


Change password for superuser.
```bash
mylab perm
```


Start project.
```bash
mylab start
```
or
```bash
mylab start 8002
```
> port from ```8000``` to ```8500```
