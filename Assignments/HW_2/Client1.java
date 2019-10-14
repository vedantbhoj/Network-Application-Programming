
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.SocketTimeoutException;

public class Client1 {
    public static void main(String[] args) throws IOException {
        //Client submit a request to localhost->127.0.0.1 and port 200006
        Socket client = new Socket("127.0.0.1", 20006);
        // set time out time
        client.setSoTimeout(10000);
        BufferedReader buf =  new BufferedReader(new InputStreamReader(client.getInputStream()));

        try{
            String echo = buf.readLine();
            draw(echo);// draw the picture with the parameter send back from the server, in Lab2 case is hello world.
            }catch(SocketTimeoutException e){
            System.out.println("Time out, No response");
        }
        if(client != null){
            client.close();
        }

    }
    public  static void draw(String string){
        int width = 100;
        int height = 30;
        StringBuilder builder=null;
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        Graphics g = image.getGraphics();
        g.setFont(new Font("SansSerif", Font.BOLD, 16));

        Graphics2D graphics = (Graphics2D) g;
        graphics.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING,
                RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
        graphics.drawString(string, 10, 20);

        for (int y = 0; y < height; y++) {
            StringBuilder sb = new StringBuilder();
            for (int x = 0; x < width; x++) {

                sb.append(image.getRGB(x, y) == -16777216 ? " " : "$");

            }

            if (sb.toString().trim().isEmpty()) {
                continue;
            }
            System.out.println(sb);

        }

    }
}