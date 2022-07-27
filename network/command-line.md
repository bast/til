# Network configuration using command line

```
nmcli dev status
nmcli con show
nmcli con show -a
sudo nmcli con delete SOMENAME

nmcli radio wifi
nmcli radio wifi on
nmcli radio wifi off

nmcli dev wifi list
sudo nmcli       dev wifi connect NETWORK-SSID password "my secret"
sudo nmcli --ask dev wifi connect NETWORK-SSID

nmtui
```
