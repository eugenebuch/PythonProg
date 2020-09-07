def sort(a):
# Процедура, выполняющая сортировку вставками, работающая по ссылке на список
    for i in range(1, len(a)):
        ins = a[i]
        j = i - 1
        while j >= 0 and a[j] > ins:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = ins
        
def printList(a):
# Процедура, выполняющая поэлементную печать элементов списка
    for elem in a:
        print(round(elem, 2))

def fileSave(a):
# Процедура, сохраняющая элементы списка в файл (построчно). Если файл не существует, то он создается в той же папке, что и программа
    with open("output.txt", "w") as file:
        for elem in a:
            file.write(str(round(elem, 2)) + '\n')

def main():
# Основная процедура, сюда вынесены управляющие элементы и вызовы других процедур (wrapper)
    n = 10
    print("Введите произвольное количество цифр через пробел")
    lst = list(map(lambda x: float(x)*0.13, input().split(' ')))
    sort(lst)
    printList(lst)
    fileSave(lst)
    
main()
