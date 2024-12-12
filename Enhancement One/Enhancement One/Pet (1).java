//Savion Peebles
//IT-145
//1/29/2023
//Professor Gossai

public class Pet 
{
	
	// PetSpecies cat or dog
	// dog and cat spaces available
	private String petName;
	private String petSpecies;
	private int petAge;
	// pet age measured in years
	private int dogSpaces;
	private int catSpaces;
	private int daysStayed;
	// Amount for bill
	private double amountDue; 
	
	//Constructor for pet class with all constructors
	Pet(String petSpecies,String petName, int petAge, int daysStayed){
		this.petSpecies = petSpecies;
		this.petName = petName;
		this.petAge = petAge;
		this.daysStayed = daysStayed;
	}
	
	public String getpetName() {
		return petName;
	}
	
	public void setpetName(String petName) {
		this.petName = petName;
	}
	
	public String getpetSpecies() {
		return petSpecies;
	}
	
	public void setpetSpecies(String petSpecies ) {
		this.petSpecies = petSpecies;
	}
	
	public int getpetAge() {
		return petAge;
	}
	
	public void setpetAge(int petAge) {
		this.petAge = petAge;
	}
	
	public int getDogspaces() {
		return dogSpaces;
	}
	
	public void setdogSpaces(int dogSpaces) {
		this.dogSpaces = dogSpaces;
	}
	
	public int getcatSpaces() {
		return catSpaces;
	}
	
	public void setcatSpaces(int catSpaces) {
		this.catSpaces = catSpaces;
	}
	
	public int getdaysStayed() {
		return daysStayed;
	}
	
	public void setdaysStayed(int daysStayed) {
		this.daysStayed = daysStayed;
	}
	
	public double getamountDue() {
		return amountDue;
	}
	
	public void setamountDue(double amountDue) {
		this.amountDue = amountDue;
	}
}
