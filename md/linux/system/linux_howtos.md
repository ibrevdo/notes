Linux Howtos
================

## Searching
* search "word" in hidden directories   

```sh
grep -R "word" `ls -ap | grep "^\..*/$"` 
```

* find file by (partial) name   `find . -iname "stdio*" `

* count a number of files in directories recursively (wihtout folders)
`find . -type f | wc -l`

* update permissions to all folders recursively
find . -type d -exec chmod 755 {} \;

* update permissions to all files recursively
find /opt/lampp/htdocs -type f -exec chmod 644 {} \;

## Logging 

* dmesg                                 prints kernel messages . i.e /var/log/kern.log            
* print 10 last lines of kernel log     `dmesg | tail 10`
* follow log file in real time          `tail -f /var/log/syslog`


## Networking

* display bandwidth usage               `iftop -P`
