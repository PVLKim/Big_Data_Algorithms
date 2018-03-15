package cs.bigdata.Tutorial2;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
@SuppressWarnings("unused")

public class Tree {
	private float[] geolocalisation = new float[2];
	private int arrondissement;
	private String genre;
	private String espece;
	private String famille;
	private int anneePlantation;
	private float hauteur;
	private float circonference;
	private String adresse;
	private String nomCommun;
	private String variete;
	private int idArbre;
	private String nomEnvironnement;
	public Tree(String line)
	{
		String[] lineSplit = line.split(";");
		String[] geoLoc = lineSplit[0].substring(1, lineSplit[0].length() - 1).split(",");
		if (geoLoc.length == 2 && !geoLoc[0].isEmpty() && !geoLoc[1].isEmpty())
		{
			this.geolocalisation[0] = Float.parseFloat(geoLoc[0]);
			this.geolocalisation[1] = Float.parseFloat(geoLoc[1]);
		}
		if (!lineSplit[1].isEmpty())
		{
			this.arrondissement = Integer.parseInt(lineSplit[1]);
		}
		this.genre = lineSplit[2];
		this.espece = lineSplit[3];
		this.famille = lineSplit[4];
		if (!lineSplit[5].isEmpty())
		{
			this.anneePlantation = Integer.parseInt(lineSplit[5]);
		}
		if (!lineSplit[6].isEmpty())
		{
			this.hauteur = Float.parseFloat(lineSplit[6]);
		}
		if (!lineSplit[7].isEmpty())
		{
			this.circonference = Float.parseFloat(lineSplit[7]);
		}
		this.adresse = lineSplit[8];
		this.nomCommun = lineSplit[9];
		this.variete = lineSplit[10];
		if (!lineSplit[11].isEmpty())
		{
			this.idArbre = Integer.parseInt(lineSplit[11]);
		}
		this.nomEnvironnement = lineSplit[12];
	}
	public static void main(String[] args) throws IOException {
		//localSrc when not used within hadoop
		//String localSrc = System.getProperty("user.dir") + "/arbres.csv";
		String localSrc = "/Users/pavelkim/eclipse-workspace/Data/arbres.csv"; // your directory with .csv file
		Path path = new Path(localSrc);
		//Open the file
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		FSDataInputStream in = fs.open(path);
		try{
			InputStreamReader isr = new InputStreamReader(in);
			BufferedReader br = new BufferedReader(isr);
			String line = br.readLine();		
			while (line !=null){
				// Split the information in a line
				String[] lineTab = line.split(";");
				// If the year/height is missing, we will display NULL
				if (lineTab[5].isEmpty())
				{
					lineTab[5] = "NULL";
				}
				if (lineTab[6].isEmpty())
				{
					lineTab[6] = "NULL";
				}
				// Print the result
				System.out.println(lineTab[5] + " - " + lineTab[6]);
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