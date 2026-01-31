package OSclass_activity;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

public class DateClient {
    public static void main(String[] args) {
        try{
            Socket sock = new Socket("127.0.0.1", 6013);

            InputStream in = sock.getInputStream();
            BufferedReader bin = new BufferedReader(new java.io.InputStreamReader(in));


            String line;
            while((line=bin.readLine())!=null){
                System.out.println(line);
            }

            sock.close();
        }

        catch (IOException ioe){
        System.err.println(ioe);
        }
    
    }   
}
