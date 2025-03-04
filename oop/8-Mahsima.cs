public class Human : Mahsima 
{
  public Mahsima(string name,string gender,int age,string blood_group)
    {
      Name = name;
      Gender = gender;
      Age = age;
      Blood_group = blood_group;
    }
     public string Job() {
        return "Student.";
     }
     public string Hobby() {
        return "Surfing the net.";
     }
     public bool Can_walk() {
        return False
     }
}