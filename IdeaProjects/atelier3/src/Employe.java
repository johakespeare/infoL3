import java.util.Calendar;

public class Employe {
    protected double salaire;
    protected int date_embauche;

    protected Employe(double salaire, int date_embauche, int age){
        /**
         * @param salaire= salaire de l'employé
         * @param date_embauche = date d'embauche de l'employé
         * @param age = age de l'employé
         */
        this.salaire = salaire;
        this.date_embauche = date_embauche;
    }

    public void createEmploye(double salaire, int date_embauche, int age){
        /**
         * * @param salaire= salaire de l'employé
         *          * @param date_embauche = date d'embauche de l'employé
         *          * @param age = age de l'employé
         */
        if((age>16)&&(age<65)){
            Employe e = new Employe(salaire,date_embauche,age);
            System.out.println("un nouvel employé");
        }
        else System.out.println("l'age pas valide");
    }

    public void augmenterLeSalaire(double pourcentage){
        /**
         * @param pourcentage = pourcentage d'augmentation du salaire
         */
        if(pourcentage>=0){
            this.salaire = this.salaire + this.salaire*pourcentage;
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
