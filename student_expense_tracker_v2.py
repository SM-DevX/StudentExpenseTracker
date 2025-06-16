# Student Expense Tracker V2 💾 (with file saving)

from datetime import datetime

def show_menu():
    print("\n📑 Expense Categories:")
    print("1️⃣ Food")
    print("2️⃣ Transport")
    print("3️⃣ Data")
    print("4️⃣ Stationery")
    print("5️⃣ Other")
    print("0️⃣ Exit and Show Total")

def log_to_file(category, amount):
    with open("expenses.txt", "a") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time_now} | {category} | R{amount:.2f}\n")

def get_category_name(choice):
    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Data",
        "4": "Stationery",
        "5": "Other"
    }
    return categories.get(choice, "Unknown")

def main():
    expenses = []
    total = 0

    print("🎓 Welcome to Student Expense Tracker V2!")

    while True:
        show_menu()
        choice = input("📌 Enter the number for the expense category (0 to finish): ")

        if choice == "0":
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("❌ Invalid choice. Please try again.")
            continue

        try:
            amount = float(input("💸 Enter amount for this expense: R"))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        category = get_category_name(choice)
        expenses.append((category, amount))
        total += amount
        log_to_file(category, amount)

        print(f"✅ Added R{amount:.2f} under {category}.")

    print("\n📝 Expense Summary:")
    for i, (category, amount) in enumerate(expenses, start=1):
        print(f"{i}. {category}: R{amount:.2f}")

    print(f"\n💰 Total Monthly Expenses: R{total:.2f}")
    print("📊 Your data has been saved to 'expenses.txt'")

if __name__ == "__main__":
    main()
