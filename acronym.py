acronyms = {'CI': 'Continous Integration', 'CD': 'Continous Deployment'}
definition = acronyms.get('CM')   #Definition equals to None because the key doesn't exist

if definition:                    # False beacuse definition is None
    print(definition)
else:
    print("key doesn't exist")    # so this statement will be displayed

sentence = 'After' + ' ' + 'CI' + ' next step is to do ' + 'CD'
translation = acronyms.get('CI') + ' next step is to do ' + acronyms.get('CD')

print(sentence)
print(translation)