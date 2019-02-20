package mypackage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Hello
{
	// 从控制台输入
	public static void test1()
	{
		try
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("please input the greeting: ");
            String greeting = br.readLine();
            System.out.println(greeting);
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
	}
	
	// 从文件输入
		public static void test2()
		{
			try
	        {
	            BufferedReader br = new BufferedReader(new FileReader("e:/foo.in"));	            
	            String greeting = br.readLine();
	            System.out.println(greeting);
	        }
	        catch(IOException e)
	        {
	            e.printStackTrace();
	        }
		}
	
    public static void main(String args[])
    {
        test1();
        test2();
    }
}
