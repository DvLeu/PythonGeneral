#Set = collection wich unordered, unindexed. NO DUPLICATED VALUES
utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("Napkin") #Add item
#utensils.remove("fork") #Delete item
#utensils.clear()#Clear set
#dishes.update(utensils) #Update set
#dinner_table = utensils.union(dishes)
#for x in dinner_table:
#   print(x)
#print(dishes.difference(utensils))
print(utensils.intersection(dishes))