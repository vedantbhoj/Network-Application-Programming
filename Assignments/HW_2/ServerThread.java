import java.io.PrintStream;
import java.net.Socket;


public class ServerThread implements Runnable {

    private Socket client = null;
    private StringBuilder test;
    public ServerThread(Socket client){
        this.client = client;
    }

    @Override
    public void run() {
        try{
            //get output stream that are going to send back to Client.
            PrintStream out = new PrintStream(client.getOutputStream());
            out.println("hello world");// Sending message to Client.
            out.close();
            client.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}