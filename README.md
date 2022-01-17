# MAPF bindings for the CGSHOP21 competition

This repository uses the excellent [libMultiRobotPlanning](https://github.com/whoenig/libMultiRobotPlanning) that implements various solvers for the Multi-Agent Path Finding problem.





## Installation

1. `git clone git@github.com:librallu/cgshop21_to_mapf.git`
2. install prerequisites (python3) and libMultiRobotPlanning prerequisites (cmake, boost, lib-yaml, doxygen):
    - linux (debian) commands: `sudo apt-get install python3 cmake libyaml-cpp-dev doxygen libboost-all-dev`
3. compile libMultiRobotPlanning:
    ```
    cd libMultiRobotPlanning/
    mkdir build
    cd build
    cmake ..
    make
    cd ../../
    ```




## Workflow

### 1. MAPF instances from CGSHOP21 instances

```
for f in cgshop_instances/images/*.json; do; ./cgshop_to_mapf.py "${f}" > "${f}.yml"; done;
for f in cgshop_instances/uniform/*.json; do; ./cgshop_to_mapf.py "${f}" > "${f}.yml"; done;
```


### 2. Solve the MAPF instance

```
./libMultiRobotPlanning/build/mapf_prioritized_sipp -i mapf_instances/clouds_00004_50x50_75_1745.instance.json.yml  -o mapf_outputs/small_free_000_10x10_30_30.instance.json.yml
```



## Useful links

 - [challenge website](https://cgshop.ibr.cs.tu-bs.de/competition/cg-shop-2021/#problem-description)