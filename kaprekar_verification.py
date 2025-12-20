def kaprekar_step(n):
    """Applies one iteration of the Kaprekar routine."""
    # Sort once: s is ascending. s[::-1] is descending.
    s = sorted(f"{n:04d}")
    return int("".join(s[::-1])) - int("".join(s))

def get_alpha_beta(n):
    """Extracts alpha (a-d) and beta (b-c) parameters."""
    d = [int(x) for x in sorted(f"{n:04d}", reverse=True)]
    return (d[0] - d[3]), (d[1] - d[2])

def verify_dominance():
    # Store worst case: {alpha: {'max_steps': 0, 'critical_beta': -1}}
    results = {a: {'max_steps': 0, 'critical_beta': -1} for a in range(1, 10)}
    
    for n in range(10000):
        if n % 1111 == 0: continue # Ignore repdigits
        
        steps, current = 0, n
        while current != 6174 and steps <= 8:
            current = kaprekar_step(current)
            steps += 1
            
        if current == 6174:
            alpha, beta = get_alpha_beta(n)
            if steps > results[alpha]['max_steps']:
                results[alpha].update({'max_steps': steps, 'critical_beta': beta})
                
    print("Alpha Class | Critical Beta | Max Steps")
    for alpha in sorted(results, reverse=True):
        print(f"{alpha:^11} | {results[alpha]['critical_beta']:^13} | {results[alpha]['max_steps']:^9}")

if __name__ == "__main__":
    verify_dominance()





    
