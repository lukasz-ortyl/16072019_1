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

    def add_task(self,task):
        self.task_list.append(task)

    @property
    def points_sum(self):
        return sum([task.point_no for task in self.task_list if task.is_done])

    @property
    def monty_salary(self):
        raise NotImplementedError()
    # jesli program nie znajdzie monty_salary w klasie podrzednej to odwoła sie wyzej a nie chcemy

class SalariedEmployee(Employee)
    def __init__(self, name, age, task_list, weekly_salary):
        super().__init__(name, age, task_list)
        self.weekly_salary = weekly_salary

class HourlyEmployee(Employee)
    def __init__(self, name, age, task_list, week_work_hrs, hour_salary):
        super().__init__(name, age, task_list)
        self.week_work_hrs = week_work_hrs
        self.hour_salary = hour_salary



if __name__ == '__main__':
    zad_1 = Task("Write Art", 140)
    zad_2 = Task("MSc review", 3)
    zad_3 = Task("TBZ classes", 2)
    emp_1_list = [zad_1, zad_3]
    emp_2_list = [zad_1, zad_2]
    emp_1 = Employee("Łukasz", 42, emp_1_list)
    emp_2 = Employee("Tomasz", 39, emp_2_list)

    emp_1.work()
    print(emp_1.points_sum)