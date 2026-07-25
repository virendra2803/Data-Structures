#Maximum Product of Two Digits

n = 124
first = 0
second = 0

while n>0:
    rem = n%10
    n//=10
    if rem>first:
        second = first
        first = rem
    elif rem>=second:
        second = rem

print(first*second)
