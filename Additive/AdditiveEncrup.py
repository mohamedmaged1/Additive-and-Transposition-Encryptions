import string

l=list(string.ascii_lowercase)
l.append(" ")

dic={i:k for k, i in enumerate(l)}

def get_key(val):
    for key, value in dic.items():
         if val == value:
             return key

def Encruption (context,code):
    context=str.lower(context)
    Enc=[ get_key((dic[i]+code )%27 ) for i in context ] 
    return "".join(Enc) 

def Decription (context,code): # 27 because of space 
    
    Dec=[ get_key((dic[i]-code+27 )%27 ) for i in context ] 
    return "".join(Dec) 

