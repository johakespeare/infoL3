import java.util.*;

public class De {
    /***      ATTRIBUTS  ***/

protected int nbFaces;
protected String nom;
protected static Random r = new Random();
protected static int i=0;

/***            CONSTRUCTEURS       ***/
    public De(int nbFaces , String nom){
        this.nbFaces=nbFaces;
        this.nom = nom;
        i++;
    }

    public De(){
        this.setNbFaces(6);
        this.setNom("De n°"+ i);
        i++;

    }

    public De(int nbFaces){
        this.nbFaces= nbFaces;
        this.setNom("De n°"+ i);
        i++;
    }

    /***        METHODES  ***/

    public int getNbFaces() {
        return nbFaces;
    }

    public void setNbFaces(int nbFaces) {
        if((nbFaces>=3)&&(nbFaces<=120)){
                this.nbFaces = nbFaces;
            }
        else {
            System.err.print("pas bonne valeur");
        }
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        if(nom.length()!=0){
        this.nom = nom;}
        else{
            System.err.println(" le nom n'est pas correcte");
        }
    }

    public int lancer(){
        return(r.nextInt(this.getNbFaces() +1) );
    }

    public int lancer(int nbCoups){
    int max=0;
        for (int i=0;i<nbCoups;i++){
            int lancer = lancer();
            //System.out.println(lancer);
            if(max<lancer){
                max=lancer;
            }
        }
        return(max);
    }




}
