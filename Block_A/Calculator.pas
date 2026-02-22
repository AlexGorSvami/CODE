program Calculator;

var
    a, b: integer;
    sum, diff, mult: integer;
    divis: real;

begin
    writeln('Enter first number');
    readln(a);

    writeln('Enter second number');
    readln(b);

    sum := a + b;
    diff := a - b;
    mult := a * b;
    divis := a / b;
    
    writeln('The sum is: ', sum);
    writeln('Difference: ', diff);
    writeln('Multiplication: ', mult);
    writeln('Division: ', divis:0:2);
end. 
