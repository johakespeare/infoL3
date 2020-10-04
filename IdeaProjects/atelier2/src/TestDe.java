public class TestDe {
    public static void main(String[] args){
//        De six = new De(6);
//        System.out.println(six.getNbFaces()+six.getNom());
//        De random = new De();
//        System.out.println(random.getNbFaces()+random.getNom());
//        System.out.println("le meilleur coup est "+six.lancer(3));
//          DePipe de = new DePipe(23,"camembert",12);
//          System.out.println(de.getNom() + " " +de.getNbFaces() + " de borne" + de.getBorne()+ " lancer" + de.lancer(5));
        DeMemoire de = new DeMemoire(23,"camembert");
        System.out.println(de.getNom() + " " +de.getNbFaces() + " lancer" + de.lancer(5));
    }

}
