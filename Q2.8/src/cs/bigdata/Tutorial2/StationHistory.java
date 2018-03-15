package cs.bigdata.Tutorial2;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class StationHistory {
	public static void main(String[] args) throws IOException {
		//localSrc when not used within Hadoop
		//String localSrc = System.getProperty("user.dir") + "/isd-history.txt";
		String localSrc = "/Users/pavelkim/eclipse-workspace/Data/isd-history.txt";
		Path path = new Path(localSrc);
		//Open the file
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		FSDataInputStream in = fs.open(path);
		try{
			System.out.println("USAF - STATION NAME - CTRY - ELEV(M)");
			InputStreamReader isr = new InputStreamReader(in);
			BufferedReader br = new BufferedReader(isr);
			//count the first lines
			int numberLine = 0;
			// read line by line
			String line = br.readLine();
			while (line !=null){
				//The first 22 lines are not relevant, we discard them
				if (numberLine < 22)
				{
					numberLine += 1;
				}
				else
				{
					System.out.println(line.substring(13, 42) + " - " + line.substring(43, 45) + " - " + line.substring(74, 81));
					// Process of the current interesting line
					//System.out.println(line.substring(0, 6) + " - " + line.substring(13, 42) + " - " + line.substring(43, 45) + " - " + line.substring(74, 81));
				}
				// go to the next line
				line = br.readLine();
			}
		}
		finally{
			//close the file
			in.close();
			fs.close();
		}
	}
}