
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    
def eval_infix(ex):
    infstr= list(ex)
    infstr.insert(0, '(')
    infstr.append(')')
    for k in range(len(infstr) - 1):
        if infstr[k] =='*':
            if infstr[k + 1] == '*':
                infstr[k] = '^'
                infstr.pop(k + 1)
                
    
    numstack = Stack()
    opstack = Stack()
    num=""
    
    def ev(n2,n1,op):
        if op == "+" : return n2 + n1
        elif op == "-" : return n2 - n1
        elif op == "/" : return n2 / n1
        elif op == "*" : return n2 * n1
        elif op == "^" or op == "**": return n2 ** n1
    def opt (a):
        if a == "+" : return 0
        elif a == "-" : return 0
        elif a == "/" : return 1
        elif a == "*" : return 1
        elif a == "^" or a == "**": return 2
        elif a == "(" : return -1
    def numt(h):
        if h in "0123456789.":
            return True
        else: return False        
    while (len(infstr)>0):
        c=infstr[0]
        
        
        while numt(c) == True :
            num = num+c
            break
        if(num != "" and numt(c) == False) :
            numstack.push(float(num))
            num=""
        while c in "+-*/^":
            if opstack.size()>0:
                if (opt(opstack.peek()) >=  opt(c) ):
                    num1 = numstack.pop()
                    num2 = numstack.pop()
                    numstack.push(ev (num2,num1,opstack.pop()))
                    if opstack.size()>0:
                        if (opt(opstack.peek()) >=  opt(c) ):
                            num1 = numstack.pop()
                            num2 = numstack.pop()
                            numstack.push(ev (num2,num1,opstack.pop())) 
                            opstack.push(c)
                            break
                        else:
                            opstack.push(c)
                            break
                    else:
                        opstack.push(c)
                        break
                    
                else :
                    opstack.push(c)
                    break
            else :
                opstack.push(c)
                break
            
        while c == "(" :
            opstack.push(c)
            break
        
        while c == ")" :
            num1 = numstack.pop()
            num2 = numstack.pop()
            numstack.push(ev (num2,num1,opstack.pop()))
            if opstack.peek() == "(" :
                opstack.pop()
                break
        del infstr[0];

    
    while (numstack.size() > 0):
        if numt(c) == True :
            numstack.push(float(num))
        elif c in "+-*/^" :
            print ("error")
        elif c in ")":
            break

        c= "non"
        num1 = numstack.pop()
        num2 = numstack.pop()
        numstack.push(ev (num2,num1,opstack.pop()))
        
        if (opstack.size()==0):
            break
    
    return numstack.pop()
        
def main():
    expr=input("Please enter an infix expression: ")
    sortd = eval_infix(expr)  
    print("The result of", expr, "is", sortd)
    print(eval(expr))
    
if __name__ == '__main__':
    main()
