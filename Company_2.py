class Task:
    def __init__(self, name, point_no):
        self.name = name
        self.point_no = point_no
        self.exe = False

    def execute(self):
        self.exe = True


class Employee:
    def __init__(self, name, age, tasks_list):
        self.name = name
        self.age = age
        self.tasks_list = tasks_list

    def describe(self):
        return "My name {}, I am {} years old".format(self.name, self.age)

    def work(self):
        not_done_tasks = [task for task in self.tasks_list if not task.exe]
        if len(not_done_tasks) > 0:
            not_done_tasks[0].execute()

    def add_task(self, task):
        self.tasks_list.append(task)

    @property
    def point_sum(self):
        return sum([task.point_no for task in self.tasks_list if task.exe])

    @property
    def monty_salary(self):
        raise NotImplementedError()


class SalariedEmployee(Employee):
    def __init__(self, name, age, tasks_list, week_salary):
        super().__init__(name, age, tasks_list)
        self.week_salary = week_salary

    def describe(self):
        return "{} I earn {} weekly".format(super().describe(), self.week_salary)

    @property
    def monty_salary(self):
        return self.week_salary * 4


class HourlyEmployee(Employee):
    def __init__(self, name, age, tasks_list, week_hours, hour_salary):
        super().__init__(name, age, tasks_list)
        self.week_hours = week_hours
        self.hour_salary = hour_salary

    def describe(self):
        return "{} I work {} hrs weekly, for {} by hr ".format(super().describe(), self.week_hours, self.week_hours)

    @property
    def monty_salary(self):
        return self.week_hours * self.hour_salary * 4


class Company:
    def __init__(self, name, empls_list, tasks_list_c):
        self.name = name
        self.empls_list = empls_list
        self.tasks_list_c = tasks_list_c

    def add_empl(self, empl):
        self.empls_list.append(empl)

    def add_task_c(self, task):
        self.tasks_list_c.append(task)

    def dist_tasks(self, task_to_dist):
        if task_to_dist > len(self.tasks_list_c):
            raise ToMenyTasksToDistributeThenException()

        while len(self.tasks_list_c) > 0:
            indeks = len(self.tasks_list_c) % len()





if __name__ == '__main__':
    zad_1 = Task("skocz", 3)
    zad_2 = Task("płyn", 4)
    zad_3 = Task("nurkuj", 5)
    zad_1.execute()
    print(" pisz {}".format(zad_1.exe))
    #emp_1 = Employee("Łukasz", 42, [zad_1, zad_2])
    #emp_1.describe()
    print()
    empl_2 = HourlyEmployee("Tomasz", 37, [], 10, 13.5)
    empl_3 = SalariedEmployee("Przemo", 35, [], 1000)
    empl_2.describe()
    print(empl_2.describe())
    print(empl_2.name)
    my_company = Company("AGH", [empl_2, empl_3], [zad_1, zad_2, zad_3])



