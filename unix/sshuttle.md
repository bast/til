# sshuttle: convenient ssh tunnel for specific webpages only

More info: https://github.com/sshuttle/sshuttle

Here you have access to `myserver.org`, the network
that `myserver.org` is on has access to `example.com`,
and you want to access `example.com` by hopping through
`myserver.org`:
```
$ sshuttle --remote=myserver.org example.com
```
