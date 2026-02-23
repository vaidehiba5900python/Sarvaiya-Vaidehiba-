print("Overtime Calculator")
workers = int(input("Enter number of workers: "))
i = 0
total_payment = 0
while i < workers:
hours = int(input("Enter working hours: "))
rate = int(input("Enter rate per hour: "))
if hours > 40:
overtime = (hours - 40) * rate * 1.5
else:
overtime = 0
salary = (40 * rate) + overtime
total_payment = total_payment + salary
print("Salary:", salary
i = i + 1
print("Total Payment:", total_payment)
if total_payment > 100000:
print("High expense")
else:
print("Normal expense")
