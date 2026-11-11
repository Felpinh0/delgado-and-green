ALQUEIRE_PAULISTA_EM_HA = 2.42

def hectares_para_alqueires(hectares):
    alqueires = hectares / ALQUEIRE_PAULISTA_EM_HA
    return alqueires

resultado = hectares_para_alqueires(10)
print(f"10 ha = {resultado:.2f} alqueires")

def alqueires_para_hectares(alqueires):
    hectares = alqueires * ALQUEIRE_PAULISTA_EM_HA
    return hectares

resultado = alqueires_para_hectares(4.13)
print(f"4.13 alqueires = {resultado:.0f} hectares")
print(resultado)

