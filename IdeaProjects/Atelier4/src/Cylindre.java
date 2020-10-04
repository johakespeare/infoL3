public class Cylindre extends Forme_TriDimension {
    private double rayon;
    private double hauteur;

    public Cylindre(String nom,double rayon,double hauteur) {
        /**
         * constructeur de la classe Cylindre
         */
        super(nom);
        this.rayon = rayon;
        this.hauteur = hauteur;

    }

    @Override
    public double volume() {
        /**
         * retourne le volume du cylindre
         */
        return Math.pow(this.rayon,2)*Math.PI*this.hauteur;
    }



    @Override
    public double surface() {
        /**
         * retourne la surface du cylindre
         */
        return 2*Math.PI*this.rayon*(this.rayon+this.hauteur);
    }

    @Override
    public boolean equals(Object objet) {
        boolean egal =false;
        if(objet==this){
            egal= true;
        }
        else if(this.getClass()==objet.getClass()){
            Cylindre other = (Cylindre) objet;
            if((other.rayon==this.rayon)&&(other.hauteur==this.hauteur)){
                egal= true;
            }
        }
        else{
            egal =false;
        }

        return egal;
    }

    @Override
    public String toString() {
        return("la forme est un cylindre nommé "+ this.nom  +" de rayon "+ this.rayon+" d'hauteur "+ this.hauteur +" , de volume "+ this.volume() + " et de surface "+ this.surface());
    }

}
