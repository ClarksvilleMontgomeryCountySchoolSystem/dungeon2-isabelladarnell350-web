good = r"""
            'x|`
          '|xx| `          '|x|
  `   '    |xx|    `   '    |x|`
           |xx|             |x|
  ============|===============|===--
  ejm ~~~~~|xx|~~~~~~~~~~~~~|x|~~~ ~~  ~   ~
"""
bad = r"""
 _______________________________
|                               |
|                               |
|                               |
|                               |
|                               |
|     "Sucker..."               |
|         \                     |
|          \                    |
|            \\\\               |
|            ( oo               |
|             \o/               |
|___________ /F-O\_____________ |
|            \\_//              |
|             //\\              |
|            // //              |
|           (_)(_)              |
"""
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: Lets go we can escape!!"
    print(good)
else:
    outcome = "Doom: NOOO, we're stuck."
    print(bad)
print(outcome)