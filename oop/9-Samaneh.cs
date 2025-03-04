public class Human : Samaneh
{
    public Samaneh(string name,string gender,int age,string blood_group)
    {
      Name = name;
      Gender = gender;
      Age = age;
      Blood_group = blood_group;
    }
    public string Job()   {
        return "Lawyer";
    }
    public string Hobby()   {
        return "Reading poets.";
    
   }
}