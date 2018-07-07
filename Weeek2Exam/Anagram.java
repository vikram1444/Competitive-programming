import java.util.*;
import java.util.Arrays;
public class Anagram
{
    static void isAnagram(String s1, String s2)
    {
        String copyOfs1 = s1.replaceAll("\\s", "");
 
        String copyOfs2 = s2.replaceAll("\\s", "");

        boolean status = true;
 
        if(copyOfs1.length() != copyOfs2.length())
        {
            
 
            status = false;
        }
        else
        {
            
 
            char[] s1Array = copyOfs1.toLowerCase().toCharArray();
 
            char[] s2Array = copyOfs2.toLowerCase().toCharArray();
 
           
 
            Arrays.sort(s1Array);
 
            Arrays.sort(s2Array);
 
           
 
            status = Arrays.equals(s1Array, s2Array);
        }
 
 
 
        if(status)
        {
            System.out.println(s1+" and "+s2+" true");
        }
        else
        {
            System.out.println(s1+" and "+s2+" false");
        }
    }
 
    public static void main(String[] args)
    {
        isAnagram("anagram", "nagaram");
 
        isAnagram("Keep", "Peek");
 
        isAnagram("Mother In Law", "Hitler Woman");
 
        isAnagram("School Master","The Classroom ");
 
        isAnagram("School MASTER", "The ClassROOM");
 
        isAnagram("DORMITORY", "Dirty Room");
 
        isAnagram("ASTRONOMERS", "NO MORE STARS");
 
        isAnagram("Toss", "Shot");
 
        isAnagram("joy", "enjoy");

        isAnagram("Debit Card","Bad Credit");
        
        isAnagram("Dormitory","Dirty Room");

        isAnagram("SiLeNt CAT", "LisTen AcT");
    }

}
