public class Test {
    public static void main(String args[]){
        Rectangle rectangle = new Rectangle("rectangle",5,10);
        Cercle cercle = new Cercle("cercle",5);
        Ellipse ellipse= new Ellipse("ellipse",4,8);
        Sphere sphere = new Sphere("sphere",7);
        Cylindre cylindre = new Cylindre("cylindre",3,12);

        Forme[] tableau = {rectangle,cercle,ellipse,sphere,cylindre};

        for(int i=0;i< tableau.length;i++){
            System.out.println(tableau[i].toString());
        }

        //test equals
        Rectangle rectangle2 = new Rectangle("rectangle",5,10);
        Cercle cercle2 = new Cercle("cercle",5);
        Cylindre cylindre2 = new Cylindre("cylindre2",3,12);
        Ellipse ellipse2= new Ellipse("ellipse",5,8);
        Sphere sphere2 = new Sphere("sphere",10);

        System.out.println( rectangle.equals(rectangle2));
        System.out.println(cercle.equals(cercle2));
        System.out.println(cylindre.equals(cylindre2));
        System.out.println(ellipse.equals(ellipse2));
        System.out.println(sphere2.equals(sphere));




    }
}
