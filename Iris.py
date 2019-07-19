class IrisLoader:
    def __init__(self):
        self.data = []

    def load(self, path):
        try:
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    line = line.split(",")
                    data_1 = float(line[0])
                    data_2 = float(line[1])
                    data_3 = float(line[2])
                    data_4 = float(line[3])
                    name = line[4]

                    self.data.append((data_1, data_2, data_3, data_4, name))
        except FileNotFoundError:
            print("Plik nie istnieje")

    def built_dict(self):
        my_dictionary = {"Iris-setosa": [], "Iris-versicolor": [], "Iris-virginica": []}
        for element in self.data:
            if element[4] == "Iris-setosa":
                values = element[:4]
                my_dictionary["Iris-setosa"].append(values)

            elif element[4] == "Iris-versicolor":
                values = element[:4]
                my_dictionary["Iris-versicolor"].append(values)

            elif element[4] == "Iris-virginica":
                values = element[:4]
                my_dictionary["Iris-virginica"].append(values)

        return my_dictionary

    # mozna tak:
    # setosa_key = "Iris-setosa" i tak powymieniac w srokdu nazwy

    def built_dict_v2(self):
        my_dictionary = {}

        for element in self.data:
            key = element[4]
            if key not in my_dictionary:
                my_dictionary[key] = []
            my_dictionary[key].append(element[:4])

        return my_dictionary


def pretty_print_dictionary(my_dictionary):
    for key, value in my_dictionary.items():
        print("{}:{}".format(key, value))


#

if __name__ == '__main__':
    loader = IrisLoader()
    loader.load("iris.data")
    print(loader.data[:2])
    #    my_dictionary = loader.built_dict()
    #    print(my_dictionary)
    my_dictionary_1 = loader.built_dict_v2()
    pretty_print_dictionary(my_dictionary_1)
