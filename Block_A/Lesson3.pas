Program Double;

var i, n: integer;
begin 
    write('Enter the n number');
    readln(n);

    for i := 1 to n do 
      writeln('Double n ', i, 'equal', i * i);
end.

