class Person
{
private int age;
private String name;
Person(String n,int a )
{name=n;
age=a;}
void displayPersonDetails()
{System.out.println("\nName: "+name);
System.out.println("\nAge: "+age);}}
class Employee extends Person
{int emp_no;float salary;
Employee(int e_no,float e_salary,int a,String nm)
{super(nm,a);emp_no=e_no;salary=e_salary;}
void displayEmployeeDetails()
{displayPersonDetails();
System.out.println("\nEmployee no: "+emp_no);
System.out.println("\nEmployee Salary: "+salary);}}
class Inheritance
{public static void main(String args[])
{Employee e=new Employee(101,15000,26,"Mr.Adam");
e.displayEmployeeDetails();}}
