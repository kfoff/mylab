## How to use


Create new directory and go to it.
```bash
mkdir foo && cd foo
```



Init ```config.json``` with argument.
- "foo" it is owner, **https://github.com/foo**
- "bar" it is repository, **https://github.com/foo/bar**

```bash
mylab init foo bar
```



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
