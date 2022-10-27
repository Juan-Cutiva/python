def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia" }

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia" },
        {"firstname": "Miguel", "lastname": "Vanegas" },
        {"firstname": "Juan", "lastname": "Cutiva" },
        {"firstname": "Andres", "lastname": "Lopez" },
        {"firstname": "Nicolle", "lastname": "Perez" },
    ]

    super_dict = {
        "natural_nums": [1, 2, 2, 4, 5],
        "integral_nums": [-1, -2, 0, 1, 2,],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for i in super_list:
        print(i.items())

if __name__ == "__main__":
    run()