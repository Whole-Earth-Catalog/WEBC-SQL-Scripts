# function to remove punctuation and capital letters in titles
drop function if exists clean_title;
delimiter //
create function clean_title(title varchar(6000))
returns varchar(6000)
deterministic
begin
	declare new_title varchar(6000);
	set new_title = lower(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(
    replace(replace(replace(replace(replace(replace(replace(replace(
    replace(replace(replace(replace(replace(replace(replace(replace(
    replace(replace(title, '|', ''), '=', '')
    , '+', ''), '\_', ''), '-', ''), '}' ,''), '{', ''), '*', ''), '^', ''), '>' ,'')
    , '<', ''), '\"', ''), '\'', ''), '\\', ''), '\%', ''), '$', ''), '#', ''), '@', '')
    , '!', ''), ')', ''), '(', ''), ']', ''),'[', ''), '/', ''), ';', ''), ':', ''), '?', ''), ',', ''), '.', ''));
    return new_title;
end//
delimiter ;
