package Classes;

/**
 * Classe Employe
 * @author Johanna Fericean
 *
 */
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class Employe extends Personne {
    protected double salaire;
    protected int date_embauche;

    public Employe(String leNom, String lePrenom, GregorianCalendar laDate, Adresse lAdresse, double salaire) {
        super(leNom, lePrenom, laDate, lAdresse);
        this.salaire = salaire;
        Calendar c = Calendar. getInstance();
        this.date_embauche = c. get(Calendar. YEAR);
        System.out.println(date_embauche);
    }

    public void createEmploye(String leNom, String lePrenom, GregorianCalendar laDate, Adresse lAdresse, double salaire){
        /**
         * * @param salaire= salaire de l'employé
         * * @param date_embauche = date d'embauche de l'employé
         * * @param age = age de l'employé
         */
        Calendar c = Calendar. getInstance();
        int year = c. get(Calendar. YEAR);
        int age = year - laDate.get(Calendar.YEAR);
        System.out.println(age);
        if((age>16)&&(age<65)){
            Employe e = new Employe(leNom, lePrenom, laDate, lAdresse, salaire);
            System.out.println("un nouvel employé");
        }
        else System.out.println("l'age pas valide");
    }

    public double getSalaire() {
        return salaire;
    }

    public void augmenterLeSalaire(double pourcentage){
        /**
         * @param pourcentage = pourcentage d'augmentation du salaire
         */
        if(pourcentage>=0){
            this.salaire = this.salaire + this.salaire*pourcentage;
            System.out.println("salaire augmenté");
        }
        else{
            System.out.println("le pourcentage n'est pasp positif");
        }
    }

    public int calculAnnuite(){
        /**
         * retourne le nombre d'années que l'employé a passé dans l'entreprise
         */
        Calendar c = Calendar. getInstance();
        int year = c. get(Calendar. YEAR);
        return(-this.date_embauche + year);
    }


}

