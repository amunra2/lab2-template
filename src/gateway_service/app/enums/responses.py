from enum import Enum

from schemas.response import ErrorResponse, ValidationErrorResponse


class RespEnum(Enum):
    GetAllLibraries = {
        "description": "Все библиотеки в городе",
    }
    GetAllBooksInLibrary = {
        "description": "Все кники в библиотеке по uid",
    }
    GetUserRentedBooks = {
        "description": "Все взятые пользователем книги",
    }
    GetUserRating = {
        "description": "Рейтинг пользователя",
    }
    InvalidData = {
        "model": ValidationErrorResponse,
        "description": "Ошибка валидации данных",
    }
