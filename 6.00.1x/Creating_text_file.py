import sys

def write():
    print('Creating new text file') 

    #name = raw_input('Enter name of text file: ')+'.txt'  # Giving name to the file

    try:
        #doc = open(name, 'w')   # Creating file
        #doc.close()
        print('Creating new text file') 
    
        summary = open('summary.txt', 'w')   # Creating file
        oldOPT = open('OPT_v13.opt', 'r')
        linesOldOPT = oldOPT.readlines()
        newOPT = open('OPT_v15.opt', 'r')
        linesNewOPT = newOPT.readlines()
        
        for i in range(len(linesOldOPT)):
            if linesOldOPT[i][0] == '[':
                summary.writelines(linesOldOPT[i])
        
        for i in range(len(linesNewOPT)):
            if linesNewOPT[i][0] == '[':
                summary.writelines(linesNewOPT[i])
        
        
        
        summary.close()
                                                
        print linesOldOPT
        print linesNewOPT
        print len(linesOldOPT)
        print len(linesNewOPT)
        summary = open('summary.txt','r')
        linesSummary = summary.readlines()
        print linesSummary
        print len(linesSummary)
        summary.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()