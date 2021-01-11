# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

import re



import re

class BagCounter:
    bags = {}  # id, bag-object
    containing_silver = {}  # So we dont dig into already checked paths

    class Bag:
        id = ''
        inner_bag_num = ''
        parent_bags = {}
        children_bags = {}  # Id,

        def relationship(self, bag, number):
            children_bag_nums.put(bag.id, number)

        def add_child(self, num, bag):
            all_progeny.add(bag)
            if num != 0:
                children_bag_nums.put()

        def Bag(self, verb, color, children):
            self.id = verb + ":" + color

        def set_ancestors(self):  # recursive function
            return ""

        def set_progeny(self):  # recursive get progeny
            return ""

    def count_question_yeses(self,file_name):
        file = open(file_name)
        all_lines = file.readlines()
        for i in range(0,len(all_lines)):
           self.manage_bag(all_lines[i])

    def manage_bag(self, line):


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tc = BagCounter()
    tc.count_question_yeses("Inputs/Inputd7Test.txt")


