# For loop : to execute same line of code multiple times
fruits=["apple","banana","mango","guava"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
print("completed")
# here we are executing each print statement 3 times

scores = [90,88,95,78,78]
print( sum(scores)  )
print( sum(scores,2)  )     # (iterable,start) adds 2 to answer
print(max(scores))
print(min(scores))


scores = [90,88,95,78,78]
sum = 0
for score in scores :
    sum += score
print("Total score is :",sum)

scores = [90,88,95,78,78]
max = 0
for score in scores:
    if score > max :
        max = score
print("Maximum value is :",max)

# For loop with range function :
sum = 0
for item in  range(1,10,3):              # include 1 ,exclude 10 , step value by default 1
    print(item)                          # 1 \n 4\n 7
    sum += item
print(sum)