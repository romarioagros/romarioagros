import glob
import os.path



files = glob.glob("*.sql")

for item in range(10):
        word = input("введите слово или его часть для поиска")
        temp_file = []
        for file in files:
            if word.lower() in file.lower():
                temp_file.append(file)
                print (file)
        
        if len(temp_file)== 0:
            print (" файлов содержащих в названиии ,", word, "не найдено")
        else:
            files =temp_file
            print ( "всего найдено файлов, содержащих " , word  ,"--" , len(temp_file))

