# 2Warm

## Can you convert the number 42 (base 10) to binary (base 2)? 

Alternatively you can use an online tool like [CyberChef](https://gchq.github.io/CyberChef/)

1. Divide the base 10 number by 2 and store the remainder.
2. Divide the quotient by 2 until the quotient is 0.
3. Write the remainders in reverse to get the binary value.

```
42 / 2 = 21; 42 % 2 = 0
21 / 2 = 10; 21 % 2 = 1
10 / 2 = 5;  10 % 2 = 0
5 / 2  = 2;  5 % 2 = 1
2 / 2  = 1;  2 % 2 = 0
1 / 2  = 0;  1 % 2 = 1

Flag: picoCTF{101010}
```

