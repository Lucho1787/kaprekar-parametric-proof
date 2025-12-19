def kaprekar_step(n):
    """Aplica una iteración de los pasos de Kaprekar."""
    s = f"{n:04d}"
    # Ordenar descendente y ascendente
    digits_desc = sorted(s, reverse=True)
    digits_asc = sorted(s)
    
    large = int("".join(digits_desc))
    small = int("".join(digits_asc))
    
    return large - small

def get_alpha_beta(n):
    """Extrae parámetros alpha (a-d) y beta (b-c)."""
    s = f"{n:04d}"
    d = sorted(s, reverse=True)
    # d[0]=a, d[1]=b, d[2]=c, d[3]=d
    return (int(d[0]) - int(d[3])), (int(d[1]) - int(d[2]))

def verify_dominance():
    # Diccionario para guardar el peor caso
    results = {a: {'max_steps': 0} for a in range(1, 10)}
    
    for n in range(10000):
        if n % 1111 == 0: continue
        
        steps = 0
        current = n
        while current != 6174 and steps <= 8:
            current = kaprekar_step(current)
            steps += 1
            
        if current == 6174:
            alpha, beta = get_alpha_beta(n)
            if steps > results[alpha]['max_steps']:
                results[alpha]['max_steps'] = steps

    print("Verificación completada.")

if __name__ == "__main__":
    verify_dominance




    