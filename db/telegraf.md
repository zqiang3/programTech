## installation

```
brew update
brew install telegraf
telegraf -config /usr/local/etc/telegraf.conf
```

## Configuration

- macOS [Homebrew](http://brew.sh/): `/usr/local/etc/telegraf.conf`
- Linux debian and RPM packages: `/etc/telegraf/telegraf.conf`

## Start

**mac**

```
telegraf -config telegraf.conf
```

**linux**

```
sudo service telegraf start
```

