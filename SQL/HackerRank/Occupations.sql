-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

select
Doctor,
Professor,
Singer,
Actor
 from (
select
    NameOrder,
    max(case Occupation when 'Doctor' then Name end) as Doctor,
    max(case Occupation when 'Professor' then Name end) as Professor,
    max(case Occupation when 'Singer' then Name end) as Singer,
    max(case Occupation when 'Actor' then Name end) as Actor
from (
        select
            Occupation,
            Name,
            row_number() over(partition by Occupation order by Name ASC) as NameOrder
        from Occupations
     ) as NameLists
group by NameOrder
) as Names



-- Selects the names of people with four different occupations (Doctor, Professor, Singer, and Actor) from a table called "Occupations". The table has two columns, "Name" and "Occupation", which contain the names of people and their occupations, respectively.
--
-- The query uses a series of nested SQL statements to accomplish this. Here is a breakdown of each part of the query:
--
--     The outermost SELECT statement lists the four occupations as columns that will be returned in the result set: Doctor, Professor, Singer, and Actor.
--     The FROM clause contains a subquery that selects the names of people with each occupation and arranges them into columns based on the order of their names. This is done using the ROW_NUMBER() function, which assigns a unique number to each row within a partition of the data (in this case, the partition is by occupation). This number is used to order the names within each occupation group.
--     The subquery in the FROM clause uses the MAX() function with a CASE statement to pivot the rows of data into columns. This creates a result set where each row represents a unique name order and the columns contain the names of people with each occupation. The MAX() function is used to select only the highest ranked name within each occupation group, which is determined by the NameOrder value.
--     The outermost query groups the results by the NameOrder column, which effectively removes the duplicate rows that were created by the inner subquery. The resulting rows contain the names of people with each occupation in the correct order.
