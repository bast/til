# Ubuntu container for development

```yaml
Bootstrap: docker
From: ubuntu:21.04

%post
    export DEBIAN_FRONTEND=noninteractive
    apt-get -qq update
    apt-get -qq -y install git
    apt-get -qq -y install gfortran-8
    apt-get -qq -y install gcc-8
    apt-get -qq -y install g++-8
    apt-get -qq -y install libomp-dev
    apt-get -qq -y install mpich libmpich-dev libhdf5-mpich-dev
    apt-get -qq -y install python python3-pip
    apt-get -qq -y install python-is-python3
    apt-get -qq -y install libhdf5-dev
    pip install scipy
    pip install h5py
    pip install cmake

%environment
    export LC_ALL=C
```
