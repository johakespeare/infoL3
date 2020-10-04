package tp1.test;
import Classes.Personne;
import Classes.Adresse;
import java.util.GregorianCalendar;

public class testQuestion4 {
    public static void main(String args[]){
        GregorianCalendar calendar1 = new GregorianCalendar(2000,9,30);
        GregorianCalendar calendar2 = new GregorianCalendar(2000,1,30);
        Adresse adresse = new Adresse(20,"des potiers","20167","malibou");
        Adresse adresse2 = new Adresse(20645,"des potiers","20167","malibou");
        Personne personne1 = new Personne("thomas","davant",calendar1,adresse);
        Personne personne2 = new Personne("jean","marc",calendar2,adresse);
        Personne personne3 = new Personne("thomas","davant",calendar1,adresse2);


       System.out.println(personne1.equals(personne2));
       System.out.println(personne1.equals(personne3));
    }
}
