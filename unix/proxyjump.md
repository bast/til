# Using ProxyJump when ssh-jumping via another host

In this example we cannot access `somehost` or `anotherhost`
directly but have to jump via two hosts (to reach `somehost`)
or jump via one host (to reach `anotherhost`):

```
Host somehost
    HostName some.host.example.com
    ProxyJump user1@jump.host1.example.com,user2@jump.host1.example.com

Host anotherhost
    HostName another.host.example.com
    User root
    ProxyJump user1@jump.host1.example.com
```
