public class DeMemoire extends De{
        /** ATTRIBUTS**/
    private int lancer_precedent;
        /**CONSTRUCTEUR**/
    public DeMemoire(int nbFaces , String nom){
        super(nbFaces,nom);
        this.lancer_precedent=0;
    }
        /** METHODES **/
    @Override
    public int lancer(int nbCoups) {
        int max=0;
        for (int i=0;i<nbCoups;i++){
            int lancer = lancer();
            while (lancer==lancer_precedent){
             lancer = lancer();}

            System.out.println(lancer + " le lancer précédent"+ lancer_precedent);
            if(max<lancer){
                max=lancer;
            }
            lancer_precedent=lancer;
        }
        return(max);
    }
}
