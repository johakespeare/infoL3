package tp1.test;
import Classes.Personne;
import Classes.Adresse;
import java.util.GregorianCalendar;

public class testQuestion1 {
    public static void main(String args[]){
        int nb_persones_crees=5;
        for (int i=0;i<5;i++){
            GregorianCalendar calendar = new GregorianCalendar(2000,9,30);
            Adresse adresse = new Adresse(20,"des potiers","20167","malibou");
            Personne p = new Personne("jean","marc",calendar,adresse);
            System.out.println(p.getNb_personnes());
        }


    }

}
