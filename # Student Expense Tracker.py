# Student Expense Tracker 📊

def show_menu():
    print("\n📑 Expense Categories:")
    print("1️⃣ Food")
    print("2️⃣ Transport")
    print("3️⃣ Data")
    print("4️⃣ Stationery")
    print("5️⃣ Other")
    print("0️⃣ Exit and Show Total")

def main():
    expenses = []
    total = 0

    print("🎓 Welcome to Student Expense Tracker!")

    while True:
        show_menu()
        choice = input("📌 Enter the number for the expense category (0 to finish): ")

        if choice == "0":
            break

        amount = float(input("💸 Enter amount for this expense: R"))
        expenses.append(amount)
        total += amount
        print(f"✅ Added R{amount:.2f} to your expenses.")

    print("\n📝 Expense Summary:")
    for i, amount in enumerate(expenses, start=1):
        print(f"{i}. R{amount:.2f}")

    print(f"\n💰 Total Monthly Expenses: R{total:.2f}")
    print("📊 Thank you for using the Student Expense Tracker!")

if __name__ == "__main__":
    main()
