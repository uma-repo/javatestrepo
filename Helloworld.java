public class Helloworld{

        public static void main(String args[]){
                Helloworld hw = new Helloworld();
                System.out.println(hw.addnum(Integer.parseInt(args[1]),Integer.parseInt(args[2])));
        }
        public int addnum(int a,int b){
                return (a+b);
        }
}
