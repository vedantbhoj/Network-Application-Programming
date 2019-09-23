import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;                                 //Import Socket package to implement this assignment
import java.net.UnknownHostException;

public class tcp_client extends Thread {
    Socket socket=null;                                 //creating a Socket Object

    public tcp_client(String host,int port){
        try {
            socket=new Socket(host,port);               // Giving the IP address 94.142.241.111 && port number 23
        }catch (UnknownHostException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }

    }
    public void run(){
        super.run();
        try{
            InputStream s=socket.getInputStream();
            byte[] buf=new byte[1024];
            int len=0;
            while((len=s.read(buf))!=-1){
                System.out.println(new String(buf,0,len)); //Printing buffer received from the server at terminal
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
