
    
    

select
    ID as unique_field,
    count(*) as n_records

from "dbt_test"."india_data"."marriage_data_analysis"
where ID is not null
group by ID
having count(*) > 1


