public class DePipe extends De {
    /** ATTRIBUTS **/
private int borne;

        /**CONSTRUCTEUR**/
    public DePipe(int nbFaces , String nom, int borne){
        super();
        this.nbFaces=nbFaces;
        this.nom=nom;
        if((borne <= nbFaces )&&(borne !=0)){
        this.borne=borne;}
        i++;

    }
            /**METHODES**/
    public  int getBorne(){
        return(this.borne);
    }

    @Override
    public int lancer() {
        i =r.nextInt(this.getNbFaces() +1);
        while ( i <= this.borne) {
            i =r.nextInt(this.getNbFaces() +1);
        }
        return (i);
    }
}