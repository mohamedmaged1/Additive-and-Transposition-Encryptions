import string
import numpy as np

def Encruption( plainText,key):
    # key=[int(i) for i in str(key) if(i!=' ')]
    nomOfAddLetters=0

    plainText =''.join([i for i in list(plainText) if (i != ' ')])  
    plainText=str.lower(plainText)

    while((len(plainText)+nomOfAddLetters) % len(key)!=0):
         nomOfAddLetters+=1

    if(nomOfAddLetters>0):
        plainText+=string.ascii_lowercase[-nomOfAddLetters:]
    
    cipherText=['' for i in range(0,len(plainText))]

    rows=int(len(plainText)/len(key))
    matrix=np.array(list(plainText)).reshape(rows,len(key))
    # print(matrix)
    for k,i in enumerate(key) :
        cipherText[i-1]=''.join(matrix[:,k])
    

    return (''.join(cipherText) )    




def Decription(cipherText,key):
    # key=[int(i) for i in str(key) if(i!=' ')]

    rows=int(len(cipherText)/len(key))
    cols=len(key)

    theMatrix = [[] for _ in range(rows)]
    for index, item in enumerate(list(cipherText)):
        theMatrix[index % rows].append(item)

    theMatrix=np.array(theMatrix).reshape(rows,cols)

    originMatrix=np.array(['' for i in range(0,rows*cols)]).reshape(rows,cols)
    
    for k,i in enumerate(key) :
        originMatrix[:,k]=theMatrix[:,i-1]

    listOfTexts=[originMatrix[i,:] for i in range(0,rows)]

    plainText=''
    for i in listOfTexts:
        plainText+=''.join(i)
    
    return plainText 

