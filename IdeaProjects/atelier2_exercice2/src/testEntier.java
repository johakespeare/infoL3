public class testEntier {
    {}
    public static void main(String args[]){
        Entier deux = new Entier(0,10,5);
        System.out.println(deux.toString());
        deux.incremente();

        System.out.println(deux.toString());
        deux.incremente(3);

        System.out.println(deux.toString());
//        Entier Un = new Entier(0,10);
//        System.out.println(Un.toString());
//        Un.setValeur(15);
//        System.out.println(Un.toString());
//        Un.setValeur(5);
//        System.out.println(Un.toString());
          EntierFou fou = new EntierFou(0,10,5,5);
          System.out.println(fou.toString());
          fou.incremente();
          System.out.println(fou.toString());
    }
}
