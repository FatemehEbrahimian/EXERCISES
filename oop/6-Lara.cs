public class Human : Lara 
{
   public Lara(string name,string gender,int age,string blood_group)
    {
      Name = name;
      Gender = gender;
      Age = age;
      Blood_group = blood_group;
    }
   public string Job() {
    return "Boss.";
   }
   public string Hobby() {
    return "Swimming.";
   } 

}
