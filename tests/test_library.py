import unittest
import os
import json
from typing import List, Dict, Union

from models.book import Book
from models.library import Library


class TestBook(unittest.TestCase):
    """Тесты для модели Book."""

    def setUp(self) -> None:
        """Инициализация перед каждым тестом."""
        self.book = Book(1, "1984", "Джордж Оруэлл", 1949)

    def test_to_dict(self) -> None:
        """Тест для метода to_dict()."""
        expected: Dict[str, Union[int, str]] = {
            "id": 1,
            "title": "1984",
            "author": "Джордж Оруэлл",
            "year": 1949,
            "status": "в наличии"
        }
        self.assertEqual(self.book.to_dict(), expected)

    def test_from_dict(self) -> None:
        """Тест для метода from_dict()."""
        data: Dict[str, Union[int, str]] = {
            "id": 1,
            "title": "1984",
            "author": "Джордж Оруэлл",
            "year": 1949,
            "status": "в наличии"
        }
        book: Book = Book.from_dict(data)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "Джордж Оруэлл")
        self.assertEqual(book.year, 1949)
        self.assertEqual(book.status, "в наличии")


class TestLibrary(unittest.TestCase):
    """Тесты для модели Library."""

    def setUp(self) -> None:
        """Инициализация перед каждым тестом."""
        self.test_file = "test_library.json"
        self.library = Library(self.test_file)

    def tearDown(self) -> None:
        """Удаление тестового файла после каждого теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self) -> None:
        """Тест для метода add_book()."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "О дивный новый мир")

    def test_remove_book(self) -> None:
        """Тест для метода remove_book()."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_find_books_by_title(self) -> None:
        """Тест для метода find_books() с параметром поиска по названию."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        books: List[Book] = self.library.find_books("дивный", "название")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "О дивный новый мир")

    def test_find_books_by_author(self) -> None:
        """Тест для метода find_books() с параметром поиска по автору."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        books: List[Book] = self.library.find_books("Хаксли", "автор")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].author, "Олдос Хаксли")

    def test_find_books_by_year(self) -> None:
        """Тест для метода find_books() с параметром поиска по году."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        books: List[Book] = self.library.find_books("1932", "год")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].year, 1932)

    def test_update_status(self) -> None:
        """Тест для метода update_status()."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.library.update_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_save_books(self) -> None:
        """Тест для метода save_books()."""
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.library.save_books()
        with open(self.test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "О дивный новый мир")

    def test_load_books(self) -> None:
        """Тест для метода load_books()."""
        book_data: List[Dict[str, Union[int, str]]] = [
            {
                "id": 1,
                "title": "О дивный новый мир",
                "author": "Олдос Хаксли",
                "year": 1932,
                "status": "в наличии"
            }
        ]
        with open(self.test_file, "w", encoding="utf-8") as file:
            json.dump(book_data, file, ensure_ascii=False, indent=4)

        self.library.load_books()
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "О дивный новый мир")


if __name__ == "__main__":
    unittest.main()
