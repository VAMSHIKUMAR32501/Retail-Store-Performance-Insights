SELECT Age, Gender, AVG(Total_Spent) AS Avg_Spending
FROM customer_data
GROUP BY Age, Gender;
