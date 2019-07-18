def write_line(path, text_line):
    with open(path, 'w') as f: # r jest automatem i czyta ale w juz trzeba pisac do pisania tworzy nowy i nadpisuje stary
        f.write(text_line)

def write_line_twice(path, text_line):
    with open(path, 'w') as f:
        f.write("{}\n".format(text_line))
        f.write("{}\n".format(text_line))

def write_names_to_file(path, names):
    with open(path, 'w') as f:
        for name in names:
            f.write("{}\n".format(name))

def append_line_to_file(path, text_line):
    with open(path, 'a') as f:
        f.write("{}\n".format(text_line))

if __name__ == '__main__':
    #write_line('writing.txt', "Ala ma kota2")
    #write_line_twice('writing.txt', "Ala ma kota2")
    #write_names_to_file('writing.txt', ["Lukasz", "Tomasz", "Przemo"])
    append_line_to_file('writing.txt', "Ewa")