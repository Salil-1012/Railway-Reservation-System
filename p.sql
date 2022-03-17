create or replace procedure book(trid cust_detail.tid%type)
is 
y number ;
cursor c1 is select cid,tid,Res_Status from cust_detail where tid=trid; 
c cust_detail.cid%type;
t cust_detail.tid%type;
r cust_detail.Res_Status%type;
begin
select count(tid) into y from cust_detail where tid=trid and Res_Status='y'; 
open c1; 
loop
fetch c1 into c,t,r;
exit when c1%notfound;
dbms_output.put_line('Number of seats book'||y);
if  r='y' then 
insert into res_detail(book_seat,cid,tid,ticket) values('y',c,t,1251);
elsif r='n' then
insert into waiting_list(book_seat,cid,tid,ticket) values('n',c,t,1251);
end if;
end loop;
close c1;
end book;
