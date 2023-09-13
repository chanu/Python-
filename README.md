# Python-set.py
#SET :- 
 #Set Properties :-  
 """Set is UnOrderd 
    Set is mutable 
    inside the set we canot assing or add any list, is do not accept the list datatype 
    Set do not accept the duplicate values 
    set doesn't allow list is an ietem 
 """ 
 #Methods in Set :- 
 ''' 
    1)add(item) 
    2)remove(ietem) 
    3)discard(ietem) 
    4)pop() it will delete first item in set but pop(index) didn't work 
    5)clear() 
    6)del set[index] 
    7)del set_name 
    8)union(set_name) 
    9)difference(set_name) 
    10)symatricdifference(set_name) 
    11)subset() 
    12)superset() 
    13)intersection() 
 ''' 
 #FUNCTIONS IN SET 
 ''' 
    1)TYPE(SET_NAME) 
    2)LEN(SET_NAME) 
  
 ''' 
 myset={} 
 print(myset) 
 print("the size of the myset :",len(myset)) 
  
 #construct a set : 
 constructSet=set() 
  
 #creating a homogeneous Set : 
 homogeneousSet={1,2,3,4,5,6,7,8,9,10} 
  
 heterogeneousSet={"mango","fruits",100,200,(5,6,7,8),"this is"} 
  
 #remove one eliment in the existing set using remove() method : 
 heterogeneousSet.remove(100) 
 print("print the total set after removing one eliment to existing set :",heterogeneousSet) 
  
  
 #Adding one eliment to the existing set : 
 heterogeneousSet.add("nani") 
 print("print the total set after addoing one eliment to existing set :",heterogeneousSet) 
  
 #deleting one eliment in existing set using discard method : 
 heterogeneousSet.discard("mango") 
 print("print the total set after deleting perticular one eliment to existing set :",heterogeneousSet) 
  
 #we can delete ietems in set using pop() method,here pop wil deleye first eliment in the set, but it pop index method doesn't work : 
 heterogeneousSet.pop() 
 print("print the total set after deleting one eliment to existing set :",heterogeneousSet) 
  
 #clear total set using clear method : 
 heterogeneousSet.clear() 
 print("print the total set after using clear method :",heterogeneousSet) 
  
 #delete total set 
 # del heterogeneousSet 
  
 setA={1,2,3,4,5} 
 setB={5,6,7,8,9} 
  
 # example for union : 
 print("The union of setA and setB :",setA.union(setB)) 
  
 print("The size of unioun of setA and setB :",len(setA.union(setB))) 
  
  
  
  
 #multiple Set Oparations :- 
  
 setC=setA.union(setB) 
 setC.remove(5) 
 print(setC) 
  
 #intersection of setA and setB is : 
 print("The intersection of setA and SetB",setA.intersection(setB)) 
  
 #differece of setA and SetB is : 
 print("The difference of setA and SetB",setA.difference(setB)) 
  
 #difference of setB and setA is : 
 print("The difference of setB and SetA",setB.difference(setA)) 
  
 #symatric Difference of setA and setB is : 
 print("The symetricDifference of setA and SetB",setA.symmetric_difference(setB)) 
  
 #subset of setA and setB is : 
 print("the subset of setA and setB is :",setB.issubset(setA)) 
  
 #subset of setA and setB is : 
 print("the superset of setA and setB is :",setA.issuperset(setB)) 
  
 #