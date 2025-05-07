#def quadrado_perfeito(n):
#    if n == n**2:
#        return True
#    else:
#        return False
def quadrado_perfeito(n):
    return n >= 0 and int(n**0.5) ** 2 == n

def perto_quad_perfeito(n):
    return quadrado_perfeito(n) or quadrado_perfeito(n - 1) or quadrado_perfeito(n + 1)


assert perto_quad_perfeito(25) == True  
assert perto_quad_perfeito(24) == True  
assert perto_quad_perfeito(26) == True  
assert perto_quad_perfeito(36) == True  
assert perto_quad_perfeito(23) == False 
assert perto_quad_perfeito(16) == True
assert perto_quad_perfeito(17) == True  
assert perto_quad_perfeito(15) == True  
assert perto_quad_perfeito(14) == False