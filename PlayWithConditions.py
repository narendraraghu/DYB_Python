n = 10

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#     in Java
#     if (n % 2 == 1) System.out.println("Weird");
#     else if (n % 2 == 0 & & n >= 2 & & n <= 5)
#     System.out.println("Not Weird");
#     else if (n % 2 == 0 & & n >= 6 & & n <= 20)
#     System.out.println("Weird");
#     else if (n % 2 == 0 & & n > 20)
#     System.out.println("Not Weird");

#Switch case
#Python does not really have a switch/case. if/elif/else are used instead.

for n in range(3) :
    print(n)

for c in "Raghu" :
  print(c)

#See c or n is only name not a special charactor


### While loop

n = 0
while True :
    n = n + 1
    print(n)
    if n==9 :
        break
print("Loop broke with n = ",n)