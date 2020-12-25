# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

import re



import re
class YesCounter:

    def count_question_yeses(self,file_name):
        file = open(file_name)
        all_lines = file.readlines()
        num_groups_questions_least_1_yes = 0
        group_lines = []

        for i in range(0,len(all_lines)):
            line = all_lines[i]
            if line != '\n':
                group_lines.append(line)
            if line == '\n' or i == len(all_lines)-1:
                num_groups_questions_least_1_yes += self.num_questions_1_yes_least(group_lines)
                group_lines = []

        print(num_groups_questions_least_1_yes)


    def num_questions_1_yes_least(self,group_arr):
        yes_questions_set = set()
        print("group array:", group_arr)
        for line in group_arr:
            line = line.replace("\n","")
            print("Line:", line)
            for character in line:
                if re.match("[a-zA-Z]",character):
                    yes_questions_set.add(character)
        print("set:",yes_questions_set)
        return len(yes_questions_set)



    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tc = YesCounter()
    tc.count_question_yeses("Inputs/Inputd6.txt")


