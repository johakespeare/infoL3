import java.util.ArrayList;


public class Secretaire extends Employe{
    ArrayList<Manager> list_managers = new ArrayList<Manager>();
    protected Secretaire(double salaire, int date_embauche, int age) {
        super(salaire, date_embauche, age);

    }

    public void add_manager(Manager manager){
        /**
         * @param manager = le manager qu'on ajoute à la secrétaire
         */
        if(list_managers.size()<5){
        list_managers.add(manager);}
        else System.out.println("trop de managers");
    }
    public void del_manager(Manager manager){
        /**
         * @param manager = le manager qu'on supprime à la secrétaire
         */
        list_managers.remove(manager);
    }

    public int getManagers(){
        return(list_managers.size());
    }

}
