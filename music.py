class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds

  def solo(self, length):
    for i in range(length):
      print(self.sounds[i % len(self.sounds)])
    print("")


class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
        
class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["boom","bash","cymbal"])
  
    def solo(self, length):
      for i in range(length):
        print(self.sounds[i % len(self.sounds)])
      print("")
      
    def count_to_four(self):
      for j in range(1,5):
        print("%s" %j)
        
    def combust(self):
      print("BOOM!!!!!")
      
class Band(object):
  def __init__(self):
    self.members = {}
  
  def hire(self):
    new_member = input("What's the new bandmember's name? ")
    type_of_musician = input("Is he a drummer or a guitarist (lower case please)? ")
    if type_of_musician == "drummer":
      self.members[new_member] = Drummer()
    elif type_of_musician == "guitarist":
      self.members[new_member] = Guitarist()
      
    
  def fire(self,fired_member):
    del self.members[fired_member]
    
  def play_solos(self,length):
    #check to see if there is a drummer in the list of values of members, if so execute code , else execute  other code
    for v in self.members.itervalues():
      band_has_drummer = isinstance(v,Drummer)
      break 
    if band_has_drummer:
      print("There is a drummer")
      for musician in self.members.itervalues():
        musician.count_to_four()
        musician.solo(length)
        musician.combust()
    else:
      print("There is no drummer")
      for musician in self.members.itervalues():
        musician.solo(length)
      

    
def main():
  var = Band()
  var.hire()
  var.hire()
  var.hire()
  var.fire("Ram")
  print(var.members)
  var.play_solos(6)
  
if __name__ == "__main__":
  main()
