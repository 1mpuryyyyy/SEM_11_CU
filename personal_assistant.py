import pandas as pd
import datetime
import random


class ManageNotes:
    def __init__(self):
        self.notes = pd.DataFrame(columns=["id", "title", "content", "timestamp"])
        self.tasks = pd.DataFrame(columns=["id", "title", "description", "done", "priority", "due_date"])
        self.contacts = pd.DataFrame(columns=["id", "name", "phone", "email"])
        self.finance_records = pd.DataFrame(columns=["id", "amount", "category", "date", "description"])

    def manage_notes(self):
        while True:
            print("Управление заметками")
            print("1) Создание новой заметки")
            print("2) Просмотр списка заметок")
            print("3) Просмотр подробностей заметки")
            print("4) Редактирование заметки")
            print("5) Удаление заметки")
            print("6) Импорт заметок из CSV")
            print("7) Экспорт заметок в CSV")
            print("8) Назад")
            choice = input("Ваш выбор: ")

            if choice == "1":
                title = input("Заголовок заметки: ").strip()
                content = input("Содержимое заметки: ").strip()
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note_data = {
                    "id": random.randint(1, 1000000),
                    "title": title,
                    "content": content,
                    "timestamp": timestamp,
                }
                self.notes = pd.concat([self.notes, pd.DataFrame([note_data])], ignore_index=True)
                print("Заметка успешно добавлена!")
            elif choice == "2":
                if self.notes.empty:
                    print("Список заметок пуст.")
                else:
                    print(self.notes)
            elif choice == "3":
                title = input("Введите заголовок заметки для просмотра: ").strip()
                note = self.notes[self.notes["title"] == title]
                if not note.empty:
                    print(note)
                else:
                    print("Заметка не найдена.")
            elif choice == "4":
                title = input("Введите заголовок заметки для редактирования: ").strip()
                if not self.notes[self.notes["title"] == title].empty:
                    new_title = input("Новый заголовок заметки: ").strip()
                    new_content = input("Новое содержимое заметки: ").strip()
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.notes.loc[self.notes["title"] == title, ["title", "content", "timestamp"]] = [new_title, new_content, timestamp]
                    print("Заметка успешно обновлена!")
                else:
                    print("Заметка не найдена.")
            elif choice == "5":
                title = input("Введите заголовок заметки для удаления: ").strip()
                if not self.notes[self.notes["title"] == title].empty:
                    self.notes = self.notes[self.notes["title"] != title]
                    print("Заметка успешно удалена!")
                else:
                    print("Заметка не найдена.")
            elif choice == "6":
                file_path = input("Введите путь до файла CSV: ").strip()
                try:
                    imported_notes = pd.read_csv(file_path)
                    self.notes = pd.concat([self.notes, imported_notes], ignore_index=True)
                    print("Заметки успешно импортированы!")
                except Exception as e:
                    print(f"Ошибка при импорте: {e}")
            elif choice == "7":
                file_path = input("Введите путь для сохранения CSV: ").strip()
                try:
                    self.notes.to_csv(file_path, index=False)
                    print("Заметки успешно экспортированы!")
                except Exception as e:
                    print(f"Ошибка при экспорте: {e}")
            elif choice == "8":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def manage_tasks(self):
        while True:
            print("Управление задачами")
            print("1) Создание новой задачи")
            print("2) Просмотр списка задач")
            print("3) Отметка задачи как выполненной")
            print("4) Редактирование задачи")
            print("5) Удаление задачи")
            print("6) Импорт задач из CSV")
            print("7) Экспорт задач в CSV")
            print("8) Назад")
            choice = input("Ваш выбор: ")

            if choice == "1":
                title = input("Заголовок задачи: ").strip()
                description = input("Описание задачи: ").strip()
                priority = input("Приоритет задачи: ").strip()
                due_date = input("Дата выполнения задачи (ГГГГ-ММ-ДД): ").strip()
                task_data = {
                    "id": random.randint(1, 1000000),
                    "title": title,
                    "description": description,
                    "done": False,
                    "priority": priority,
                    "due_date": due_date,
                }
                self.tasks = pd.concat([self.tasks, pd.DataFrame([task_data])], ignore_index=True)
                print("Задача успешно добавлена!")
            elif choice == "2":
                if self.tasks.empty:
                    print("Список задач пуст.")
                else:
                    print(self.tasks)
            elif choice == "3":
                title = input("Введите заголовок задачи для отметки как выполненной: ").strip()
                if not self.tasks[self.tasks["title"] == title].empty:
                    self.tasks.loc[self.tasks["title"] == title, "done"] = True
                    print("Задача успешно отмечена как выполненная!")
                else:
                    print("Задача не найдена.")
            elif choice == "4":
                title = input("Введите заголовок задачи для редактирования: ").strip()
                if not self.tasks[self.tasks["title"] == title].empty:
                    new_title = input("Новый заголовок задачи: ").strip()
                    new_description = input("Новое описание задачи: ").strip()
                    new_priority = input("Новый приоритет задачи: ").strip()
                    new_due_date = input("Новая дата выполнения задачи (ГГГГ-ММ-ДД): ").strip()
                    self.tasks.loc[self.tasks["title"] == title, ["title", "description", "priority", "due_date"]] = [new_title, new_description, new_priority, new_due_date]
                    print("Задача успешно обновлена!")
                else:
                    print("Задача не найдена.")
            elif choice == "5":
                title = input("Введите заголовок задачи для удаления: ").strip()
                if not self.tasks[self.tasks["title"] == title].empty:
                    self.tasks = self.tasks[self.tasks["title"] != title]
                    print("Задача успешно удалена!")
                else:
                    print("Задача не найдена.")
            elif choice == "6":
                file_path = input("Введите путь до файла CSV: ").strip()
                try:
                    imported_tasks = pd.read_csv(file_path)
                    self.tasks = pd.concat([self.tasks, imported_tasks], ignore_index=True)
                    print("Задачи успешно импортированы!")
                except Exception as e:
                    print(f"Ошибка при импорте: {e}")
            elif choice == "7":
                file_path = input("Введите путь для сохранения CSV: ").strip()
                try:
                    self.tasks.to_csv(file_path, index=False)
                    print("Задачи успешно экспортированы!")
                except Exception as e:
                    print(f"Ошибка при экспорте: {e}")
            elif choice == "8":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def manage_contacts(self):
        while True:
            print("Управление контактами")
            print("1) Создание нового контакта")
            print("2) Поиск контакта")
            print("3) Редактирование контакта")
            print("4) Удаление контакта")
            print("5) Импорт контактов из CSV")
            print("6) Экспорт контактов в CSV")
            print("7) Назад")
            choice = input("Ваш выбор: ")

            if choice == "1":
                name = input("Имя контакта: ").strip()
                phone = input("Телефон контакта: ").strip()
                email = input("Email контакта: ").strip()
                contact_data = {
                    "id": random.randint(1, 1000000),
                    "name": name,
                    "phone": phone,
                    "email": email,
                }
                self.contacts = pd.concat([self.contacts, pd.DataFrame([contact_data])], ignore_index=True)
                print("Контакт успешно добавлен!")
            elif choice == "2":
                search_term = input("Введите имя или номер телефона для поиска: ").strip()
                results = self.contacts[
                    self.contacts["name"].str.contains(search_term, case=False, na=False) |
                    self.contacts["phone"].str.contains(search_term, case=False, na=False)
                ]
                if not results.empty:
                    print(results)
                else:
                    print("Контакт не найден.")
            elif choice == "3":
                name = input("Введите имя контакта для редактирования: ").strip()
                if not self.contacts[self.contacts["name"] == name].empty:
                    new_name = input("Новое имя: ").strip()
                    new_phone = input("Новый телефон: ").strip()
                    new_email = input("Новый Email: ").strip()
                    self.contacts.loc[self.contacts["name"] == name, ["name", "phone", "email"]] = [new_name, new_phone, new_email]
                    print("Контакт успешно обновлен!")
                else:
                    print("Контакт не найден.")
            elif choice == "4":
                name = input("Введите имя контакта для удаления: ").strip()
                if not self.contacts[self.contacts["name"] == name].empty:
                    self.contacts = self.contacts[self.contacts["name"] != name]
                    print("Контакт успешно удален!")
                else:
                    print("Контакт не найден.")
            elif choice == "5":
                file_path = input("Введите путь до файла CSV: ").strip()
                try:
                    imported_contacts = pd.read_csv(file_path)
                    self.contacts = pd.concat([self.contacts, imported_contacts], ignore_index=True)
                    print("Контакты успешно импортированы!")
                except Exception as e:
                    print(f"Ошибка при импорте: {e}")
            elif choice == "6":
                file_path = input("Введите путь для сохранения CSV: ").strip()
                try:
                    self.contacts.to_csv(file_path, index=False)
                    print("Контакты успешно экспортированы!")
                except Exception as e:
                    print(f"Ошибка при экспорте: {e}")
            elif choice == "7":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def manage_finance_records(self):
        while True:
            print("Управление финансовыми записями")
            print("1) Добавление новой записи")
            print("2) Просмотр всех записей")
            print("3) Поиск записей по категории")
            print("4) Удаление записи")
            print("5) Импорт записей из CSV")
            print("6) Экспорт записей в CSV")
            print("7) Назад")
            choice = input("Ваш выбор: ")

            if choice == "1":
                amount = float(input("Сумма: "))
                category = input("Категория: ").strip()
                date = input("Дата (ГГГГ-ММ-ДД): ").strip()
                description = input("Описание: ").strip()
                record_data = {
                    "id": random.randint(1, 1000000),
                    "amount": amount,
                    "category": category,
                    "date": date,
                    "description": description,
                }
                self.finance_records = pd.concat([self.finance_records, pd.DataFrame([record_data])], ignore_index=True)
                print("Финансовая запись успешно добавлена!")
            elif choice == "2":
                if self.finance_records.empty:
                    print("Финансовые записи отсутствуют.")
                else:
                    print(self.finance_records)
            elif choice == "3":
                category = input("Введите категорию для поиска: ").strip()
                results = self.finance_records[self.finance_records["category"] == category]
                if not results.empty:
                    print(results)
                else:
                    print("Записей по данной категории не найдено.")
            elif choice == "4":
                record_id = int(input("Введите ID записи для удаления: "))
                if not self.finance_records[self.finance_records["id"] == record_id].empty:
                    self.finance_records = self.finance_records[self.finance_records["id"] != record_id]
                    print("Запись успешно удалена!")
                else:
                    print("Запись не найдена.")
            elif choice == "5":
                file_path = input("Введите путь до файла CSV: ").strip()
                try:
                    imported_records = pd.read_csv(file_path)
                    self.finance_records = pd.concat([self.finance_records, imported_records], ignore_index=True)
                    print("Финансовые записи успешно импортированы!")
                except Exception as e:
                    print(f"Ошибка при импорте: {e}")
            elif choice == "6":
                file_path = input("Введите путь для сохранения CSV: ").strip()
                try:
                    self.finance_records.to_csv(file_path, index=False)
                    print("Финансовые записи успешно экспортированы!")
                except Exception as e:
                    print(f"Ошибка при экспорте: {e}")
            elif choice == "7":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def calculator(num1, num2, operation):
        try:
            if operation == 'add':
                return num1 + num2
            elif operation == 'subtract':
                return num1 - num2
            elif operation == 'multiply':
                return num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    raise ValueError("Ошибка: Деление на ноль!")
                return num1 / num2
            else:
                raise ValueError("Ошибка: Неверная операция.")
        except Exception as e:
            return str(e)


def main():
    manager = ManageNotes()
    print("Добро пожаловать в Персональный помощник!")
    while True:
        print("Главное меню:")
        print("1) Управление заметками")
        print("2) Управление задачами")
        print("3) Управление контактами")
        print("4) Управление финансовыми записями")
        print("5) Калькулятор")
        print("6) Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            manager.manage_notes()
        elif choice == "2":
            manager.manage_tasks()
        elif choice == "3":
            manager.manage_contacts()
        elif choice == "4":
            manager.manage_finance_records()
        elif choice == "5":
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                operation = input("Выберите операцию (add, subtract, multiply, divide): ").strip()
                result = manager.calculator(num1, num2, operation)
                print(f"Результат: {result}")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
