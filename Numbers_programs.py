
import math as m

# 1. prime number

def prime(num, fcount=0):
    for f in range (1, num+1):
        if (num %f == 0):
            fcount +=1
    return fcount == 2


# 2. composite number:

def composite(num, fcount=0):
    for f in range (1, num+1):
        if(f%num == 0):
            fcount += 1
    return f!=2


# 3. perfect  number:

def perfect(num, fsum =0):
    for f in range (1, num//2+1):
        if (num%f == 0):
            fsum+=f
    return fsum == num


# 4. pronic number 

def pronic(num, n = 0):
    while (n*(n+1) <= num):
        if (n*(n+1)== num):
            return True
        else:
            n+=1
    return False




# 5. Niven num:

def n_sum(num, dsum = 0):
    while (num != 0):
        dsum += num % 10
        num //= 10
    return dsum
def niven(num):
    return (num % n_sum(num) == 0) 


# 6. Sunny number: (n** = num+1)

def sunny(num, n = 1):
    while (n**2 <= num+1):
        if(n**2 == num+1):
            return True
        else:
            n += 1
    return False


# 7. Spy number

def s_prod(num, pro = 1):
    while (num != 0):
        pro *= num%10
        num//=10
    return pro

def spy(num):
    return n_sum(num) == s_prod(num)

# 8. Neon number

def neon(num):
    return num == n_sum(num ** 2)

# 9.Armstrong number

def arm_sum(num , p, dsum= 0):
    while (num != 0):
         rem = num% 10
         dsum += rem ** p
         num //=10
    return dsum

def armstrong(num):
    return num == arm_sum(num, len(str(num)))


# 10. disarium number:

def dis_sum(num, p, dsum = 0):
    while (num != 0):
        rem = num % 10
        dsum += rem ** p
        num //= 10
        p-=1
    return dsum

def disarium(num):
    return num == dis_sum(num, len(str(num)))


# 11. palindrom number 

def reverse(num, rev = 0):
    while(num != 0):
        rem = num % 10
        rev = rev*10 + rem
        num//=10
    return rev

def palindrom(num):
    return reverse(num) == num


#12. palyprime

def palyprime(num):
    return num == reverse(num) and prime(num) 


# 13. emirp number

def emrip(num):
    return num != reverse(num) and prime(num) and prime(reverse(num))  

# 14. evil number:

def binary(num, count = 0):
    count+= num %2
    num//=2
    return count

def evil(num):
    return binary(num)%2 == 0

# 15. Strong number

def strong_sum(num, dsum = 0):
    while num != 0:
        rem = num %10
        dsum += m.factorial(rem)
        num //= 10
    return dsum
def strong(num):
    return num == strong_sum(num)

# 16. Happy number 

def happy_sq(num):
    if num <9:
        dsum = 0
        while num != 0:
            rem = num % 10
            dsum += rem ** 2
            num //= 10
        num = dsum
    return num

def happy(num ):
        return happy_sq(num) == 1 

# 17. Automarfic number 

def automarfic(num):
    return num == (num**2) % 10 ** len(str(num))

def trimarfic(num):
    return num == (num**3) % 10 ** len(str(num))







