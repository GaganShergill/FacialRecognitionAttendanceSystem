from openpyxl import Workbook, load_workbook
import os
import sqlite3


def create_spreadsheet():
    #database connection
    conn = sqlite3.connect('Facial_Recog/Personal_project/recognizer/Face-Database.db')
    c = conn.cursor()
    wb = Workbook()
    dest_filename = 'Facial_Recog/Personal_project/recognizer/reports.xlsx'
    c.execute("SELECT * FROM Students ORDER BY Roll ASC")

    #creating worksheet and giving names to column
    ws1 = wb.active
    ws1.title = "Cse1"
    ws1.append(('Roll Number', 'Name'))
    ws1.append(('', '', '', ''))

    #entering students information from database
    while True:
        a = c.fetchone()
        if a == None:
            break
        else:
            ws1.append((a[2], a[1]))

    #saving the file
    wb.save(filename = dest_filename)
