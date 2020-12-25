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
                num_groups_questions_least_1_yes += self.num_questions_all_yes(group_lines)
                group_lines = []

        print(num_groups_questions_least_1_yes)


    def num_questions_all_yes(self,group_arr):
        num_people = len(group_arr)
        yes_question_answers = {}
        print("group array:", group_arr)
        num_all_yes_questions = 0
        for line in group_arr:
            line = line.replace("\n","")
            print("Line:", line)
            for character in line:
                print("character:", character)
                if re.match("[a-zA-Z]",character):
                    if character in yes_question_answers.keys():
                        yes_question_answers[character] +=1
                    else:
                        yes_question_answers[character] = 1
        print("set:",yes_question_answers)
        for num in yes_question_answers.values():
             if num == num_people:
                 num_all_yes_questions+=1

        return num_all_yes_questions



    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tc = YesCounter()
    tc.count_question_yeses("Inputs/Inputd6.txt")


