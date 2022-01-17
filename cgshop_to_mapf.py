#!/usr/bin/python3
import json
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("USAGE: {} CGSHOP_INSTANCE".format(argv[0]))
    else:
        input_filename = argv[1]
        offset = 100
        # 1. read instance
        with open(input_filename, 'r') as f:
            data = json.load(f)
            starts = data["starts"]
            targets = data["targets"]
            obstacles = data["obstacles"]
            map_size = data["meta"]["description"]["parameters"]["shape"]
            print("agents:")
            for (i,start) in enumerate(starts):
                print("-   goal: {}".format([offset+targets[i][0], offset+targets[i][1]]))
                print("    name: agent_{}".format(i))
                print("    start: {}".format([offset+start[0], offset+start[1]]))
            # 2. print output
            print("map:")
            print("    dimensions: [{},{}]".format(map_size[0]+offset*2, map_size[1]+offset*2))
            print("    obstacles:")
            for obstacle in obstacles:
                print("    - [{}, {}]".format(offset+obstacle[0], offset+obstacle[1]))
