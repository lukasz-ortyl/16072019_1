from Company import Task

def print_lines_in_file(path):
    with open(path) as f:
        for line in f:
            line = line.strip()
            print(line)

def read_lines_in_file(path):
    with open(path) as f:
        return [line.strip() for line in f]

def read_tasks_from_file(path):
    tasks = []

    with open(path) as f:
        for line in f:
            line = line.strip()
# Teraz PARSUJEMY
            line = line.split(";")
            description = line[0]
            points = int(line[1])
            tasks.append(Task(description, points))
    return tasks


if __name__ == '__main__':
    #print_lines_in_file("tasks.txt")
    #lines_list = read_lines_in_file("tasks.txt")
    #print(lines_list)
    print(read_tasks_from_file("tasks.txt"))


