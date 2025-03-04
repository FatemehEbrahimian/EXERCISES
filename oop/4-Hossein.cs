public class Human : Hossein
{
   public Hossein(string name,string gender,int age,string blood_group)
    {
      Name = name;
      Gender = gender;
      Age = age;
      Blood_group = blood_group;
    }
   public string Job()   {
    return "Teacher.";
   }
   public string Hobby()   {
    returnn "Playing football.";
   }
}