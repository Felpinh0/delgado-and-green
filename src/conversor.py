alqueire_paulista_em_ha = 2.42

def hectares_para_alqueires(hectares):
    alqueires = hectares / alqueire_paulista_em_ha
    return alqueires

resultado = hectares_para_alqueires(10)
print(f"10 ha = {resultado:.2f} alqueires")