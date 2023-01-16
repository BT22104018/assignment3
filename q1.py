
stringname=str(input("Enter The String:"))
myList=stringname.split()
list_l=[]
for e in myList:
    lower_e=e.lower()
    list_l.append(lower_e)
set1=set(list_l)
dic={}
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
dic2={}       
set2={1,2}
set2.clear()  
list2=[]     
if len(myList)==1:
    
    for elements in stringname:
        list2.append(elements)
   
    for el in list2:
        set2.add(el.lower())
    
    string_l=stringname.lower()
    for elem in set2:
        
        dic2.update({elem:string_l.count(elem)})
    
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)

else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic) 