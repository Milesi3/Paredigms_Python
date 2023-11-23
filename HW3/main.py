"""
В данном коде использованы следующие парадигмы программирования:
1. Объектно-ориентированное программирование (ООП): Класс TicTacToe
инкапсулирует логику игры, предоставляя методы для взаимодействия
с игровым полем, совершения ходов, проверки наличия победителя и
другие операции.
2. Императивное программирование: В основе кода лежит императивная парадигма,
где задаются последовательности инструкций для выполнения определенных
действий. Например, цикл while в функции main управляет основным потоком
выполнения игры.
3. Структурное программирование: Код разделен на логические блоки
(модули и классы), что улучшает читаемость и обслуживаемость.
4. Процедурное программирование: Функция main в game.py является
процедурой, которая организует ход игры, вызывая методы класса TicTacToe.
5. Интерактивное программирование: Взаимодействие с пользователем
реализовано через стандартный ввод/вывод, позволяя игрокам совершать ходы.
"""

from game import main

if __name__ == "__main__":
    main()