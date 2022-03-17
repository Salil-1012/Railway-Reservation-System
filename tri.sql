create or replace trigger pri_key
before insert on cust_detail
for each row
declare
ulast number;
unew number;
clast number;
cnew number;
begin
select nvl(max(cid),0) into clast from cust_detail;
cnew:=clast+1;
:new.cid:=cnew;
end;
