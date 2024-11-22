'''
Create a simple program with these variables:
name, job, salary, and netWorth

output:
"My name is Mike, and I'm a Programmer. My monthly net income is $12,200"
'''

def main():
  name: str = input("What's your name? ")
  job: str = input("What's your job? ")
  salary: int = get_salary()
  net_worth: int = salary - (salary * 5 / 100)

  print(f"My name is {name.title()}, and I'm a {job.title()}. My monthly net income is ${net_worth:,.0f}.")


def get_salary() -> int:
  while True:
    try:
      return int(input("How much is your monthly income? "))
    except ValueError:
      pass


main()
