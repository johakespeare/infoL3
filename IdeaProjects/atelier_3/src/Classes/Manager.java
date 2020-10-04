package Classes;
import java.util.GregorianCalendar;


/**
 * Classe Manager
 * @author Johanna Fericean
 *
 */

public class Manager extends Employe {
    private Secretaire secretaire;

    public Manager(String leNom, String lePrenom, GregorianCalendar laDate, Adresse lAdresse, double salaire, int date_embauche, Secretaire secretaire) {
        /** constructeur de la classe Manager
         * @param leNom le nom du Manager
         * @param lePrenom le pr�nom du Manager
         * @param laDate la date de naissance du Manager
         * @param lAdresse l'adresse du Manager
         * @param salaire le salaire du Manager
         * @param date_embauche la date où l'employé a été embauché
         */
        super(leNom, lePrenom, laDate, lAdresse, salaire);
        this.secretaire=secretaire;
    }

    public void augmenterLeSalaire(int pourcentage){
        /**la fonction augmente le salaire du manager
         * @param pourcentange = taux d'augmentation du salaire
         */
        if(pourcentage>=0){
            this.salaire = this.salaire*pourcentage + 0.5*(this.salaire);
            System.out.println("le salaire a été augmenté");
        }
       else{
           System.out.println("le pourcentage n'est pas positif!");
        }
    }
    public void setSecretaire(Secretaire secretaire){
        /** la fonction modifie la secrétaire du Manager
         * @param secretaire = la nouvelle secrétaire
         */
        this.secretaire= secretaire;
    }

    public Secretaire getSecretaire() {
        return secretaire;
    }
}
