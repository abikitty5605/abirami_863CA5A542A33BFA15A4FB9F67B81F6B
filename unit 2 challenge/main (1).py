class player:
  def play(self):
    print("the player is playing cricket.")

class batsman(player):
  def play(self):
    print("the batsman is batting.")

class bowler(player):
  def play(self):
    print("the bowler is bowling.")

batsman = Batsman()
bowler = Bowler()
