import sqlite3 as sql
con=sql.connect('database3.sqlite3')
con.execute('''drop table employee3''')
con.execute('''create table employee3(employee_id int,firstname varchar2(50),lastname varchar2(50),email varchar2(200),phone_number int,hiredate varchar2(15),job_id int,salary int,commision_pct int,manager_id int,department_id varchar2(10))''')
con.execute('''insert into employee3 values(489,'vamsi','lakkimsetti','saivamsi1927@gmail.com',8712124753,'14 Feb 2022',20,80000,5000,210,'cse')''')
con.execute('''insert into employee3 values(485,'yashwanth','kowthrapu','yashwanthkk@gmail.com',9856234562,'20 aug 2021',19,60000,3500,210,'cse')''')
con.commit()
query=con.execute('''select * from employee3''')
for i in query:
	print(i)