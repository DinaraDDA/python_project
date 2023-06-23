sports = ['Gerrard', 'Ronaldo', 'Bechkam', 'Messi', 'Owen']
print(f"Я бы хотел сыграть с {sports[0]}")
print(f"Я бы хотел сыграть с {sports[1]}")
print(f"Я бы хотел сыграть с {sports[-1]}")
guests = ['Laura', 'Gulnara', 'Zhanar']
print(f"Приглашаю тебя, {guests[0]}, на обед!")
print(f"Приглашаю тебя, {guests[1]}, на обед!")
print(f"Приглашаю тебя, {guests[2]}, на обед!")

guests = ['Laura', 'Gulnara', 'Zhanar']
print(f"Приглашаю тебя, {guests[0]}, на обед!")
print(f"Приглашаю тебя, {guests[1]}, на обед!")
print(f"Приглашаю тебя, {guests[2]}, на обед!")
print("Расширяем список гостей")

guests.insert(0, "Kamila")
guests.insert(3, "Elmira")
guests.append("Larisa")
print()
print("Обновленный список гостей:\n")
print(guests)
print()
print(f"Приглашаю тебя, {guests[0]}, на обед!")
print(f"Приглашаю тебя, {guests[1]}, на обед!")
print(f"Приглашаю тебя, {guests[2]}, на обед!")
print(f"Приглашаю тебя, {guests[3]}, на обед!")
print(f"Приглашаю тебя, {guests[-2]}, на обед!")
print(f"Приглашаю тебя, {guests[-1]}, на обед!")
