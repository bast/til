

# How to run scripts in parallel


## xargs

```
$ find -name "*.png" | xargs -n 1 ./script.sh
$ find -name "*.png" | xargs -n 1 -P 4 ./script.sh
```


## [GNU parallel](https://www.gnu.org/software/parallel/)

```
$ find -name "*.jpg" | parallel convert -geometry 120 {} {.}_thumb.jpg
```


## Makefile

Needs documenting ...


## Shell script with & and wait

Needs documenting ...
