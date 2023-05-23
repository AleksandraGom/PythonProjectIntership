#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A collection of functions for xyz2gaussian

Created on Thu Sep  2 08:32:04 2021

@authors: A. Gomółka, T. Borowski
"""
import math, re

# print(function_name._doc_) - wyświetlenie dokumentacji docstring przeznaczonej dla funkcji o nazwie function_name

def count_lines(file):

    """
    Counts number of lines in a file

    Parameters
    ----------
    file : file object

    Returns
    -------
    i: int
        number of lines in a file
    """

    file.seek(0)
    i = -1
    for i, l in enumerate(file):
        pass
    file.seek(0)

    return i + 1


def int_digits(n):

    """
    For a positive integer n returns its number of digits

    Parameters
    ----------
    n : INT

    Returns
    -------
    digits : int
            number of digits

    """

    digits = int(math.log10(n))+1
    return digits


def read_head_tail(file):

    """
    Reading the contents of a file

    Parameters
    ----------
    file : file object

    Returns
    -------
    split_line: list
            a list containing the following lines of the file

    """

    file.seek(0)
    line = file.read()   # this line reads the entire file
    split_line = line.splitlines()
    file.seek(0)

    return split_line


# Funkcja float_finder(), składowa pierwszej wersji funkcji read_xyz() - wyodrębnia liczby zmiennoprzecinkowe dodatnie oraz
# liczby całkowite dodatnie
'''
def float_finder(splt_line):
    list = []
    for _, variable in enumerate(splt_line):
        if ((re.match("([0-9]+[.])+[0-9]+", variable)) or (re.match("^[0-9]+$", variable))):
            list.append(variable)
    return list

'''
# Element potrzebny do zapisu wyniku funkcji do pliku - wykorzystywany w pierwszej wersji funkcji read_xyz()
'''
file_name ="xyz_output_body3.txt"
file_output = open(file_name,'w')
'''
# Funkcja float_finder(), składowa pierwszej wersji funkcji read_xyz() - wyodrębnia liczby zmiennoprzecinkowe dodatnie i ujemne
# oraz liczby całkowite dodatnie i ujemne a także liczby zmiennoprzecinkowe w skróconej formie np: .3 lub 3.
'''
def float_finder(splt_line):
    list = []
    for _, variable in enumerate(splt_line):
        if ((re.match("^[-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$", variable)) or (re.match("^[-]?[0-9]+$", variable))):
            list.append(variable)
    return list
'''
# Funkcja float_line(), składowa pierwszej wersji funkcji read_xyz() - funkcja ta z kilku ciągów znakowych przedstawionych
# w postaci listy otrzymanej jako wynik funkcji "float_finder()" stworzyła jeden napis
'''
def float_line(file):
    #file.seek(0)
    split_line = file.readline()
    split_line = split_line.split()
    #file.seek(0)

    str = "  ".join(float_finder(split_line))
    return str
'''
# Pierwsza wersja funkcji read_xyz() - wyodrębnia koordynaty x,y i z z pliku body lub body_oniom, wykorzystując uprzednio
# stworzone funkcje dodatkowe
'''
def read_xyz_frs(file):

    file.seek(0)
    n_lines = count_lines(file)

    for _ in range(n_lines):
        file_output.write(float_line(file) + "\n")

    file.seek(0)
'''
# Druga wersja funkcji read_xyz() - wyodrębnia koordynaty x,y i z z pliku body lub body_oniom, nie wykorzystując żadnych
# dodatkowych funkcji - każda linia pliku jest splitowana i "skanowana" w celu odnalezienia liczb spełniających wyrażenie regularne
'''
def read_xyz_sec(file):
    file.seek(0)
    n_lines = count_lines(file)

    for _ in range(n_lines):
        str = ""
        split_line = file.readline()
        split_line = split_line.split()
        for i, variable in enumerate(split_line):
            if (re.match("([0-9]+[.])+[0-9]+", variable)):
                str = str + "  " + variable
        str.lstrip() # method removes whitespace at the beginning of a string
        print(str)

    file.seek(0)
'''
# Trzecia wersja funkcji read_xyz() - wyodrębnia koordynaty x,y i z z pliku body lub body_oniom, nie wykorzystując żadnych
# dodatkowych funkcji - tylko pierwsza linia jest splitowana a indexy koordynatów są zapisywane do nowej listy
'''
def read_xyz_thrd(file):
    file.seek(0)
    n_lines = count_lines(file)
    split_line = file.readline()
    split_line = split_line.split()

    index_floatList = []
    for i, variable in enumerate(split_line):
        if (re.match("([0-9]+[.])+[0-9]+", variable)):
            index_floatList.append(i)

    ints = [int(x) for x in index_floatList]


    for _ in range(n_lines):
        floatString = ""
        for j in range(len(ints)):
            floatString = floatString + "  " + split_line[ints[j]]
        floatString.lstrip()
        print(floatString)
        split_line = file.readline()
        split_line = split_line.split()

    file.seek(0)
'''

# Właściwa wersja funkcji read_xyz() - wyodrębnia koordynaty x,y i z z pliku oh_h2o.irc_ts.xyz
def read_xyz(file):

    """
    Listing x, y and z coordinates

    Parameters
    ----------
    file : file object

    Returns
    -------
    numberOfatoms : int
                number of atoms
    comment : str
            string containing the comment
    geo : list
        a list with x, y and z coordinates

    """

    comment = ""
    numberOfatoms  = int(file.readline())
    comment = file.readline() # taking a comment
    comment = comment.rstrip('\n')
    comment = comment.lstrip()

    #pattern = r"^\s+"
    #comment = re.sub(pattern, "", comment)
    geo = []

    for j in range(numberOfatoms):
        floatString = ""

        split_line = file.readline()
        split_line = split_line.split()
        split_line = split_line[1:]
        floatString = "  ".join(split_line)


        geo.append(floatString)

    return numberOfatoms, comment, geo

# Właściwa wersja funkcji read_body() - wyodrębnia dane poza koordynatami x,y i z
def read_body(file):

    """
    Listing all data except for coordinates x, y and z

    Parameters
    ----------
    file : file object

    Returns
    -------
    body : list
        a list of tuples containing all data except x, y and z

    """

    file.seek(0)
    body = []
    n_lines = count_lines(file)
    split_line = file.readline()
    split_line = split_line.split()

    index_floatList = []
    for i, variable in enumerate(split_line):
        if ((re.match("^[-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$", variable)) or (re.match("^[-]?[0-9]+$", variable))):
            index_floatList.append(i)

    ints = [int(x) for x in index_floatList]

    if (len(index_floatList) == 4):
        ints.pop(0)

    for _ in range(n_lines):
        bodyStringRight = ""
        bodyStringLeft = ""
        bodyStringLeft = "  ".join(split_line[:ints[0]])
        bodyStringRight = "  ".join(split_line[(ints[2] + 1):])
        #print(bodyStringLeft + "      " + bodyStringRight)
        body.append(tuple([bodyStringLeft,bodyStringRight]))
        split_line = file.readline()
        split_line = split_line.split()

    file.seek(0)
    return body


# Pierwsza wersja funkcji head_remove_guess() - usuwa z pliku wyrażenie "guess=read"
'''
def head_remove_guess(file):
    file_withoutGuess = file.replace("guess=read", "")
    print(file_withoutGuess)
'''
# Druga wersja funkcji head_remove_guess() - usuwa wyrażenie "guess=read" ale nie z pliku tylko z listy "head", zgodnie ze
# sposobem działania programu - uwzględnia, że to wyrażenie zawsze znajduje się w trzecim ciągu znakowym w liście
'''
def head_remove_guess(head):
    head_new = head.copy()
    line_withGuess = head_new[2]
    head_new.pop(2)
    head_withoutGuess = line_withGuess.replace("guess=read", "")
    head_new.insert(2, head_withoutGuess)

    return head_new
'''

# Właściwa wersja funkcji head_remove_guess() - uwzględnia, że wyrażenie, które podlega usunięciu może znajdować się w dowolnym
# stringu, czyli ostatecznie w dowolnym miejscu w pliku
def head_remove_guess(head):

    """
    Removing "guess = read" expression from head

    Parameters
    ----------
    head : list

    Returns
    -------
    new_head : list
        a list containing elements of a new head

    """

    head_new = head.copy()
    new_head = []
    for i in head_new:
        if "guess=read" in i:
            i = i.replace("guess=read","")

        new_head.append(i)
    return new_head


# Pierwsza wersja funkcji head_add_chk_label() - dodaje znacznik określający numer serii danych
# - nieprawidłowy sposób generowania numeru etykiety
'''
def head_add_chk_label(file,label_digits,index):
    file.seek(0)
    file_content = ""
    file_withLabel = ""
    split_fileContent = []
    file_content = head_remove_guess(file)
    label = str(0) * (label_digits - 1) + (str(index + 1))
    split_fileContent = file_content.split()
    print(split_fileContent)

    file.seek(0)
'''
# Druga wersja funkcji head_add_chk_label() - dodaje znacznik określający numer serii danych
# - uwzględnia, że linia podlegająca zmianie, czyli miejsce gdzie należy umieścić etykietę znajduje się na początku pliku,
# (linia ta jest pierwszym elementem listy)
# - prawidłowy sposób generowania numeru etykiety
'''
def head_add_chk_label_frs(head,label_digits,index):
    #head = head_remove_guess(head)
    line_withoutLabel = head[0]
    head.pop(0)
    start_fileName = line_withoutLabel.find("=") + len("=")
    end_filename = line_withoutLabel.find(".chk") # poprawić
    file_name = line_withoutLabel[start_fileName:end_filename]

    label = str(index).zfill(label_digits)
    fileName_withLabel = file_name + label
    head_withLabel = line_withoutLabel.replace(file_name,fileName_withLabel)
    head.insert(0, head_withLabel)

    return head
'''

# Właściwe wersje funkcji head_add_chk_label()
# Pierwsza wersja - uwzględnia, że linia podlegająca zmianie może się znajdować w dowolnym miejscu w pliku
# - umieszcza zmienioną linię (zawierająca etykietę) na początku pliku (jako pierwszy element listy)
def head_add_chk_label(head,label_digits,index):

    """
    Adding a label specifying the file number and data set number

    Parameters
    ----------
    head : list
    label_digits : int
    index : int

    Returns
    -------
    head_new : list
        a list containing elements of a new head

    """

    head_new = head.copy()
    line_withoutLabel = ', '.join([item for item in head_new if item.startswith('%Chk' or '%chk')])
    head_new.remove(line_withoutLabel)

    start_fileName = line_withoutLabel.find("=") + len("=")
    end_filename = line_withoutLabel.find(".chk") # the file must end with a ".chk" extension
    file_name = line_withoutLabel[start_fileName:end_filename]

    label = str(index).zfill(label_digits)
    fileName_withLabel = file_name + label
    head_withLabel = line_withoutLabel.replace(file_name,fileName_withLabel)
    head_new[0] = head_withLabel

    return head_new

# Druga wersja - umieszcza zmienioną linię (zawierająca etykietę) w miejsu występowania linii podlegającej zmianie
def head_add_chk_label(head,label_digits,index):
    head_new = head.copy()
    line_withoutLabel = ', '.join([item for item in head_new if item.startswith('%Chk' or '%chk')])
    index_line_withoutLabel = head_new.index(line_withoutLabel)
    #head_new.pop(index_line_withoutLabel)

    start_fileName = line_withoutLabel.find("=") + len("=")
    end_filename = line_withoutLabel.find(".chk") # the file must end with a ".chk" extension
    file_name = line_withoutLabel[start_fileName:end_filename]

    label = str(index).zfill(label_digits)
    fileName_withLabel = file_name + label
    head_withLabel = line_withoutLabel.replace(file_name,fileName_withLabel)
    #head_new.insert(0, head_withLabel)
    #head_new.insert(index_line_withoutLabel,head_withLabel)
    head_new[index_line_withoutLabel] = head_withLabel

    return head_new


# Funkcja head_addLabel_removeGuess() - jednocześnie usuwa z pliku wyrażenie "guess=read" oraz dodaje etykietę
'''
def head_addLabel_removeGuess(file,label_digits,index):
    file.seek(0)
    file_content = ""
    new_fileContent = ""
    label = ""
    #change_line = ""
    #change_line = file.readline()
    #new_fileContent = new_fileContent.replace(change_line, "")  # pierwsza linijka do poprawy - trzeba dodać label
    #print(new_fileContent)

    for i in range(count_lines(file)):
        file_content = file_content + file.readline()
        if (i == 0):
            file_content = ""

    label = str(0) * (label_digits - 1) + (str(index + 1))
    new_fileContent = "%Chk=oh_h2o.irc_ts_{}.chk\n".format(label) + file_content
    new_fileContent = new_fileContent.replace("guess=read", "")
    print(new_fileContent)
    #file.seek(0)
'''
# Pierwsza wersja funkcji head_add_oldchk() - dodaje określenie "Old" dla kolejnych, generowanych plików poza pierwszym
# - uwzględnia, że wyrażenie "%OldChk=oh_h2o.irc_ts_.chk" jest niezmienne dla każdego z tych plików
# - nieprawidłowy sposób generowania numeru etykiety
'''
def head_add_oldchk(file,label_digits,index):
    file.seek(0)
    file_content = ""
    new_fileContent = ""
    first_line = ""
    label = ""
    for i in range(count_lines(file)):
        file_content = file_content + file.readline()


    #label = str(0) * (label_digits-1) + (var)
    label = str(index+1)
    new_fileContent = "%OldChk=oh_h2o.irc_ts_{}.chk\n".format(label) + file_content
    print(new_fileContent)
    file.seek(0)
'''
# Druga wersja funkcji head_add_oldchk() - uwzględnia, że linia podlegająca zmianie, czyli miejsce gdzie należy umieścić
# etykietę znajduje się na początku pliku (pierwszy element listy)
# - prawidłowy sposób generowania numeru etykiety
'''
def head_add_oldchk(head,label_digits,index):
    head_firstLine = head[0] # pierwsza linia head
    head = head_add_chk_label(head, label_digits, index) # head z label

    start_fileName = head_firstLine.find("=") + len("=")
    end_filename = head_firstLine.find(".chk")
    file_name = head_firstLine[start_fileName:end_filename]

    label = str(index-1).zfill(label_digits)
    fileName_withLabel = file_name + label # '%Chk=oh_h2o.irc_ts_001.chk'
    head_withLabel = head_firstLine.replace(file_name, fileName_withLabel)

    start_old = head_withLabel.find("%") + len("%")
    head_with_oldAndlabel = head_withLabel[:start_old] + "Old" + head_withLabel[start_old:]
    head.insert(0, head_with_oldAndlabel)

    return head
'''

# Właściwa wersja funkcji head_add_oldchk() - uwzględnia, że linia podlegająca zmianie może się znajdować w dowolnym miejscu
# w pliku (jako dowolny element listy)
def head_add_oldchk(head,label_digits,index):

    """
    Adding a label specifying the previous file number with the phrase "Old"

    Parameters
    ----------
    head : list
    label_digits : int
    index : int

    Returns
    -------
    head_new : list
        a list containing elements of a new head

    """

    head_new = head.copy()
    head_firstLine = ', '.join([item for item in head_new if item.startswith('%Chk' or '%chk')])
    head_new = head_add_chk_label(head_new, label_digits, index) # head z label

    start_fileName = head_firstLine.find("=") + len("=")
    end_filename = head_firstLine.find(".chk") # the file must end with a ".chk" extension
    file_name = head_firstLine[start_fileName:end_filename]

    label = str(index-1).zfill(label_digits)
    fileName_withLabel = file_name + label # '%Chk=oh_h2o.irc_ts_001.chk'
    head_withLabel = head_firstLine.replace(file_name, fileName_withLabel)

    start_old = head_withLabel.find("%") + len("%")
    head_with_oldAndlabel = head_withLabel[:start_old] + "Old" + head_withLabel[start_old:]
    head_new.insert(0, head_with_oldAndlabel)

    return head_new


def head_change_comment(head, comm_line):

    """
    Adding a comment in place of the word "test"

    Parameters
    ----------
    head : list
    comm_line : str

    Returns
    -------
    new_head : list
        a list containing elements of a new head

    """

    new_head = head.copy()
    new_head[-3] = comm_line

    return new_head


def gen_file_name(xyz_fileName, label_digits,index):

    """
    Generating a file name - adding a label and changing the extension

    Parameters
    ----------
    xyz_fileName : str
    label_digits : int
    index : int

    Returns
    -------
    new_fileName : str
        a string that specifies the new file name

    """

    start_fileName = 0
    end_filename = xyz_fileName.find(".xyz")
    new_fileName = xyz_fileName[start_fileName:end_filename]

    label = str(index).zfill(label_digits) + ".com"
    new_fileName = new_fileName + label

    return new_fileName

# Właściwe wersje funkcji gen_new_body()
# Pierwsza wersja
def gen_new_body(body, geo):

    """
    Combining the contents of the body list with the contents of the geo list

    Parameters
    ----------
    body : tuples list
    geo : tuples list

    Returns
    -------
    newBody_list : list
        a list consisting of geo and body lists

    """

    list_length = len(body)
    newBody_list = []
    for i in range(list_length):
        newBody_list.append((body[i])[0] + "  " + geo[i] + "  " + (body[i])[1])

    return newBody_list

# Druga wersja
def gen_new_body(body, geo):
    list_length = len(body)
    newBody_list = []
    for i in range(list_length):
        if (len(body[i][1]) > 0):
            newBody_list.append((body[i])[0] + "  " + geo[i] + "  " + (body[i])[1])
        else:
            newBody_list.append((body[i])[0] + "  " + geo[i])

    return newBody_list

# Trzecia wersja
def gen_new_body(body, geo):
    list_length = len(body)
    newBody_list = []
    newBody = ""
    for i in range(list_length):
        if (len(body[i][1]) > 0):
            newBody = body[i][0] + "  " + geo[i] + "  " + body[i][1]
        else:
            newBody = body[i][0] + "  " + geo[i]
        newBody_list.append(newBody)

    return newBody_list

# Właściwe wersje funkcji write_g_input()
# Pierwsza wersja
def write_g_input(out_file_name, head_new, body_new, tail):

    """
    Create a file with specific content

    Parameters
    ----------
    out_file_name : str
    head_new : list
    body_new : list
    tail : list

    Returns
    -------
    Specified file containing head, body, x, y and z coordinates, and tail

    """

    file_output = open(out_file_name, 'w')

    for part in [head_new, body_new, tail]:
        for i in range(len(part)):
            file_output.write(part[i] + "\n")

    file_output.close()

# Druga wersja
def write_g_input(out_file_name, head_new, body_new, tail):

    file_output = open(out_file_name, 'w')

    for i in range(len(head_new)):
        file_output.write(head_new[i] + "\n")
    for j in range(len(body_new)):
        file_output.write(body_new[j] + "\n")
    for k in range(len(tail)):
        file_output.write(tail[k] + "\n")

    file_output.close()

# Trzecia wersja
def write_g_input(out_file_name, head_new, body_new, tail):
        file_output = open(out_file_name, 'w')

        file_output.write("\n".join(head_new))
        file_output.write("\n")
        file_output.write("\n".join(body_new))
        file_output.write("\n")
        file_output.write("\n".join(tail))

        file_output.close()

# Czwarta wersja
def write_g_input(out_file_name, head_new, body_new, tail):
    file_output = open(out_file_name, 'w')

    file_output.write("\n".join(head_new) + "\n" + "\n".join(body_new) + "\n" + "\n".join(tail))
    file_output.close()


def div_into_files(read_file):

    """
    Dividing the main,input file into smaller files named head, body, and tail

    Parameters
    ----------
    read_file : file

    Returns
    -------
    Files containing head, body and tail

    """

    blankLine_counter = 0
    head_end_index = 0
    body_end_index = 0
    file_output_head = open('head_test', 'w')
    file_output_body = open('body_test', 'w')
    file_output_tail = open('tail_test', 'w')

    for i, var in enumerate(read_file):

        if (read_file[i] == ''):
            blankLine_counter += 1
            if (blankLine_counter == 2):
                head_end_index = i + 2  # początek body (index)
            if (blankLine_counter == 3):
                body_end_index = i + 1  # początek tail (index)
                break

    file_output_head.write("\n".join(read_file[0:head_end_index]))
    file_output_body.write("\n".join(read_file[head_end_index:body_end_index]))
    file_output_tail.write("\n".join(read_file[body_end_index:]))
    
    file_output_head.close()
    file_output_body.close()
    file_output_tail.close()
