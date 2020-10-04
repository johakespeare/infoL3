import java.util.*;

import tp1.personnel.util.Adresse;

public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
	private static int nb_personnes;
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		nb_personnes++;
	}
	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'ann�e de naissance
	 * @param numero le n� de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le pr�nom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}
		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Pr�nom : "+prenom+"\n"+
		"N�(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
		"-"+dateNaissance.get(Calendar.MONTH)+
		"-"+dateNaissance.get(Calendar.YEAR)+"\n"+
		"Adresse : "+ adresse.toString() ;
		return result;
	}

	public int getNb_personnes(){
		return(nb_personnes);
	}

	public boolean PlusAgeQue( Personne personne) {
		return(this.getDateNaissance().compareTo(personne.getDateNaissance())>0) ;
	}

	public boolean equals(Object obj1){
		boolean idem= false;
		if(obj1 instanceof Personne){
			Personne autre = (Personne) obj1;
			System.out.println("caca");
			if((autre.getNom()==this.getNom())&&(autre.getDateNaissance()==this.getDateNaissance())&&(this.getPrenom()==autre.getPrenom())){
					idem=true; }
			}

		return idem;

	}
	public static void main(String args[]){
		Adresse adresse1 = new Adresse(20,"carotte","20157","bibiVille");
		Adresse adresse2 = new Adresse(25,"car9te","20147","ertyVille");
		GregorianCalendar date1 = new GregorianCalendar(1598,01,19);
		GregorianCalendar date2 = new GregorianCalendar(2000,10,20);
		Personne caca = new Personne("jean eudes","barbarie",date1,adresse1);
		Personne caca2 = new Personne("natacha"," la chaudasse",date2,adresse2);
		Personne caca3 = new Personne("natacha"," la chaudasse",date2,adresse2);
		System.out.println(caca3.equals(caca2));
	}
}




   
   