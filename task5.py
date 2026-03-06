good =r"""
  (>,  oo      
        /  8 "} > @ <
        |`.8 .-._/| 
        `-.'`')`_.'
           ) /    
          /  |__,      
          |    ( /   
        .'    , /  
         `._/  '`- 
          \|        
     --  -`' -        ---
"""
bad = r"""
     __________
    /`.`^%===_/
    `. `\ 
      `. `. 
        `./
"""
escaped = True
if escaped:
    outcome = "Legend: FREEDOM!!!!"
    print(good)
else:
    outcome = "Doom: NOOOOO im trapped forever."
    print(bad)
print(outcome)