program SmartCalculator;

uses Math, sysutils;

// Функция для безопасного ввода чисел
function ReadDouble(prompt: string): real;
var
    s: string;
    val: real;
    code: integer;
begin
    while true do
    begin
        write(prompt);
        readln(s);
        val := StrToFloatDef(s, -999999.99); // Пытаемся конвертировать
        if val <> -999999.99 then
            exit(val)
        else
            writeln('Ошибка: Введите корректное число!');
    end;
end;

var 
    num1, num2, result: real;
    op: string;
    isValid: boolean;

begin 
    writeln('==========================================');
    writeln('       PASCAL SMART CALCULATOR 3.0       ');
    writeln('==========================================');

    while true do 
    begin 
        write('> Операция (+, -, *, /, pow, sin, cos, exit): ');
        readln(op);
        op := lowercase(trim(op));

        if op = 'exit' then break;

        isValid := true;

        // Блок функций с одним числом
        if (op = 'sin') or (op = 'cos') or (op = 'ln') or (op = '%') then
        begin
            num1 := ReadDouble('Введите число: ');
            if op = 'sin' then result := sin(num1)
            else if op = 'cos' then result := cos(num1)
            else if op = 'ln' then 
            begin
                if num1 > 0 then result := ln(num1) 
                else begin writeln('Ошибка: x > 0'); isValid := false; end;
            end
            else if op = '%' then result := num1 / 100;
        end

        // Блок функций с двумя числами
        else if (op = '+') or (op = '-') or (op = '*') or (op = '/') or (op = 'pow') then
        begin
            num1 := ReadDouble('Первое число: ');
            num2 := ReadDouble('Второе число: ');

            if op = '+' then result := num1 + num2
            else if op = '-' then result := num1 - num2
            else if op = '*' then result := num1 * num2
            else if op = '/' then 
            begin
                if num2 <> 0 then result := num1 / num2
                else begin writeln('Ошибка: Деление на ноль!'); isValid := false; end;
            end
            else if op = 'pow' then result := power(num1, num2);
        end
        else 
        begin
            writeln('Ошибка: Неизвестная операция!');
            isValid := false;
        end;

        if isValid then
        begin
            writeln('------------------------------------------');
            writeln('РЕЗУЛЬТАТ: ', result:0:4);
            writeln('------------------------------------------');
        end;
    end;

    writeln('До встречи!');
end.
