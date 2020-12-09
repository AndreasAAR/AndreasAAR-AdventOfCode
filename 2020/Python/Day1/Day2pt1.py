# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

class Valid_Pass_Counter:
    file_name =""
    valid_passwords = 0

    def find_passwords(self,file):
        self.file_name = file
        self.process_file()

    def process_file(self):
        file = open(self.file_name)
        all_lines = file.readlines()
        for line in all_lines:
            if self.is_correct(line):
                self.valid_passwords+=1
        print(self.valid_passwords)

    def is_correct(self, line):
        limits = re.sub('[^0-9\-]','',line)
        repetition_params = limits.split('-')
        min = repetition_params[0]
        max = repetition_params[1]
        letter = (line.split(' ')[1]).replace(':','')
        password = line.split(' ')[2]
        print('min:' , min , " max: " , max, " letter: ", letter)
        return self.is_correct_helper(password,min,max, letter)

    def is_correct_helper(self, password,min,max, letter):
        num_min = self.clean(min)
        num_max = self.clean(max)
        letter_count = password.count(letter)

        return letter_count >= int(num_min) and letter_count <= int(num_max)


    def clean(self,num):
       return re.sub('[^0-9]','',num)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = Valid_Pass_Counter()
    nm.find_passwords("Inputs/Inputd2.txt")


