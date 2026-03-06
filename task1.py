good = r"""
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
"""
bad = r"""
 7_O_/           
  (/ 
  /\/' 
 7  
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: Finally I can see."
    print(good)
else:
    outcome = "Doom: AHHHHHH,wheres the light."
    print(bad)
print(outcome)