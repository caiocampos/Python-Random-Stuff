"""
Verifica possíveis pizzas
"""

NAME_LENGTHS = [
    10,
    10,
    17,
    13,
    10,
    8,
    10,
    13,
    9,
    7,
    11
]

NAMES = [
    "Americana",
    "Atum",
    "AtumSólido",
    "AtumComCebola",
    "Bacon",
    "Baiana",
    "Brócolis",
    "Caipira",
    "Calabresa",
    "CincoQueijos",
    "QuatroQueijos",
    "Escarola",
    "Mussarela",
    "Muçarela",
    "Lombinho",
    "FrangoCatupiry",
    "FrangoComCatupiry",
    "Marguerita",
    "Margherita",
    "Milho",
    "Napolitana",
    "Portuguesa",
    "Toscana",
    "Mexicana",
    "Vegetariana",
    "Nutella",
    "NutellaComFrutas",
    "NutellaComMorango",
    "CremeDeAvelã",
    "CremeDeAvelãComFrutas",
    "CremeDeAvelãComMorango",
    "RomeuEJulieta",
    "RomeuJulieta",
    "Brigadeiro",
    "Baiana",
    "Califórnia",
    "Abacaxi",
    "Alhoeóleo",
    "Aliche",
    "Aspargos",
    "Basca",
    "Bauru",
    "Camarão",
    "Carneseca",
    "Chester",
    "Gorgonzola",
    "Lombo",
    "Mafiosa",
    "Morango",
    "Palmito",
    "Pepperone",
    "Peruana",
    "SeteAnões",
    "Tomate",
    "Anchovas",
    "Banana",
    "Chocolate",
    "Cocada",
    "Coreana",
    "CoceDeLeite",
    "Palmito",
    "PeitoDePeru",
    "Pomodoro",
    "PéDeMoleque",
    "Salame",
    "Salaminho",
    "Siciliana",
    "Presunto",
    "Presuntinho",
    "Montreal",
    "Alvorada",
    "Romana",
    "BaconEMilho",
    "CornBacon",
    "CornAndBacon",
    "Berinjela",
    "Brasileira",
    "Bombom",
    "Catupiry",
    "DoceDeLeite",
    "Espinafre",
    "Havaiana",
    "Jardineira",
    "Pretigio",
    "Provolone",
    "Strogonoff",
    "RúculaComTomateSeco",
    "Champignon",
    "Espanhola",
    "Paçoca",
    "Prestígio",
    "Sensação",
    "Beijinho",
    "MeM",
    "MM",
    "Sorvete",
    "Paçoca"
]

def run():
    """
    Verifica possíveis pizzas
    """
    res = ""
    for i, name_length in enumerate(NAME_LENGTHS):
        res += f"{i}\n"
        for name in NAMES:
            if len(name) == name_length:
                res += f"{name}\n"

        res += "\n\n"

    with open("res_pizza.txt", "w", encoding="utf-8") as file:
        file.write(res)

run()
