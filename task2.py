good = r"""
                __
               / o\
               \_ /
                <|
                <|
                <|
                `
"""
bad = r"""
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
"""
has_key = True
if has_key:
    outcome = "Click: yay I got in!"
    print(good)
else:
    outcome = "Doom: Oh no imlocked out."
    print(bad)
print(outcome)