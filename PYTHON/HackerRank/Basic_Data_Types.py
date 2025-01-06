array = []
def command_run(array, command, var1=None, var2=None):
    match command:
        case 'insert', array,var1, var2:
            array.insert(var1, var2)
        case 'print', array:
            print(array)
        case 'remove', array, var1:
            array.remove(var1)
        case 'append', array, var1:
            array.append(var1)
        case 'sort', array:
            array.sort()
        case 'pop', array:
            array.pop()
        case 'reverse', array:
            array.reverse()
for i in range(int(input())):
    command_run(array,input().split())
    
print(array)


    
