"""
convert C++ to Python

vector <bool> sieve(int n) {
    vector <bool> isPrime(n + 1, true);
    vector <int> primes;
    if (n < 2) return {};
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= n; ++i) {
        if (isPrime[i] == true) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    for (int i = 2; i <= n; ++i){
        if (isPrime[i]) primes.push_back(i);
    }
    return primes;
}
"""

#Python
def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

"""
Difference from C++:
1. vector<bool> is a specialized container that optimizes memory by storing each boolean as a single bit, while Python's list stores each boolean as a full object.
2. The syntax for loops and range is different in Python compared to C++.

"""