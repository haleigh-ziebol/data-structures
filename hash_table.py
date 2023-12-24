#create dictionary to represent library catalog
library_catalog = {}

#insert books into catalog

library_catalog['Brother'] = 'Horror'
library_catalog['1984'] = 'Dystopian'
library_catalog['Python Crash Course'] = 'Programming'

#Retrive genre of specific book
genre = library_catalog.get('1984', 'Not found')

#delete book
del library_catalog['Tripwire']

## do not keep track of order of elements, heavy on memory (often allocated more space than needed)
# complex operations are not as easy (range queries or sorted data)