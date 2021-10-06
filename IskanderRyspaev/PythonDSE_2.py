F = {
    1: 0,
    2: 1,
}

def function_fib(n):
    global F 
    if n in F:
        return F[n]
    result = function_fib(n - 1) + function_fib(n - 2)
    F[n] = result
    return result

print(function_fib(500))

class Task:
    def __init__(self, name):
        self.name = name
        self.action = lambda: print("Do nothing")
        # self.dependencies = []
 
    def set_action(self, func):
        self.action = func
 
    def run(self):
        print(self.name)
        self.action()
 
    # def depend_on(self, task):
    #     self.dependencies.append(task)
 
class Taskgraph:
    def __init__(self):
        self.tasks = []
 
    def append_task(self, task):
        self.tasks.append(task)
 
    def show_all_tasks(self):
        for t in self.tasks:
            print(t.name)
 
    def run(self):
        for t in self.tasks:
            t.run()
 
def func():
    print("Hello. I am task.")
 
task1 = Task('1')
task1.set_action(func)
 
task2 = Task('2')
task2.set_action(func)
 
taskgraph = Taskgraph()
taskgraph.append_task(task1)
taskgraph.append_task(task2)
taskgraph.run()

#git status
#git diff
#git add
#git commit -m "Add task order and threads"
#git push origin master:threading