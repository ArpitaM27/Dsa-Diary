Select user_id,
CONCAT(Upper(Left(name,1)),Lower(Substring(name,2))) as name
from Users
order by user_id