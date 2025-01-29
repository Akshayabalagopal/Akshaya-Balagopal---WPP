#index function- returns position of the element

#1.
ind="Hello world. Hello world"
ind_1="world"
print("a)", ind.index(ind_1))

ind="The sun is beautiful to watch"
ind_1="beautiful to"
print("b)", ind.index(ind_1,2,23))
'''
ind="Hello world"
ind_1="Python"
print("c)",ind.index(ind_1))
'''
#rindex function-highest index or last occurances.

#2
rind="Hello world, hello world"
rind_1="world"
print("a)", rind.rindex(rind_1))

rind="Beautiful sky, Beautiful mountains"
rind_1="Beautiful"
print("b)", rind.rindex(rind_1,0,24))

rind="Hello world"
rind_1="world"
print("c)",rind.rindex(rind_1))

#split-splits string to list of substrings

#3
spl="apple banana orange"
print(spl.split())

spl="apple,banana,orange"
print(spl.split(","))

spl="apple,banana,orange,guava"
print(spl.split(",", 2))

spl="apple:banana:orange"
print(spl.split(":"))

spl="applebananaorange"
print(spl.split('a',4))

#rsplit-from right

#4
rspl="apple banana orange"
print(rspl.rsplit())

rspl="apple,banana,orange"
print(rspl.rsplit(","))

rspl="apple,banana,orange,guava"
print(rspl.rsplit(",", 2))

rspl="apple:banana:orange"
print(rspl.rsplit(":"))

rspl="applebananaorange"
print(rspl.rsplit('a',4))

#find-sames as index but gives -1 if not present

#5
fnd="Hello world. Hello world"
fnd_1="world"
print("a)", fnd.find(fnd_1))

fnd="The sun is beautiful to watch"
fnd_1="beautiful to"
print("b)", fnd.find(fnd_1,2,23))

fnd="Hello world"
fnd_1="Python"
print("c)",fnd.find(fnd_1))

#rfind-same as rindex

#6
rfnd="Hello world, hello world"
rfnd_1="world"
print("a)", rfnd.rfind(rfnd_1))

rfnd="Beautiful sky, Beautiful mountains"
rfnd_1="Beautiful"
print("b)", rfnd.rfind(rfnd_1,0,24))

rfnd="Hello world"
rfnd_1="world"
print("c)",rfnd.rfind(rfnd_1))

#replace-will replace old word with new word

#7
rpl="apple apple orange apple"
print(rpl.replace("apple","banana"))

rpl="apple apple orange apple"
print(rpl.replace("apple","banana",2))

rpl="apple apple orange apple"
print(rpl.replace("guava","pear"))

rpl="apple apple orange apple"
print(rpl.replace("apple",""))

#count-counts no of occurances

#8
ct="apple apple orange apple"
print(ct.count("apple"))

ct="apple apple orange apple"
print(ct.count("apple",5))

ct="apple apple orange apple"
print(ct.count("apple",5,15))

ct="apple apple orange apple"
print(ct.count("banana"))

ct="Apple apple APPLE"
print(ct.count("apple"))

ct="ababab"
print(ct.count("ab",3,6))