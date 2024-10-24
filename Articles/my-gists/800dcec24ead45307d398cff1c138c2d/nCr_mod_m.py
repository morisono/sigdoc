def nCr_mod_m(n, r, m):
    if r == 0:
        return 1
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % m
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], -1, m)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % m
    return (fact[n] * inv_fact[r] * inv_fact[n - r]) % m
