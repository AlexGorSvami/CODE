program CheckInput;
var age: integer; hasTicket, isVip: boolean; temp1, temp2: string;
    
begin
    write('Enter your age ');
    readln(age);

    write('Do you have a ticket? Yes\no ');
    readln(temp1);
    if (temp1 = 'yes') or (temp1 = 'Yes') or (temp1 = 'YES') then 
        hasTicket := true
    else 
        hasTicket := false;

    write('Do you have Vip status? Yes\no ');
    readln(temp2);
    if (temp2 = 'yes') or (temp2 = 'Yes') or (temp2 = 'YES') then 
        isVip := true
    else 
        isVip := false;

    
    if ((age >= 18) and (hasTicket)) or (isVip) then
        writeln('Access')
    else
        writeln('Stop');
end.

