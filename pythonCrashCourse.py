#price=300
#print(price**0.5)

#import math
#math.sqrt(price)

#stock_index = "SP500"
#print(stock_index[2: ])
#price = 300
#print("The {} is at {} today.".format(stock_index,price))


stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
#use indexing and key calls to grab the following
#Yesterday's SP500 price of 250
#the # 365 nested inside list nested inside 'info' key
print(stock_info['sp500']['yesterday'])
print(stock_info['info'][1][2])

"PRICE:345.324:SOURCE--QUANDL"
def source_finder(s):
    return s.split('--')[-1]
print(source_finder("PRICE:345.324:SOURCE--QUANDL"))

def price_finder(s):
    return 'price' in s.lower()
print(price_finder("What is the price?"))
print(price_finder("DUDE, WHAT IS THE PRICE!!!"))
print(price_finder("The price is 300"))

#TASK 6
#below is not working
#create a function that counts time 'price' appears
#def count_price(s):
#    count = 0
#    for word in s.lower().split():
#        if 'price' in word:
#            count += 1
#    return count
#print(count_price("number is "))

#simpler option
#below is not working
#def count_price(s):
#    return s.lower().count('price')
#s = 'That is a nice price, very nice Price. I said price a lot. Priceless!')
#print(count_price("number is "))
#s = 'That is a nice price, very nice Price. I said price a lot. Priceless!')

#TASK 7
#this works!
def avg_price(stocks):
    return sum(stocks)/len(stocks)
    #avg_price([3,4,5])
print(avg_price([3,4,5]))

print(1+1)
print(2**4)
print(4%2)
print(5%2)
print((2+3)*(5+5))
x=2
y=3
z=x+y
print(z)

num=12
name="Sam"
print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))
print('My number is: {}, and my name is: {}'.format(num,name))

#for loops
seq=[1,2,3,4,5]
for item in seq:
    print(item)
for item in seq:
    print('Yep')
for jelly in seq:
    print(jelly + jelly)
for comey in seq:
    print(comey - comey**2)
    
#while loops
#    i=1
#    while i<5:
#        print('i is: {}'.format(i))
#        i=i+1

#methods
st = "hello, my name is Sam"
print(st.lower())
print(st.upper())
print(st.split())

#not working
#lst = [1,2,3]:
#lst.pop()
#print(lst())















