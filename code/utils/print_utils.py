
def print_iterable_binary(elements: Iterable, start: str = ''):
    for element in elements:
        if isinstance(element, List):
            print_iterable_binary(element, start + '\t')
            continue

        if isinstance(element, str):
            print(start + "- " + element)
            continue

        print_to_str(start + "- ", element)


def print_to_str(element, start: str = ''):
    print(start + str(element))
