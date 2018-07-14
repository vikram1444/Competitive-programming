import java.util.*;
class binary{
       private String stri;
       private String str;
       public binary(Integer a,Integer b){
             stri=a.toBinaryString(a);
             str=b.toBinaryString(b);
       }
       public void details(){
           while(true){
               if(stri.length()==8){
                    break;
               }else{
                   stri="0"+stri;
                
               }
           }
           while(true){
            if(str.length()==8){
                 break;
            }else{
                str="0"+str;
            }
        } 
       }
       public int check()
       {
        int x=0;
        int count=0;   
        while(true){
            if(x==8){
                break;
            } else{
              if(str.charAt(x)!=stri.charAt(x)){
                  count++;
              }
            }
            x++;
           }
           return count;
       }
}
class binaryapp{
    public static void main(String[] args) {
        binary ob=new binary(25, 30);
        ob.details();
        System.out.println(ob.check());
        binary p=new binary(1,4);
        p.details();
        System.out.println(p.check());
        binary q=new binary(25, 30);
        q.details();
        System.out.println(q.check());
        binary r=new binary(100,250);
        r.details();
        System.out.println(r.check());
        binary s=new binary(1,30);
        s.details();
        System.out.println(s.check());
        binary t=new binary(0, 255);
        t.details();
        System.out.println(t.check());
    }
}
