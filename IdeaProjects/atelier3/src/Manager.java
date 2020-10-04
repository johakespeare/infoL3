import java.util.GregorianCalendar;

public class Manager extends Employe {
    private Secretaire secretaire;

    protected Manager(double salaire, int date_embauche, int age, Secretaire secretaire) {
        super(salaire, date_embauche, age);
        this.secretaire=secretaire;
    }

    public void augmenterLeSalaire(int pourcentage){
        /**
         * @param pourcentange = taux d'augmentation du salaire
         */
        this.salaire = this.salaire*pourcentage + 0.5*(this.salaire);
    }
    public void setSecretaire(Secretaire secretaire){
        /**
         * @param secretaire = la nouvelle secrétaire
         */
        this.secretaire= secretaire;
    }
}
