numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(len(numbers))
print('Numbers: ',numbers)
primes = []
not_primes = []
is_prime = True
#i = 2
for i in range(2, numbers[len(numbers)]):
    k = 1
    for j in range(2, i + 1):
    if i % j == 0:
is_prime = True:
    primes.append(i)
 #               k += 1
    else:

    not_primes.append(i)


 #           if is_prime == False:
  #              break



print('Primes:', primes)
print('Not Primes:',not_primes)



 #           if is_prime == False:
 #               break
 #   if is_prime == True:







