
declare @date_time datetime
declare @date_time_min datetime
declare @user_id int
declare @site_id int

declare sess_cur cursor local
for
select [user_id], site_id, [date_time]
from clickstream
order by [user_id], site_id, [date_time]

open sess_cur

fetch from sess_cur into @user_id, @site_id, @date_time
while @@FETCH_STATUS = 0
begin

if exists(select site_id 
			from sess
			where @user_id = [user_id] 
				and @site_id = site_id 
				and @date_time_min = session_start_time
				and datediff(minute, session_end_time, @date_time)<=30)
BEGIN
    --Обновляем конец сессии, если между смежными кликами не прошло 30 минут

	update ss
		set ss.session_end_time = @date_time 
	from sess ss
	where ss.[user_id] = @user_id
		and ss.site_id = @site_id
		and ss.session_start_time = @date_time_min
END
else 
BEGIN
    --Создаем новую сессию
    select @date_time_min = @date_time
	insert into sess ([user_id], site_id, session_start_time, session_end_time)
	select @user_id, @site_id, @date_time_min, @date_time
END		 


fetch next from sess_cur into @user_id, @site_id, @date_time
end

close sess_cur
deallocate sess_cur



























