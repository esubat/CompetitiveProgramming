'''
challenge link : https://www.hackerrank.com/challenges/python-lists
'''


if __name__ == '__main__':
    N = int(input())
    commands=[]
    list = []
    
    for i in range(N):
        command = input().lower().split()
        commands.append(command)
    
    def command_handler(commands , lst):
        for cmd in commands:
            if cmd[0] == 'insert':
                lst.insert(int(cmd[1]) , int(cmd[2]))
            if cmd[0] == 'print':
                print(lst)
                # lst = lst
            if cmd[0] == 'remove':
                lst.remove(int(cmd[1]))
            if cmd[0] == 'append':
                lst.append(int(cmd[1]))
            if cmd[0] == 'sort':
                lst.sort()
            if cmd[0] =='pop':
                lst.pop()
            if cmd[0] == 'reverse':
                lst.reverse()
        # return lst 
            
    
    command_handler(commands , list)
        
            
