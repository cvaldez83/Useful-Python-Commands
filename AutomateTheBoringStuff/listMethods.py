spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('howdy'))

#append() and insert() methods
spam = ['cat', 'dog', 'bat']
spam.append('mouse')
spam.append('mouse')
print(spam)

spam.insert(1,'chicken')
print(spam)

#remove method: removes instances based on value
spam.remove('mouse') #only removes 1 of the 'mouse' references
print(spam)

#delete method: removes instances based on index
del spam[0]
print(spam)

#reverse list
spam = spam[::-1]
print(spam)