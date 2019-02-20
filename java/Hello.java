import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.File;
import java.io.OutputStreamWriter;

public class Hello
{
    public static void test()
    {
        int b;
        b = 'A';
        System.out.write(b);
        System.out.write('\n');

    }

    public static void test5() throws Exception
    {
        InputStream f = new FileInputStream("/home/zq/hello");
        int size = f.available();
        System.out.println(size);

    }

    public static void test6() throws Exception
    {
        File f = new File("/home/zq/hello");
        FileOutputStream fop = new FileOutputStream(f);
        OutputStreamWriter writer = new OutputStreamWriter(fop, "UTF-8");

        writer.append("中文输入");
        writer.append("\r\n");
        writer.append("English");
        writer.close();
        fop.close();

        FileInputStream fip = new FileInputStream(f);
        InputStreamReader reader = new InputStreamReader(fip, "UTF-8");
        StringBuffer sb = new StringBuffer();
        while(reader.ready())
        {
            sb.append((char)reader.read());
        }
        System.out.println(sb.toString());
        reader.close();
        fip.close();
    }

    public static void main(String args[])
    {
        try
        {
            test6();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        
    }
}
