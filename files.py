from Company import Task, SalariedEmployee, HourlyEmployee, Company


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
# dopisuje plik do zmiennej f
        for line in f:
            try:
                line = line.strip()
# usuwa znaki enter z pliku
# Teraz PARSUJEMY
                line = line.split(";")
# dzieli tekst po taki znaku split zapisuje do listy !!! [kup banany, 10]
                description = line[0]
                points = int(line[1])
#musi być int aby Py wiedział ze ma do czynienia z liczbą bo z pliku traktuje liczbę jak string
                tasks.append(Task(description, points))
            except Exception:
                print("{} is wrong. Cannot parse".format(line))
                print()
    return tasks

def read_salaried_employees_from_file(path):
    empls_list = []

    with open(path) as f:
        for line in f:
            line = line.strip()
            line = line.split(";")
            name = line[0]
            week_salary = int(line[2])
            empls_list.append(SalariedEmployee(name, int(line[1]), [], week_salary))
    return empls_list


def read_hourly_employees_from_file(path):
    empls_list = []

    with open(path) as g:
        for line in g:
            line = line.strip()
            line = line.split(";")
            empls_list.append(HourlyEmployee(line[0], int(line[1]), [], int(line[2]), int(line[3])))
        return empls_list


if __name__ == '__main__':
    #print_lines_in_file("tasks.txt")
    #lines_list = read_lines_in_file("tasks.txt")
    #print(lines_list)
    tasks = read_tasks_from_file("tasks.txt")
    salaried_empls = read_salaried_employees_from_file("salariedemployees.txt")
    hourly_empls = read_hourly_employees_from_file("hourlyemployees.txt")

    empls = salaried_empls + hourly_empls
    company = Company("QuickGeo", empls, tasks)

    company.dist_task(2)
    company.work_all()
    company.print_emp()
    print(company.monty_salary)