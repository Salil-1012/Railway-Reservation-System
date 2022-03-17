create or replace trigger waiting_list
after  delete on res_detail
for each row 
begin 
if deleting then
insert into waiting_list(book_seat,cid,tid)  values ('n',:old.cid,:old.tid);
end if ; 
end;

