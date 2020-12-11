# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

class Num_Finder:
    file_name = "Inputs/Inputd1.txt"
    nums = set()

    def find_nums(self):
        self.set_2020_sum_nums()
        self.calc_num_sums()

    def calc_num_sums(self):
        sum = 1
        for n in self.nums:
            sum = int(sum)*int( n)
        print(sum)

    def set_2020_sum_nums(self):
        outer_index = 0
        file = open(self.file_name)
        all_lines = file.readlines()
        for num1 in all_lines:
            for num2 in all_lines:
                for num3 in all_lines:
                    num1 = self.clean(num1)
                    num2 = self.clean(num2)
                    num3 = self.clean(num3)
                    in_param_set = set()
                    in_param_set.add(num1)
                    in_param_set.add(num2)
                    in_param_set.add(num3)
                    if len(in_param_set) == 3:
                        if self.is_2020_sum(num1,num2,num3):
                            self.nums.add(num1);
                            self.nums.add(num2);
                            self.nums.add(num3);

    def is_2020_sum(self,num1,num2,num3):
        return int(num1)+int(num2)+int(num3)  == 2020

    def clean(self,num):
       return re.sub('[^0-9]','',num)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = Num_Finder()
    nm.find_nums()


