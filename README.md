# AI-final-project

# How to start project
```
1. mkdir .venv
2. python -m venv .venv
3. .venv\Scripts\activate
4. pip install -r requirements.txt
5. python __init__.py
```
----------------------------------------------------------------------------
Sudoku generator and solver with simple GUI created in Python using PyGame.

About the game
In the beginning the player chooses a level of difficulty (easy, normal or hard). Afterwards, the first script generates a random sudoku map according to the chosen level of difficulty and another script solves the sudoku for comparison with the player input after the player submits their answers. The player can then play sudoku with a simple GUI

The program contains 4 scripts .
1️ sudoku_generator - script that generates a 9X9 sudoku board according to the sudoku puzzle rules 
2️ sudoku_solver - script that solves the sudoku puzzle 
3️ choose_level - simple script for the level difficulty GUI
4 sudoku - script that define Sudoku class
    state, size, sub_column_size, sub_row_size, domains 
    Phương thức :
    update_domains(self) : cập nhật miền giá trị cho các ô, bằng cách kiểm tra những số trong khoảng 1 đến size có thể đặt vào ô trống, sau đó gán tập những số hợp lệ đó cho miền giá trị của ô
    is_consistent(self, number:int, row:int, column:int) -> bool : trả về kiểu boolean, cho liệu việc đặt số (number) vào vị trí [row,column] có phù hợp với quy tắc của Sudoku hay không. Bằng cách kiểm tra trong hàng, cột và ma trận con của vị trí
    number_of_conflicts(self, number:int, row:int, column:int) -> int : Trả về số lượng xung đột của giá trị number tại vị trí [row,column], tương tự kiểm tra trong hàng, cột và ma trận con của vị trí
    create_initial_solution(self) : Tạo ra một giải pháp ban đầu, bằng cách chọn các số ngẫu nhiên cho các vị trí trong bảng, có khả năng gây ra xung đột
    min_conflicts(self, var_rate:float=0.04, val_rate:float=0.02, max_steps:int=100000) -> bool : Trả về kiểu boolean, True nếu tìm ra lời giải cho bài toán và ngược lại. Bằng cách, lặp lại nhiều lần chọn một biến ngẫu nhiên trong xung đột và thay đổi giá trị của nó. Đối với biến được chọn, thuật toán sẽ tính toán số lượng xung đột mà mỗi giá trị có thể gây ra và chọn một trong các giá trị giúp giảm thiểu số lượng xung đột. Nếu có nhiều giá trị giảm thiểu số lượng xung đột, thuật toán sẽ chọn ngẫu nhiên một giá trị với xác suất được cho bởi val_rate, còn var_rate dùng để thoát khỏi trạng thái tối thiểu cục bộ. 
5 __init__ - the main script, the player runs this script to play the game
