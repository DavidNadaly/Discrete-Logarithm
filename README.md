# Discrete-Logarithm-
Calculating the discrete log of mod17 by modular exponentiation.

Discrete log problem - Give a prime $p$, a primitive root $g$, and 
$h \not\equiv 0(modp)$ (which means $gcd(h,p)=1)$.
Find $x$ so that $g^x \equiv h(modp)$ or $Dis\log_{g}h \equiv x$. From Neilsen Chuang 
textbook we solve a complex function $f(x) \equiv a^{sx_{1} + x_{2}}(modN)$ where 
$a^{r} \equiv 1(modN)$, using discrete logarithm by taking $a^{s} = b$ 
and solving $s$ by $a^{r}(modN)$ and $b^{r}(modN)$ by modular exponentiation. 
The code is designed specifically for $a=4$, $b=13$ and $N=17$.
