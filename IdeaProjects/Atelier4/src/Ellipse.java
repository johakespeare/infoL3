import java.lang.Math;

public class Ellipse extends Forme_BiDimension{
private double petit_axe;
private double grand_axe;

    public Ellipse(String nom,double petit_axe, double grand_axe) {
        /**
         * constructeur de la classe Ellipse
         * @param nom = le nom de l'Ellipse
         * @param petit_axe = le petit axe de l'Ellipse
         * @param grand_axe = le grand axe de l'Ellipse
         */
        super(nom);
        this.grand_axe=grand_axe;
        this.petit_axe=petit_axe;
    }

    @Override
    public double perimetre(){
        /**
         * calcule le périmètre de l'ellipse qui est égale à 2pi*sqrt((petit_axe²+grand_axe²)/2)
         */
        return(Math.PI *2 * Math.sqrt((Math.pow(petit_axe,2) +Math.pow(grand_axe,2))/2));
    }

    @Override
    public double surface(){
        /**
         * calcule la surface de l'ellipse qui est égale à pi*petit_axe*grand_axe
         */
        return(Math.PI * this.petit_axe * this.grand_axe);
    }

    @Override
    public boolean equals(Object objet) {
        boolean egal =false;
        if(objet==this){
            egal= true;
        }
        else if(this.getClass()==objet.getClass()){
            Ellipse other = (Ellipse) objet;
            if((other.petit_axe==this.petit_axe)&&(other.grand_axe==this.grand_axe)){
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
        return("la forme est une ellipse nommée "+ this.nom  +" de  petit axe "+ this.petit_axe+" , de Grand axe "+ this.grand_axe +
               " de perimetre "+ this.perimetre() + " et de surface "+ this.surface());
    }

}
