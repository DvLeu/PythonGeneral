#Dictionary = A changeable, unordered collection of unique key : Values pairs
#              Fast because they use hashing, allow us to access a value quicky

capitals = {'USA' : 'Washington DC',
            'India' : 'New Dehli',
            'China' : 'Beijing',
            'Russia' : 'Moscow'}
capitals.update({'Germany':'Berling'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()
#print(capitals['Germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for i in capitals.items():
    print(i)