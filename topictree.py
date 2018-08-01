class topic:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __str__(self):
        return self. name + ": " + str(len(self.children))

    def childgenerator(self): #doesn't really serve a purpose
        for child in self.children:
            yield child

#so you could have a class 'tree' and the only thing in it would be a list of root topics
class topictree:
    def __init__(self, inputs):
        self.__roots = [] #a topictree can have multiple roots (see output)
        ls = inputs.split(' ') #make this a local variable in final version
        self.__maketree(ls)

    def __maketree(self, inputls):
        tempP = self.__roots #P for primary #interact with this list to build a level
        pctr = -1 #to remember what index I'm at in tempP
        tempR = [] #R for return #interact with this list to change depth #TREAT AS STACK
        pctrls = []#a stack of indexes I need to return to
        for i in range(len(inputls)):
            #print(str(i) + " : " + inputls[i]) #for testing purposes
            
            if inputls[i] == '(': #means to go down a level
                tempR.append(tempP) #a stack of lists I will need to return to
                tempP = tempP[pctr].children 
                pctrls.append(pctr)
                pctr = -1
            elif inputls[i] == ')': #means to return up a level
                tempP = tempR.pop() #a list of lists
                pctr = pctrls.pop()
            else: #otherwise just keep adding to current level
                pctr+=1
                tempP.append(topic(inputls[i]))  
    def printtree(self):
        self.__printtree(self.__roots, "")

    def __printtree(self, lst, prepend):
        for topic in lst:
            print(prepend + str(topic))
            if len(topic.children) > 0:
                self.__printtree(topic.children, prepend+"- ")

#-------------------------
def main():
    x = 'Animals ( Reptiles Birds ( Eagles Pigeons Crows ) Mammals ( Cows ) ) Technology ( Software ( AI? ) Hardware )' #you'll always be adding to a list...so control which list you add to
    print('--------------------')
    ttree = topictree(x)
    print('--------------------')
    ttree.printtree()

if __name__ == '__main__':
    main()