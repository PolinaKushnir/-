if __name__ == "__main__":
    # Write your solution here
    class SocialNetwork:
        """
        Attributes // Атрибуты:
            name (str): Наименование социальной сети
            foundation_year (int): Год основания социальной сети
        Methods // Методы:
            __init__: Конструктор
            __str__: Строковое представление
            __repr__: Официальное строковое представление
        """

        def __init__(self, name: str, foundation_year: int):
            self.name = name
            self.foundation_year = foundation_year

        def __str__(self) -> str:
            return f"{self.name}, основана в {self.foundation_year} году"

        def __repr__(self) -> str:
            return f"SocialNetwork(name={self.name}, foundation_year={self.foundation_year})"

    class VK(SocialNetwork):
        """
        Дочерний класс, представляющий собой социальную сеть Вконтакте (VK).
        Additional Attributes // Дополнительные атрибуты:
            users_count (int): Количество пользователей социальной сети
        Additional Methods // Дополнительные методы:
            send_message: Отправить сообщение
            __str__: Строковое представление социальной сети VK
            __repr__: Официальное строковое представление социальной сети VK
        """

        def __int__(self, name: str, foundation_year: int, users_count: int):
            super().__int__(name, foundation_year)
            self.users_count = users_count

        def send_message(self, recipient: str, text: str) -> None:
            """
            Arguments // Аргументы:
                recipient (str): Имя получателя сообщения
                text (str): Текст сообщений
            """
            # Реализация метода отправки сообщения
            pass

        def __str__(self) -> str:
            return f"{super().__str__()}, {self.users_count} пользователей"

        def __repr__(self) -> str:
            return f"VK(name={self.name}, foundation_year={self.foundation_year}, users_count={self.users_count})"

    class Facebook(SocialNetwork):
        """
        Дочерний класс, представляющий собой социальную сеть Facebook.
        Additional Attributes // Дополнительные атрибуты:
            active_users (int): Количество активных пользователей социальной сети
        Additional Methods // Дополнительные методы:
            create_group: Создать сообщество (группу)
            __str__: Строковое представление социальной сети Facebook
            __repr__: Официальное строковое представление социальной сети Facebook
        """

        def __init__(self, name: str, foundation_year: int, active_users: int):
            super().__init__(name, foundation_year)
            self.active_users = active_users

        def create_group(self, group_name: str) -> None:
            """
            Arguments // Аргументы:
                group_name (str): Наименование нового сообщества (группы)
            """
            # Реализация метода создания сообщества
            pass

        def __str__(self) -> str:
            return f"{super().__str__()}, {self.active_users} активных пользователей"

        def __repr__(self) -> str:
            return f"Facebook(name={self.name}, foundation_year={self.foundation_year}, " \
                   f"active_users={self.active_users})"