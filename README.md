# MAPF bindings for the CGSHOP21 competition

This repository uses the excellent [libMultiRobotPlanning](https://github.com/whoenig/libMultiRobotPlanning) that implements various solvers for the Multi-Agent Path Finding problem.

## Installation

1. `git clone [TODO]`
2. install prerequisites (python3, cmake, boost):
    - linux (debian) commands: `sudo apt-get install python3 cmake`
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

### 1. Generate MAPF instances from the CGSHOP21 instances

### 2. Solve the MAPF instance