import java.io.*;  
import java.net.*;  

public class serverTest
{  
	public static void main(String args[])throws Exception
	{  
		ServerSocket ss=new ServerSocket(5555);  
		Socket s=ss.accept();  
		DataInputStream din=new DataInputStream(s.getInputStream());  
		DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));  
		  
		String str="",str2="";  
		while(!str.equals("yes"))
		{  
			str=din.readUTF();  
			System.out.println("client message: "+str);  
			str2=br.readLine();  
			dout.writeUTF(str2);  
			dout.flush();  
		}
		dout.writeUTF("Client has disconnected"); 	  
		din.close();  
		s.close();  
		ss.close();  
	}
}  