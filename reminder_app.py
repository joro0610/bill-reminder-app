# Приложение за напомняне за плащания

class Reminder:
    def __init__(self, name, amount, due_date, periodicity):
        self.name = name
        self.amount = amount
        self.due_date = due_date
        self.periodicity = periodicity

    def __str__(self):
        return f'{self.name}: {self.amount}, due on {self.due_date}, {self.periodicity}.'

class ReminderApp:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, name, amount, due_date, periodicity):
        # Логическа грешка: Променливата amount се добавя като стринг, а не като число.
        # Това може да доведе до проблеми при изчисления или форматиране в бъдеще.
        new_reminder = Reminder(name, str(amount), due_date, periodicity)
        self.reminders.append(new_reminder)
        return "Reminder added successfully!"

    def show_reminders(self):
        if not self.reminders:
            return "No reminders set."
        return "\n".join(str(reminder) for reminder in self.reminders)

# Пример за използване на приложението
app = ReminderApp()
print(app.add_reminder("Electric Bill", 50.00, "2023-12-01", "monthly"))  # Въвеждане на числена стойност за amount
print(app.add_reminder("Water Bill", 30.00, "2023-12-05", "monthly"))
print(app.show_reminders())
ater Bill", "30.00", "2023-12-05", "monthly"))
print(app.show_reminders())

