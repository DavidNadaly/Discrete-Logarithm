# Discrete-Logarithm-
Calculating the discrete log of mod17 by modular exponentiation.

Discrete log problem - Give a prime $p$, a primitive root $g$, and 
$h \not\equiv 0(modp)$ (which means $gcd(h,p)=1)$.
Find $x$ so that $g^x \equiv h(modp)$ or $Dis\log_{g}h \equiv x$. From Neilsen Chuang 
textbook we solve a complex function $f(x) \equiv a^{sx_{1} + x_{2}}(modN)$ where 
$a^{r} \equiv 1(modN)$, using discrete logarithm by taking $a^{s} = b$ 
and solving $s$ by $a^{r}(modN)$ and $b^{r}(modN)$ by modular exponentiation. 
The code is designed specifically for $a=4$, $b=13$ and $N=17$.

The cicuit is
![image](https://user-images.githubusercontent.com/115821009/199062117-ac901652-19b8-4497-8a23-3ac58c39d4ea.png)

The result gave out $s=35$ and more qubit are required
for efficiently finding the value of s. These kind of 
problem can be solved efficiently only if there is a
mechanism or a set of steps to find oracle for any
value of multiplication modulo N.
