select max(c.company_code), max(c.founder), count(distinct e.lead_manager_code), count(distinct e.senior_manager_code),
count (distinct e.manager_code), count (distinct e.employee_code)
from company c, employee e
where c.company_code = e.company_code
group by e.lead_manager_code
order by max(c.company_code);
