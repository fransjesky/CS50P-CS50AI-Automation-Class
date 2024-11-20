'''
task:
create a simple program with these variables:
name, job, salary, and netWorth

output:
"My name is Mike, and I'm a Programmer. My monthly net income is $12,200"
'''

def main():
  name: str = input("What's your name? ")
  job: str = input("What's your job? ")
  salary: int = int(input("How much is your monthly income? "))
  netWorth: int = salary - (salary * 5 / 100)

  print(f"My name is {name.title()}, and I'm a {job.title()}. My monthly net income is ${netWorth:,}.")


main()
