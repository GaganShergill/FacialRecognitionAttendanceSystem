from openpyxl import Workbook, load_workbook
import time
import os

def give_attendance(profiles):
    #get current date
    currentDate = time.strftime("%d.%m.%Y")
    path = './Pics_Taken/' + currentDate + '/attendance.xlsx'
    #create a workbook and add a worksheet

    wb = Workbook()
    #creating worksheet and giving names to column
    ws1 = wb.active
    ws1.title = "Cse1"
    ws1.append(('Roll Number', 'Name', '', currentDate))
    ws1.append(('', '', '', ''))
    profiles = sorted(profiles, key= lambda x: x[2])
    for profile in profiles:
        ws1.append((profile[2], profile[1]))

    #saving the file
    wb.save(filename = path)
