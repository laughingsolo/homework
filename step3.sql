-- 3-1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）
select * from people 
where school is not 'GDUFS'
union
select * from people
where school is null;

-- 3-2.查找计算机系每次考试学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。-- 
select a.exam_name,avg(grade)
from exam a,student b
where dept_name='computer' and student_ID=ID;
group by exam_name;

-- 3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
select student.name,avg(exam.grade)
from exam,student
where sex='f' and student_ID=ID
group by student_ID
having avg(exam.grade)>=80;

-- 3-4.找出人数最少的院系以及其年度预算。
select department.dept_name,budget, count(*) AS counts
from department left join student on department.dept_name = student.dept_name
group by dept_name
order by counts limit 0,1;

-- 3-5.计算机系改名了，改成计算机科学系（comp. sci.）-- 
update department
set dept_name='comp. sci.'
where dept_name='computer';

-- 3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
select department.dept_name,count(*) AS counts
from department left join student on department.dept_name = student.dept_name
group by dept_name;
update department
set budget=budget+3*2000
where dept_name='biology';
update department
set budget=budget+8*2000
where dept_name='computer';
update department
set budget=budget+2*2000
where dept_name='math';
update department
set budget=budget+3*2000
where dept_name='new';
update department
set budget=budget+4*2000
where dept_name='physics';

-- 3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
select avg(budget) as avg_budget
from department;
insert into department values('21400.0000',NULL,'21400.0000');

-- 3-8. 删除计算机系中考试成绩平均分低于70的学生.
delete from student where dept_name='comp. sci.' and name in (
select a.name from(
select name from student,exam 
where student_ID=ID 
group by student_ID
having avg(exam.grade)<70)
a
)

-- 3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
update student 
set emotion_state='single'
where emotion_state='loving' and ID in (
select a.ID from(
select ID from student,exam 
where student_ID=ID 
group by student_ID
having avg(exam.grade)<75)
a
)
;

-- 对每个学生, 往exam表格中插入名为Avg_Exam的考试, 考试分数为之前学生参加过考试的平均分.
alter table exam add Avg_exam int;

