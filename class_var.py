class Employee:
  count=0
  def __init__(self):
    Employee.count = Employee.count + 1
    return None


def main():
  emp1 = Employee()
  emp2 = Employee()
  print(Employee.count)
  print(emp1.count)
  print(emp2.count)


if __name__=="__main__":
  main()

##all print statements will be 2.
