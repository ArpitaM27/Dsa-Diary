Select year,price,product_name
from Sales s Left Join Product p
on s.product_id=p.product_id
