# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import linecache

import re

import re




class TicketCounter:

    class Ticket:
        def __init__(self, id, row, column):
            self.id = id
            self.row = row
            self.column = column

    def count_tickets(self,file_name):
        file = open(file_name)
        all_lines = file.readlines()
        passLines = []
        line_count = 0
        pass_line_count = 0
        num_lines = len(all_lines)
        tickets = []

        for line in all_lines:
           tickets.append(self.process_line(line))

        self.print_biggest(tickets)

    def print_biggest(self,tickets):
        biggest_id = 0
        for ticket in tickets:
            if ticket.id >= biggest_id:
                biggest_id = ticket.id
        print(biggest_id)

    def process_line(self,line):
        line = line.replace("\n","")
        row = self.get_row(line[:7])[0]
        column = self.get_column(line[7:])[0]
        print("row",row)
        print('column',column)
        id = self.seat_id(row,column)
        print("id", id)
        new_ticket = self.Ticket(id,row, column)
        return new_ticket

    def get_column(self,line):
        cols_remaining = []
        cols_remaining.extend(range(0, 8))
        for direction in line:
            half = int(len(cols_remaining) / 2)
            cols_remaining = cols_remaining[half:] if direction == 'R' else cols_remaining[:half]
        return cols_remaining

    def get_row(self,line):
        rows_remaining = []
        rows_remaining.extend(range(0,128))
        for direction in line:
            half = int(len(rows_remaining)/2)
            rows_remaining =  rows_remaining[half:] if direction == 'B' else rows_remaining[:half]
        return rows_remaining

    def seat_id(self,row,column):
        return int(row)*8+int(column)




    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tc = TicketCounter()
    tc.count_tickets("Inputs/Inputd5.txt")


