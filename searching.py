import os
import json

# get current working directory path
cwd_path = os.getcwd()


def linear_search(searched_list, tested_integer):
    dictionary = {}
    indx = 0
    counter = 0
    positions_list = []
    for number in searched_list:
        if number == tested_integer:
            positions_list.append(indx)
            counter = counter + 1
        indx = indx + 1

    dictionary["positions"] = positions_list
    dictionary["count"] = counter
    return dictionary


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as json_file:
        my_dict = json.load(json_file)
    my_keys = my_dict.keys()

    if field not in my_keys:
        return None
    else:
        return my_dict[field]


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    search = linear_search(sequential_data, 0)
    print(search)
    pass


if __name__ == '__main__':
    main()
