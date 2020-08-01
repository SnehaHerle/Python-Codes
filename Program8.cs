using System;
namespace ConsoleApplication3
{class Base
{public void show()
{Console.WriteLine("\nThis is base class show method.");
}}
class Derived:Base
{public void show1()
{Console.WriteLine("\nThis is derived class method.");}
}class Program{static void Main(string[] args)
{Derived D1=new Derived();
Console.WriteLine("\n*********Inheritance Application*********\n");
Console.WriteLine("\nInherited Show method called on derived class object.\n");
D1.show();D1.show1();Console.ReadLine();
}}}
