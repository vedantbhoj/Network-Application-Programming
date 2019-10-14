import java.net.ServerSocket;
import java.net.Socket;

public class Server1 {
    public static void main(String[] args) throws Exception{
        //Server open a port at 20006
        ServerSocket server = new ServerSocket(20006);
        Socket client = null;
        boolean f = true;
        while(f){
            //Keep Waiting for the requests
            client = server.accept();
            System.out.println("Connect with Server successfully");
            //Create a new thread for each request.
            new Thread(new ServerThread(client)).start();
        }
        server.close();
    }
}