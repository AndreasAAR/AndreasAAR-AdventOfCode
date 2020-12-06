# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

class Num_Finder:
    file_name = "input.txt"
    firstnum = ""
    secondNum = ""

    def find_nums(self):
        self.set_2020_sum_nums()

        print((int(self.firstnum)*int(self.secondNum)))

    def set_2020_sum_nums(self):
        outer_index = 0
        file = open(self.file_name)
        all_lines = file.readlines()
        for num in all_lines:
            outer_index += 1
            for num2 in all_lines[outer_index:]:
                if self.is_2020_sum(num,num2):
                    self.firstnum = num
                    self.secondNum = num2

    def is_2020_sum(self,num1,num2):
        num1 = self.clean(num1)
        num2 = self.clean(num2)
        return int(num1)+int(num2) == 2020

    def clean(self,num):
       return re.sub('[^0-9]','',num)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = Num_Finder()
    nm.find_nums()


