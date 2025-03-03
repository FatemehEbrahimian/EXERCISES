using System;

public abstract class Human
{
    public string Name { get; set; }
    public string Gender { get; set; }
    public int Age { get; set; }
    public string Blood_group { get; set; }
    public bool Can_walk()    {
        return True;
   }
   public string Can_breath()   {
    return True;
   }
   public string Can_eat()    {
    return True;
   }
   public string Place_of_residence()   {
    return "Iran";
   }
   public string Job();
    public string Hobby();
}
