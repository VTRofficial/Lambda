from pprint import pp


def open_csv():
    shoes = []
    with open('sneakers.csv', 'r', encoding='utf-8') as file:
        next(file)  # https://www.geeksforgeeks.org/python-next-method/
        for line in file:
            data = line.strip().split(',')
            shoes.append({
                'title': data[0],
                'color': data[1],
                'full_price': float(data[2]),
                'current_price': float(data[3]),
                'publish_date': data[4][:10]  # Csak az első 10 karakter (év-hónap-nap)
            })
    return shoes


def sort_shoes(shoes, key):
    sorted_shoes = sorted(shoes, key=lambda x: x[key])
    return sorted_shoes


def make_choice():
    print('Válasszon, melyik szempont alapján rendezzem a cipőket?')
    print('1 - title')
    print('2 - color')
    print('3 - full price')
    print('4 - current price')
    print('5 - publish date')
    choice = int(input('Adja meg a lehetőség számát! '))

    if choice == 1:
        key = 'title'
    elif choice == 2:
        key = 'color'
    elif choice == 3:
        key = 'full_price'
    elif choice == 4:
        key = 'current_price'
    elif choice == 5:
        key = 'publish_date'
    else:
        print('Érvénytelen választás!')
        return
    return key


def main():
    shoes = open_csv()
    key = make_choice()
    if key is None:
        return
    sorted_shoes = sort_shoes(shoes, key)
    print('\nRendezett cipők:')
    pp(sorted_shoes)


main()
