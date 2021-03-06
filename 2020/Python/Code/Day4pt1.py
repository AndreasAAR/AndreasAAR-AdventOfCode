# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re



class TreeCounter:
    pattern_len = 0
    tree = '#'
    ground = '.'
    valid_passports = 0;

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

    def correct_passport(self,token_lines,line_count):
        tokens = {}
        pairs = []
        if(len(token_lines) == 0):
            return False

        for line in token_lines:
            pairs.extend(line.split(" "))

        for pair in pairs:
            key = pair.split(":")[0]
            value = pair.split(":")[1]
            tokens[key] = value

        if not (self.correct_tokens(tokens.keys(),line_count)):
           return False
        return True



    def correct_tokens(self, tokens,line_count):
       if not 'byr' in tokens:
        #   print("byr miss at line" , line_count)
           return False
       if not 'iyr' in tokens:
         #  print("iyr miss at line", line_count)
           return False
       if not 'eyr' in tokens:
       #    print("eyr miss at line", line_count)
           return False
       if not  'hgt' in tokens:
        #   print("hgt miss at line", line_count)
           return False
       if not 'hcl' in tokens:
       #    print("hcl miss at line", line_count)
           return False
       if not  'ecl' in tokens:
       #    print("ecl miss at line", line_count)
           return False
       if not  'pid' in tokens:
        #   print("pid miss at line", line_count)
           return False
       return True

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nm = TreeCounter()
    nm.count_passports("Inputs/Inputd4.txt")


