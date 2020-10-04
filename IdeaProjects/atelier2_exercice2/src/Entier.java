public  class Entier {
    protected int borne_inf;
    protected int borne_sup;
    protected int valeur;

    public Entier(int borne_inf,int borne_sup,int valeur){
        /**
         * constructeur avec comme paramètres borne_inf,borne_sup et valeur
         * borne_inf = borne inférieure
         * borne_sup = borne supérieure
         * valeur = une valeur comprise entre la borne inférieure et supérieure
         **/
        this.borne_inf=borne_inf;
        this.borne_sup=borne_sup;
        this.valeur= valeur;

    }

    public Entier(int borne_inf,int borne_sup){
        /**
         * constructeur avec comme paramètres borne_inf et borne_sup
         * borne_inf = borne inférieure
         * borne_sup = borne supérieure
         * valeur = initialisée à 0
         **/

        this.borne_inf=borne_inf;
        this.borne_sup=borne_sup;
        this.valeur=0;
    }

    public Entier(){
        /**
         * constructeur sans paramètre
         * borne_inf = initialisée à 0
         * borne_sup = initialisée à 10
         * valeur = initialisée à 0
         **/
        this.borne_inf=0;
        this.borne_sup=10;
        this.valeur=0;

    }

    public int getBorne_inf() {
        /**
         * retourne la borne inférieure d'Entier
         **/
        return borne_inf;
    }

    public int getBorne_sup() {
        /**
         * retourne la borne supérieure d'Entier
         **/
        return borne_sup;
    }

    public int getValeur(){
        /**
         * retourne la valeur d'Entier
         **/
        return valeur;
    }

    public void setValeur(int nb){
        /**
         * modifie la valeur d'Entier par nb si il est compris entre la borne inférieure et la borne supérieure
         **/
        if((nb>=borne_inf)&&(nb<=borne_sup)){
        this.valeur = nb;}
    }

    public void incremente(){
        /**
         * incrémente la valeur de 1 si elle ne dépasse pas la borne sup
         **/
        if(this.valeur != borne_sup){
            this.valeur++;
        }
    }

    public void incremente(int n){
        /**
         * incrémente la valeur de n si elle ne dépasse pas la borne sup ou la borne inf ( int peut être négatif)
         */
        if((this.valeur + n <= borne_sup)&&(this.valeur + n >= borne_inf)){
            this.valeur= this.valeur+n;
        }
    }

    public String toString(){
        /**
         * @return un string avec la valeur de l'entier et ses bornes
         */
        return(" L'entier est de valeur "+ this.valeur + " compris entre " + this.borne_inf + " et " + this.borne_sup);
    }
}
