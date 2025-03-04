public class Human : Mahdis
{
    public Mahdis(string name,string gender,int age,string blood_group)
    {
      Name = name;
      Gender = gender;
      Age = age;
      Blood_group = blood_group;
    }
    public string Job()   {
        return "Programmer";
    }
    public string Hobby()   {
        return "Watching movies.";
    
   }
    public string Place_of_residence() {
        return "Japan.";
    }
}