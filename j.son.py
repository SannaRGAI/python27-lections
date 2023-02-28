#Java script object notation - edinyii format, v kot mogut hranitsya tolko te tipy dannyh, kot est vo vseh jap podderjivajushije json 

# chisla int, float 
#stroki str
# slovari
# bool , true false 
#spiski,list 
# pustoe znachenije 

#import json 
#serialiazija -  perevod  iz python v Json (dump)(dumps - funcion kot convert python object to Json str)
#deserializacia - perevod iz JSON v Python (load)(load - function  kot perevodit json str v python object)

#dump 
#load
python_list = [1,2,3]
json_list = json.dumps(python_list) #list
print(type(json_list)) #str

json_dict = '{"a":1,"b":2}'
python_dict = json.loads(json_dict)


print(type(json_list)) #str
print(type(python_dict)) #dict 

list_ = [1,2,3,4,5##### suka bliat kak  doljno eto but v novom faile 
(1,3,4).  
{"a":1}
"hello" ######

with open("test.json","w") as file:
    json.dump(list_,file)

    with open("test.json","r")as file:
        res = json.load(file)
        print 