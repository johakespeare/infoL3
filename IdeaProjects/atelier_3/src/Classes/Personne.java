package Classes;
import java.util.*;

public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
    private static int nb_personnes=0;
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
		/**
		 * Modificateur
		 * @param retourne l'adresse
		 */

		return adresse;
	}

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
		"Adresse : "+
		adresse.toString();
		return result;
	}

	public int getNb_personnes(){
		/**
		 * @return : le nombre d'objets personne créés
		 */
		return(nb_personnes);
	}

	public boolean plusAge(Personne personne_1,Personne personne_2){
		/**
		 * @param personne1 = un objet personne
		 * @param personne2 = un objet personne
		 * @return booleen = true si la personne1 est plus agée que la personne2 en paramètres
		 */
		return(personne_1.getDateNaissance().compareTo(personne_2.getDateNaissance())>0);

	}
	public boolean plusAgeQue( Personne personne) {
		/**
		 * @param personne = un objet personne
		 * @return booleen = true si la personne est plus agée que la personne en paramètres
		 */
		return(this.getDateNaissance().compareTo(personne.getDateNaissance())>0) ;
	}

	public boolean equals(Object obj1){
		boolean idem= false;
		if(obj1 instanceof Personne){
			Personne autre = (Personne) obj1;
			if((autre.getNom().equals(this.getNom()))&&(this.getDateNaissance()==autre.getDateNaissance())
					&&(this.getPrenom().equals(autre.getPrenom()))){
				idem=true;
		       }
		}

		return idem;

	}

}

    
   
   