import sys
import unicodedata

words = [None, 0, ' '.join(sys.argv[1::])]

def print_unicode_table(words):

    print("decimal  hex  chr  {0:^40}".format("name"))
    print("------- ----- ---  {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if words.find(" ") == -1:
            if words == words[0] or words in name.lower():
                print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        else:
            j = words.split(" ")                #временный список
            count = 0                           #Добавляем счетчик для сравнения его с длинной списка
            for word in j:                      #Проходимся по элементам в списке
                if word in name.lower():        #Если элемент из списка находится в строке name, то увеличиваем счетчик
                    count += 1
                    if count == len(j):         #Сравниваем счетчик с длинной временного списка и если они равны, то выводим строку name
                        print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))

        code += 1

if len (sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = words[1]
    else:
        words = words[2].lower()
        if words != 0:
            print_unicode_table(words)


 
