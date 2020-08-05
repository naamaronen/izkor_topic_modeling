import codecs
# Reading an excel file using Python
import xlrd
import os
import shutil
import WordCloud


# Give the location of the file
loc = "izkor-full-data-json-death-year.xlsx"
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(1, 21435):
    year = int(sheet.cell_value(i, 1))
    gender = sheet.cell_value(i, 2)
    filename = "txt" + str(i) + ".txt"
    source = "C:/Users/user/Documents/semester_f/science/project/no_stop_words_and_dotted/" + filename
    dest = "C:/Users/user/Documents/semester_f/science/project"
    if os.path.exists("no_stop_words_and_dotted/" + filename):
        if year <= 1900:
            decay = 1900
        elif (1900 < year <= 1910):
            decay = 1910
        elif (1910 < year <= 1920):
            decay = 1920
        elif (1920 < year <= 1930):
            decay = 1930
        elif (1930 < year <= 1940):
            decay = 1940
        elif (1940 < year <= 1950):
            decay = 1950
        elif (1950 < year <= 1960):
            decay = 1960
        elif (1960 < year <= 1970):
            decay = 1970
        elif (1970 < year <= 1980):
            decay = 1980
        elif (1980 < year <= 1990):
            decay = 1990
        elif (1990 < year <= 2000):
            decay = 2000
        elif (2000 < year <= 2010):
            decay = 2010
        elif (2010 < year <= 2020):
            decay = 2020
        shutil.move(source, dest + "/final/" + str(decay) + "_" + gender + "_" + filename)



