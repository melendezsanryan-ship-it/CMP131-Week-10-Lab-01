def main():
  employees = get_employees()
  total_days = get_total_days(employees)
  avg_days = calculate_average(employees, total_days)

  print("Total days absent:", total_days)
  print("Average days absent:", round(avg_days, 2))


def get_employees():
  count = int(input("Enter 1 or more employees: "))
  while count < 1:
    count = int(input("Enter 1 or more employees: "))
  return count


def get_total_days(employees):
  total = 0

  for i in range(employees):
    days = int(input("Days missed for employee " + str(i + 1) + ": "))
    while days < 0:
      days = int(input("Days cannot be negative. Try again: "))
    total += days

  return total


def calculate_average(employees, total_days):
  return float(total_days / employees)


main()

