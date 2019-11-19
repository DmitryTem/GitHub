


select * 
from employees 
where last_name = 'Smith'



select dp.department_name, AVG(emp.salary)
from departments dp 
 join employees emp on emp.department_id = dp.department_id
group by dp.department_id, dp.department_name
having AVG(emp.salary) > 10000



select 
 emp.first_name, 
 emp.last_name
from
 employees emp  
 join departments dp on dp.department_id = emp.department_id 
 join locations lc on lc.location_id = dp.location_id
where lc.country_code = 'RU'

