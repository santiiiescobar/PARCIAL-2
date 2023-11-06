class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

class Pokedex:
    def __init__(self):
        self.pokemon_by_name = {}  
        self.pokemon_by_number = {}  
        self.pokemon_by_type = {}  

    def add_pokemon(self, pokemon):
        self.pokemon_by_name[pokemon.nombre] = pokemon
        self.pokemon_by_number[pokemon.numero] = pokemon
        for tipo in pokemon.tipos:
            if tipo in self.pokemon_by_type:
                self.pokemon_by_type[tipo].append(pokemon)
            else:
                self.pokemon_by_type[tipo] = [pokemon]

    def search_by_name(self, name):
        results = []
        for pokemon_name in self.pokemon_by_name.keys():
            if name in pokemon_name:
                results.append(self.pokemon_by_name[pokemon_name])
        return results

    def list_by_number(self):
        return sorted(self.pokemon_by_number.values(), key=lambda x: x.numero)

    def list_by_name(self):
        return sorted(self.pokemon_by_number.values(), key=lambda x: x.nombre)

    def list_names_by_type(self, tipo):
        if tipo in self.pokemon_by_type:
            return [pokemon.nombre for pokemon in self.pokemon_by_type[tipo]]
        else:
            return []

    def get_pokemon_info(self, names):
        return [self.pokemon_by_name[name] for name in names]

    def count_by_type(self, tipo):
        if tipo in self.pokemon_by_type:
            return len(self.pokemon_by_type[tipo])
        else:
            return 0

pokedex = Pokedex()

pokedex.add_pokemon(Pokemon("Bulbasaur", 1, ["planta", "veneno"]))
pokedex.add_pokemon(Pokemon("Charizard", 6, ["fuego", "volador"]))
pokedex.add_pokemon(Pokemon("Pikachu", 25, ["eléctrico"]))
pokedex.add_pokemon(Pokemon("Squirtle", 7, ["agua"]))
pokedex.add_pokemon(Pokemon("Vaporeon", 134, ["agua"]))
pokedex.add_pokemon(Pokemon("Charmander", 4, ["fuego"]))
pokedex.add_pokemon(Pokemon("Venusaur", 3, ["planta", "veneno"]))
pokedex.add_pokemon(Pokemon("Raichu", 26, ["eléctrico"]))
pokedex.add_pokemon(Pokemon("Magnezone", 462, ["eléctrico", "acero"]))
pokedex.add_pokemon(Pokemon("Jolteon", 135, ["eléctrico"]))
pokedex.add_pokemon(Pokemon("Lycanroc", 745, ["roca"]))
pokedex.add_pokemon(Pokemon("Tyrantrum", 697, ["roca", "dragón"]))

#Punto B
print("Resultados de búsqueda por nombre (para 'bul'):")
results = pokedex.search_by_name("bul")
for pokemon in results:
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipos: {pokemon.tipos}")

#Punto C
print("\nNombres de Pokémon de tipo 'planta':")
print(pokedex.list_names_by_type("planta"))

print("\nNombres de Pokémon de tipo 'fuego':")
print(pokedex.list_names_by_type("fuego"))

print("\nNombres de Pokémon de tipo 'agua':")
print(pokedex.list_names_by_type("agua"))

print("\nNombres de Pokémon de tipo 'eléctrico':")
print(pokedex.list_names_by_type("eléctrico"))

#Punto D
print("\nListado de Pokémon por número:")
for pokemon in pokedex.list_by_number():
    print(f"Número: {pokemon.numero}, Nombre: {pokemon.nombre}")

#Punto E
pokemon_info = pokedex.get_pokemon_info(["Jolteon", "Lycanroc", "Tyrantrum"])
print("\nInformación de Pokémon Jolteon, Lycanroc, Tyrantum:")
for pokemon in pokemon_info:
    print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipos: {pokemon.tipos}")

#Punto F
print("\nCantidad de Pokémon de tipo 'eléctrico':", pokedex.count_by_type("eléctrico", ))

print("\nCantidad de Pokémon de tipo 'acero':", pokedex.count_by_type("acero"))
