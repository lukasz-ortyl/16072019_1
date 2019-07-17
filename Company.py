class Task:
    def __init__(self, t_name, point_no):
        self.t_name = t_name
        self.point_no = point_no
        self.is_done = False

    def execute(self):
        self.is_done = True

class Employee:
    def __init__(self, name, age, task_list):
        self.name = name
        self.age = age
        self.task_list = task_list

    def describe(self):
        return "My mane is {} and I am {}".format(self.name, self.age)

    def work(self):
        not_done_task = [task for task in self.task_list if not task.is_done]
        if not_done_task:
            not_done_task[0].execute()

    def add_task(self, task):
        self.task_list.append(task)

    @property
    def points_sum(self):
        return sum([task.point_no for task in self.task_list if task.is_done])

    @property
    def monty_salary(self):
        raise NotImplementedError()
    # jesli program nie znajdzie monty_salary w klasie podrzednej to odwoła sie wyzej a nie chcemy

class SalariedEmployee(Employee):
    def __init__(self, name, age, task_list, weekly_salary):
        super().__init__(name, age, task_list)
        self.weekly_salary = weekly_salary

    def describe(self):
        return "{} I earn {} weekly".format(super().describe(), self.weekly_salary)

    @property
    def monty_salary(self):
        return self.monty_salary * 4

class HourlyEmployee(Employee):
    def __init__(self, name, age, task_list, week_work_hrs, hour_salary):
        super().__init__(name, age, task_list)
        self.week_work_hrs = week_work_hrs
        self.hour_salary = hour_salary

    def describe(self):
        return "{} I work {} hours weekly".format(super().describe(), self.week_work_hrs)

    @property
    def monty_salary(self):
        return self.hour_salary*self.week_work_hrs * 4

class Company:
    def __init__(self, name, emp_list, task_list):
        self.name = name
        self.emp_list = emp_list
        self.task_list = task_list

    def add_employees(self, employee):
        self.emp_list.append(employee)

    def add_task(self, task):
        self.task_list.append(task)

    def dist_task(self, task_to_distribute):

        while task_to_distribute > 0:
            self.emp_list[task_to_distribute % len(self.emp_list)].add_task(self.task_list.pop())
            task_to_distribute -= 1


if __name__ == '__main__':
    zad_1 = Task("Write Art", 140)
    zad_2 = Task("Write Art", 140)
    zad_3 = Task("write Art", 140)
    zad_4 = Task("MSc review", 3)
    zad_5 = Task("TBZ classes", 2)
    zad_6 = Task("PP classes", 5)
    emp_1_list = []
    emp_2_list = []
    emp_3_list = []
    emp_1 = SalariedEmployee("Łukasz", 42, emp_1_list, 500)
    emp_2 = HourlyEmployee("Tomasz", 39, emp_2_list, 40, 13.50)
    #emp_3 = Employee("Przemo", 34, emp_3_list)
    my_emp_list = []
    my_task_list = []
    my_company = Company("AGH", my_emp_list, my_task_list)
    my_company.add_employees(emp_1)
    my_company.add_employees(emp_2)
    my_company.add_task(zad_1)
    my_company.add_task(zad_2)
    my_company.add_task(zad_3)
    my_company.add_task(zad_4)
    emp_1.work()
    print(emp_1.points_sum)
    my_company.dist_task(4)
    for i in range(0, len(my_company.emp_list)):
        print(my_company.emp_list[i].name)
        for j in range(0, len(my_company.emp_list[i].task_list)):
            print(my_company.emp_list[i].task_list[j].t_name)