## SQL Server Database

### About SQL

SQL is a common language that we could use to extract structured data from a Database, if you are not familiar with SQL, you could try to learn it from [SQL tutorial](https://www.runoob.com/sql/sql-tutorial.html).


### About SQL Server

SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network. --from wikipedia

But if you are familiar with the open-source relational database: `MYSQL`, then for `SQL Server` then just regard it as another tool.


### Install SQL Server

You could try to get the latest version from [official website](https://www.microsoft.com/zh-cn/sql-server/sql-server-downloads) try to get version that you would like to install. 

If you are using Windows without a lisence, then you could try to download `Express Version` as this contain basic features but not big as developer version, installment is just like traditional way to install software in your computer, one more thing is that after download it into disk, try to install it with **Adaministrator** role, just right click `.exe` file with `Run as Adaministrator`, you could select the reason to install it like Accenture use case. The last thing is to wait it to be installed. I have to say that to install **SQL Server** is a time-consuming task, take your time to learn some basic syntax of SQL Server.

The main step should be just like below image for reference. 

![Select to install SQL Server client](https://github.com/lugq1990/machine-learning-beginner-jupyter-series/blob/master/other_materials/SQL_Server/picture/install.png)


![Install Java to select JRE](https://github.com/lugq1990/machine-learning-beginner-jupyter-series/blob/master/other_materials/SQL_Server/picture/java_install.png)


![Installing process](https://github.com/lugq1990/machine-learning-beginner-jupyter-series/blob/master/other_materials/SQL_Server/picture/install_process.png)


![Finishment of installment](https://github.com/lugq1990/machine-learning-beginner-jupyter-series/blob/master/other_materials/SQL_Server/picture/sucess.png)


### Install SQL Server Management Studio (SSMS)


There must be a way for us to hands-on with some code to dementrate that we could get a better understanding for some technologies, it's same for **SQL Server**. So we have already installed SQL Server client, the way to test is to install SSMS, you could download the latest version from [here](https://docs.microsoft.com/zh-cn/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15#download-ssms). SSMS provides tools to configure, monitor, and administer instances of SQL Server and databases. The installment step is just like traditional software.


### Uses of SSMS 


After we have already installed **SSMS**, the first thing is to connect with our client, as we have already install our client with default user, then it could automately search username and password for us, then just `connect`. 

![Connect to Server](https://github.com/lugq1990/machine-learning-beginner-jupyter-series/blob/master/other_materials/SQL_Server/picture/connect_to_server.png)

After connection is OK, then the first thing should `create a database` with right click **Databases**, then add your database name, then refresh the database type, you could see your database there, or we could use SQL to create our database.

![Create new database](https://github.com/lugq1990/machine-learning-beginner-jupyter-series/blob/master/other_materials/SQL_Server/picture/create_new_db.png)


In fact, I highly recommend you should be familiar with SQL as most of daily work will need SQL functionality.


```SQL
-- Basic SQL step for confirm we are there
-- create database
create database sales;

-- use database
use sales;

-- create table
create table users (id bigint primary key, names varchar(255));

-- query table
select * from users;

-- insert tahle with data
insert into users (id, names) values (1, 'lu');
insert into users values (2, 'new');

-- confirm our data.
select * from users;

-- drop table if we don't need it
--drop table if exists users;

```

If we want to delete a database with SQL query, you will face a error for: `database is already in use`, you could just use bellow SQL to force stop process of SQL server, then we could continue our deletation of database.

```SQL
use master 
go 

declare @dbname sysname 
set @dbname='sales' --change database name here.

declare @s nvarchar(1000) 
declare tb cursor local for 
select s='kill '+cast(spid as varchar) 
from master..sysprocesses 
where dbid=db_id(@dbname) 

open tb 
fetch next from tb into @s 
while @@fetch_status=0 
begin 
exec(@s) 
fetch next from tb into @s 
end 
close tb 
deallocate tb 
exec('drop database ['+@dbname+']')  
```


### Personal recommendation

If you are curious about **machine learning** and want some **hands-on** tutorial, you could try my git repo: [machine-learning-notebook-series](https://github.com/lugq1990/machine-learning-notebook-series).

If you are curious about how to create **Auto machine learning** models with only 3 lines of code, you could also get it from [auto-ml-cl](https://github.com/lugq1990/auto-ml-cl).


### Final words

Happy to join **Accenture** and hope you will enjoy the journey of discovering your strength and potential ability!