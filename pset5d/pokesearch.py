import pokedex


def pokesearch(trait, minimum, maximum):
    """
    Returns a list of Pokemon data structures (dictionaries,
    as shown in the pset problem description) that
    have a value of trait between minimum and maximum
    """
    pokemon_list = []
    for pokemon in pokedex.data:
        if minimum <= pokemon['base'][trait] <= maximum:
            pokemon_list.append(pokemon)
    return pokemon_list


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the results of your pokemon search.
    trait = input('What Pokemon trait would you like to search on?\nValid traits are HP, Attack, Sp. Attack, Sp. Defense, Speed:')
    minimum = int(input('What is the minimum value for HP?'))
    maximum = int(input('What is the maximum value for HP?'))
    result = pokesearch(trait, minimum, maximum)
    res = sorted(result, key=english_name)
    print('The Pokemon that match are:')
    for x in res:
        print(f"{x['name']['english']:<19} {x['base'][trait]:^10}")


if __name__ == "__main__":
    main()
