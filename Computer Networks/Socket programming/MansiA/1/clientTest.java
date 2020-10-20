import java.io.*;  
import java.net.*;  
public class clientTest 
{  
	public static void main(String args[])throws Exception
	{  
		Socket s=new Socket("localhost",5555);  
		DataInputStream din=new DataInputStream(s.getInputStream());  
		DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));  
		String str="",str2="";  
		while(!str.equals("yes"))
		{  
			str=br.readLine();  
			dout.writeUTF(str);  
			dout.flush();  
			str2=din.readUTF();  
			System.out.println("server message: "+str2);  
		}  
		dout.writeUTF("Server has disconnected");   
		dout.close();  
		s.close();  
	}
}  