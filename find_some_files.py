#!/usr/bin/env python
# -*- coding: utf-8 -*-


import glob
import os.path
import unicodedata


files = glob.glob("*.sql")


while True:

        word = input("введите слово или его часть для поиска")
        temp_file = []
        for file in files:

            f = open(file, encoding='utf-8', errors='ignore')
            for line in f:

                if (word.lower() in line.lower() ) and (file not in temp_file):
                    temp_file.append(file)
            f.close()

        if len(temp_file)== 0:
            print (" файлов содержащих в названиии ,", word, "не найдено")
        else:
            files =temp_file
            for row in temp_file:
                print (row)
        print ( "всего найдено файлов, содержащих " , word  ,"--" , len(temp_file))

