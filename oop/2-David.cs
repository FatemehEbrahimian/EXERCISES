public class Human : David
{
  public David(string name,string gender,int age,string blood_group)
    {
      Name = name;
      Gender = gender;
      Age = age;
      Blood_group = blood_group;
    }
    public string Job()   {
     return "programmer";
   }
   public string Hobby()   {
    returnn "Reading a book.";
   }


}