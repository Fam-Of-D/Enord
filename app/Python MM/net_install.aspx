yum install rh-dotnet20 -y
scl enable rh-dotnet20 bash

<%-- Open a new command prompt and run the following commands:--%>

dotnet new console -o myApp
cd myApp


<%--  -o parameter creates a directory named myApp where your app is stored

<%-- MAIN !!!!!!@#$$ --%>
using System;



namespace myApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}