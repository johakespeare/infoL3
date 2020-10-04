import java.util.Random;

public class EntierFou extends Entier {
private int niveauDeFolie;
private Random r = new Random();

    public EntierFou(int borne_inf,int borne_sup, int valeur, int niveauDeFolie){
        super();

        this.borne_inf = borne_inf;
        this.borne_sup = borne_sup;
        this.valeur = valeur;
        this.niveauDeFolie = niveauDeFolie;
    }

    @Override
    public void incremente() {
        incremente(r.nextInt(niveauDeFolie));
    }
}
