# MachEntry class to hold information of interest
# using the Mach-IV test
class MachEntry:

  # Contructor
  # @in score - calculated Mach-IV score
  # @in q6    - score of the question 6
  # @in q7    - score of the question 7
  # @in rel   - religion value (3-7)
  # @in TIPI1 - score on TIPI1
  # @in TIPI6 - score on TIPI6
  # @in ed    - eduation value
  # @in race  - race value
  # @in age   - age value
  # @in gen   - gender value
  def __init__(self, score, q6, q7, rel, TIPI1, TIPI6, ed, race, age, gen):
    self.Score = score
    self.Q6 = q6
    self.Q7 = q7
    self.Religion = rel
    self.TIPI1 = TIPI1
    self.TIPI6 = TIPI6
    self.Education = ed
    self.Race = race
    self.Age = age
    self.Gender = gen
    
  def GetScore(self):
    return self.Score
    
  def GetQ6(self):
    return self.Q6
    
  def GetQ7(self):
    return self.Q7
    
  def GetReligion(self):
    return self.Religion
    
  def GetTIPI1(self):
    return self.TIPI1
    
  def GetTIPI2(self):
    return self.TIPI2
    
  def GetEducation(self):
    return self.Education
    
  def GetRace(self):
    return self.Race
    
  def GetAge(self):
    return self.Age
    
  def GetGender(self):
    return self.Gender

