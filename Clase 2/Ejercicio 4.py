


heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
 
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"},
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}

info_heroes_reclutados = {}

for heroes in heroes_info:
    for reclutados in heroes_para_reclutar:
        if(heroes == reclutados):
            heroes_reclutados = {}
            heroes_reclutados ["id"] = heroes_info[reclutados]["ID"]
            heroes_reclutados ["Origen"] = heroes_info [reclutados]["Origen"]
            heroes_reclutados ["Habilidades"] = set(heroes_info [reclutados]["Habilidades"])
            heroes_reclutados ["Identidad"] = heroes_info [reclutados]["Identidad"]
            info_heroes_reclutados[reclutados] = heroes_reclutados
 
print(info_heroes_reclutados)


            