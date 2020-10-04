package Classes;

/**
 * Classe Secrétaire
 * @author Johanna Fericean
 *
 */

import java.util.ArrayList;
import java.util.GregorianCalendar;


public class Secretaire extends Employe {
    ArrayList<Manager> list_managers = new ArrayList<Manager>();

    public Secretaire(String leNom, String lePrenom, GregorianCalendar laDate, Adresse lAdresse, double salaire, int date_embauche) {
        /** constructeur de la classe Manager
         * @param leNom le nom de la secrétaire
         * @param lePrenom le pr�nom de la secrétaire
         * @param laDate la date de naissance de la secrétaire
         * @param lAdresse l'adresse de la secrétaire
         * @param salaire le salaire de la secrétaire
         * @param date_embauche la date où la secrétaire a été embauché
         */
        super(leNom, lePrenom, laDate, lAdresse, salaire);
    }


    public void add_manager(Manager manager){
            /** fonction qui ajoute un manager à la secrétaire, si elle en a déjà 5, n'en ajoute pas
             * @param manager = le manager qu'on ajoute à la secrétaire
             */
            if(list_managers.size()<5){
                list_managers.add(manager);}
            else System.out.println("trop de managers");
    }

    public void del_manager(Manager manager){
        /** fonction qui supprimer un manager
         * @param manager = le manager qu'on supprime à la secrétaire
         */
        list_managers.remove(manager);
    }
    public void augmenterLeSalaire(int pourcentage){
        /**la fonction augmente le salaire du manager
         * @param pourcentange = taux d'augmentation du salaire
         */
        if(pourcentage>=0){
            this.salaire = this.salaire*pourcentage + this.getManagers()*0.1*(this.salaire);
            System.out.println("le salaire a été augmenté");
        }
        else{
            System.out.println("le pourcentage n'est pas positif!");
        }
    }

    public int getManagers(){
        /**
         * retourne le nombre de managers de la secrétaire
         */
        return(list_managers.size());
    }

}

