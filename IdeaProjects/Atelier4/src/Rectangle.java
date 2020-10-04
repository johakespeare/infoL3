public class Rectangle extends Forme_BiDimension{
    private double largeur;
    private double longueur;

    public Rectangle(String nom, double largeur, double longueur) {
        /**
         * constructeur de la classe Rectangle
         * @param nom = le nom du Rectangle
         * @param largeur = la largeur du Rectangle
         * @param longueur= la longueur du Rectangle
         */
        super(nom);
        this.largeur=largeur;
        this.longueur=longueur;
    }

    @Override
    public double perimetre() {
        /**
         * retourne le périmètre du rectangle
         */
        return (2*largeur+2*longueur);
    }

    @Override
    public double surface() {
        /**
         * retourne l'aire du rectangle
         */
        return (largeur*longueur);
    }


    @Override
    public boolean equals(Object objet) {
        boolean egal =false;
           if(objet==this){
               egal= true;
           }
           else if(this.getClass()==objet.getClass()){
               Rectangle other = (Rectangle) objet;
               if((other.longueur==this.longueur)&&(other.largeur==this.largeur)){
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
        return("la forme est un rectangle nommé "+ this.nom  +" de  longueur "+ this.longueur+" , de largeur "+ this.largeur +
                " de perimetre "+ this.perimetre() + " et de surface "+ this.surface());
    }

}
