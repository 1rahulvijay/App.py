SELECT 
    l.*,
    CASE 
        WHEN r1.f_id IS NOT NULL THEN 'tm'
        ELSE NULL
    END AS new_column_1,
    CASE 
        WHEN r2.f_id IS NOT NULL THEN 'tm'
        ELSE NULL
    END AS new_column_2
FROM 
    table_left l
LEFT JOIN 
    table_right r1
ON 
    l.f_id = r1.f_id
LEFT JOIN 
    table_right r2
ON 
    l.f_id = r2.f_id;
