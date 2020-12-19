# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

import re



class TreeCounter:
    rows =

    def count_passports(self,file_name):
        file = open(file_name)
        all_lines = file.readlines()
        passLines = []
        line_count = 0
        pass_line_count = 0
        num_lines = len(all_lines)
        for line in all_lines:
            pass_line_count += 1
            line_count += 1
            if line == "\n" or line_count == num_lines:
                if line_count == num_lines:
                    passLines.append(line)
                self.valid_passports += 1 if self.correct_passport(passLines,line_count-pass_line_count) else 0
                pass_line_count = 0
                passLines.clear()
            else:
                passLines.append(line)

        print(self.valid_passports)

    def seat_id(self,row,column):
        return row*8+column




    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = TreeCounter()
    nm.count_passports("Inputs/Inputd4.txt")


