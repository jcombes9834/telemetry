T = readtable('dbf test flight one.csv');
t1 = T.Var1; %first column is the memory address each val was stored in. For the first test flight values were read every 300 milliseconds.
v1 = T.Var2; %voltage readings from first test flight
t2 = T.Var3; %memory address vector for second test flight
v2 = T.Var4; %voltage readings from second test flight.

plot(t1, v1);
figure()
plot(t2, v2);