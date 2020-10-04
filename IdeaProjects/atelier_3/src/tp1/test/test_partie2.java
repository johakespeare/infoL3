package tp1.test;

import Classes.*;

import java.util.GregorianCalendar;

public class test_partie2 {
    public static void main(String args[]){
        GregorianCalendar calendar1 = new GregorianCalendar(2000,9,30);
        GregorianCalendar calendar2 = new GregorianCalendar(2010,9,30);
        Adresse adresse = new Adresse(20,"des potiers","20167","malibou");

        //test age employés
        Employe employeTropJeune = new Employe("thomas","davant",calendar2,adresse,1200);
        employeTropJeune.createEmploye("thomas","davant",calendar2,adresse,1200);
        Employe employe1 = new Employe("thomas","davant",calendar1,adresse,1200);
        employe1.createEmploye("thomas","davant",calendar1,adresse,1200);

        //test calcul salaire manager
        Secretaire secretaire1 = new Secretaire("caroline","davant",calendar1,adresse,1200,2000);
        Manager manager1 = new Manager("jean","marc",calendar1,adresse,1200,2000,secretaire1);
        manager1.augmenterLeSalaire(0.5);
        manager1.augmenterLeSalaire(-885);
        System.out.println(manager1.getSalaire());

        //test changement de secrétaire
        Secretaire secretaire2 = new Secretaire("gertrude","davant",calendar1,adresse,1200,2000);
        manager1.setSecretaire(secretaire2);
        System.out.println("la secrétaire était "+ secretaire1.getNom()+"maintenant c'est "+ manager1.getSecretaire().getNom());

        //test nombre de secrétaires
        int Nb_managers=6;
        for (int i=0;Nb_managers>i ;i++){
            Manager manager = new Manager("jean","marc",calendar1,adresse,1200,2000,secretaire1);
            secretaire1.add_manager(manager);
        }
        System.out.println(secretaire1.getManagers());

    }
}

