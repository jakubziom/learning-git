print("Lista Zakupów")
shopping_dict={'piekarnia':['chleb','pączek','bułki'],'warzywniak':['marchew','seler','rukola']}
shopping_items_count=[]

for item in shopping_dict:
    print('Idę do ' + str(item).capitalize() + ', kupuję tu następujące rzeczy: ' + str(shopping_dict[item]).title())
    shopping_items_count.append((len(shopping_dict[item])))
 
print('W sumie kupuję ' + str(sum(shopping_items_count)) + ' rzeczy.')

#to jest pierwszy commit
#to jest drugi commit
