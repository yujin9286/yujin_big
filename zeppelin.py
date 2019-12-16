%spark
val dataframe = spark.read.option("header","true").option("sep",",").csv("hdfs:///user/maria_dev/test/all_total_bookcrawling.csv")
dataframe.printSchema()        
dataframe.show()
dataframe.createOrReplaceTempView("Books")

%sql
select AVG(rating) from Books where rating > 1

%sql
select AVG(price) from Books

%sql
select title,AVG(rating) from Books GROUP BY title ORDER BY AVG(rating) DESC

%sql
select title,AVG(price) from Books GROUP BY title ORDER BY AVG(price) DESC 

%sql
select count(title) from Books where rating >=10 