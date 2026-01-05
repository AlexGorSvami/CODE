program SimpleCalculator;

var 
	num1, num2, result: real;
	operation: char;

begin 
	writeln('--- SimpleCalculator ---');

	// Enter first number
	write('Enter first number: ');
	readln(num1);

	// Choice of operation 
	write('Enter operation (+, -, *, /): ');
	readln(operation);

	//Enter second number 
	write('Enter second number: ');
	readln(num2);

	//Computational logic
	case operation of 
	 '+': result := num1 + num2;
	 '-': result := num1 - num2;
	 '*': result := num1 * num2;
	 '/':
		if num2 <> 0 then 
		  result := num1 / num2 
		else
		begin 
		  writeln('Error: you cant divide by zero');
		  exit;
		end;
	else
	 begin 
	  writeln('Error: unknown operation');
	  exit;
	 end;
    end;

	// Print result 
	writeln('Result: ', result:0:2); // 0:2 means 2 decimal places

	readln; //To prevent the console window from closing immediately
end. 
   

