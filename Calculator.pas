program SimpleCalculator;

uses Math; // connect math module

var 
	num1, num2, result: real;
	operation: string;
    continueCalculations: boolean = true;

begin 
	writeln('--- SimpleCalculator 2.0 ---');
    writeln('Availible operations: +, -, *, /, power, sin, cos, ln, log10, %');
    writeln('Type "exit" to close the calculator.');

    while continueCalculations do 
    begin 
        // enter operation 
        write ('> Enter operation +,-,*,power,sin,cos,ln,log10,% or enter exit');
        readln(operation);

        operation := lowercase(operation);

        if operation = 'exit' then 
        begin 
            continueCalculations := false;
            break;
        end;

        if (operation = 'sin') or (operation = 'cos') or (operation = 'ln') or (operation = 'log10') or (operation = '%') then
        begin 
            write('Enter number: ');
            readln(num1);

            case operation of 
                'sin': result := sin(num1);
                'cos': result := cos(num1);
                'ln':
                    if num1 > 0 then 
                        result := ln(num1)
                    else
                    begin 
                        writeln('Error: Ln must be of a positive number.');
                        continue;
                    end;
                'log10': // Log10(x) = Ln(x) / Ln(10)
                    if num1 > 0 then 
                        result := ln(num1) / ln(10)
                    else 
                    begin 
                        writeln('Error: Log10 must be of a positive number');
                        continue;
                    end;
                '%': result := num1 / 100;
            end;
        end

        // Handling an operation with 2 operand
        else if (operation = '+') or (operation = '-') or (operation = '*') or (operation = '/') or (operation = 'power') then
        begin 
            write('Enter first number: ');
            readln(num1);
            write('Enter second number: ');
            readln(num2);

            case operation of 
                '+': result := num1 + num2;
                '-': result := num1 - num2;
                '/':
                    if num1 <> 0 then
                        result := num1 / num2 
                    else
                    begin 
                        writeln('Error: Cannont divide by zero');
                        continue;
                    end;
                'power': result := power(num1, num2);
            end;
        end

        else
        begin 
            writeln('Error: Unknown operation. Try again');
            continue;
        end; 

        // Output of the result 
        writeln('Resullt:', result:0:4); // 4 char after , 
        writeln;
    end;

    writeln('Calculator closed');
end.


