# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

import re


class TreeCounter:
    pattern_len = 0
    tree = '#'
    ground = '.'

    def count_trees(self,file_name):
        trees1 = self.process_file(file_name, 1, 1)
        trees2 = self.process_file(file_name,3,1)
        trees3 = self.process_file(file_name,5,1)
        trees4 = self.process_file(file_name, 7, 1)
        trees5 = self.process_file(file_name, 1, 2)
        print(trees1*trees2*trees3*trees4*trees5)
     #trees5 = self.process_file(file_name, 1, 2)
    #  print(trees5)

    def process_file(self,file_name,right ,down):
        trees = 0
        file = open(file_name)
        all_lines = file.readlines()
        for i in range(0,len(all_lines)-1):
            all_lines[i] =  re.sub("[^#.]", "",  all_lines[i])

        pattern_len = len(all_lines[0])
        pattern_pos=0
        hill_len = len(all_lines)
        height=0
        while height < hill_len-1:
            pattern_pos += right
            height += down
            if pattern_pos >= pattern_len:
                pattern_pos %= pattern_len
            pattern = (all_lines[height])
            hit = pattern[int(pattern_pos):int(pattern_pos+1)]
            trees = trees+1 if hit == self.tree else trees
            print("Down:" , down, " height ", height)
        return trees

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = TreeCounter()
    nm.count_trees("Inputs/Inputd3TEST")


