# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

class TreeCounter:
    pattern_len = 0
    trees = 0
    right = 3
    down = 1
    tree = '#'
    ground = '.'

    def count_trees(self,file_name):
        self.process_file(file_name)
        print(self.trees)

    def process_file(self,file_name):
        file = open(file_name)
        all_lines = file.readlines()
        self.pattern_len = len(all_lines[0])
        pattern_pos=0
        hill_len = len(all_lines)
        for height in range(0,hill_len):
            pattern_pos += 3
            if pattern_pos >= self.pattern_len-1:
                pattern_pos %= (self.pattern_len-1)
            if height != hill_len-1:
                object = (all_lines[height+1])[int(pattern_pos):int(pattern_pos+1)]
                self.trees = self.trees+1 if object == self.tree else self.trees
            print(line)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = TreeCounter()
    nm.count_trees("Inputs/Inputd3")


