readme plz >~<

I am Emika, and I made this great thing. It's a random word generator running on Python. I use it from command line thing, I dunno, figure it out yourself.
you can use it, but if you share it, please like, credit me I guess?? also, don't sell it. thank you!!
also, if you have questions or requests, my thingy on Discord is 'everyoung_goddess_emika'



HOW DO YOU (OR I AT LEAST) ACTIVATE THIS PROGRAM
(this might be different because I use linux since a few days I guess, this was partly just me trying to get used to that)

have a file which has the phonology you want to generate words for saved in the same folder as this one (it can technically be somewhere else but ye)
open terminal
use the 'cd' command to go to the path where this program is stored
type 'python3 ./word-generator.py ./[name of that file] <number of words you want>
(the number of words is optional, if you don't put anything in, it makes one)





AN EXAMPLE SO YOU KNOW HOW TO USE THIS THING (you can copy paste and edit it into what you want, or just start from nothing)

# DOGY BONA EXAMPLE THING  <- this is a comment, the code ignores them
#                          only put comments on their own lines please!! don't put them after a line you actually use,
#                          and don't put a space before the hashtag because that *might* break your program depending
#                          on what's in your comment.

# this is the length of the word. The first number is the chance for the first syllable, the second is the chance for
# the second syllable, etc. The last syllable, which can be defined to act differently from the medial ones, is the
# one after the tilde. The value right before the tilde is a repeating chance that keeps trying to add a syllable, as
# long as it keeps succeeding the check. If you don't want this to be possible, to have a maximum of three syllables,
# for example, you could put in '100>20~90' instead. The chances are in percent.
100>20>5~90

# these are the forms syllables can have. The letters refer to the categories defined in the next section. 
# the numbers refer to the relative chances in different parts of the word. There are four ways to define chances,
# and they work in three sections. The first syllable can have a chance defined on its own, the last one as well,
# and all those in between use the same chances.

# the ways to define are as follows:
#            first | medial | last
# $a      ~    a   |   a    |  a
# $a-b    ~    a   |   b    |  b
# a-b$    ~    a   |   a    |  b
# $a-b-c$ ~    a   |   b    |  c

# so practically, this means that, in this case, syllables without onset can only appear word-initially,
# and syllables with a nasal coda are more likely to appear word-initially, and way more likely word-finally
# note that the 'last syllable' is the one after the '~' in the previous section.
# monosyllabic words which act as both word-initial *and* word-final are not supported.
V, $2-0
CV, $5
VN, $1-0
CVN, $2-1-3$


# these are the categories of phonemes. The name of a category should be one letter (might change this later).
C = p,t,k,m,n,s,l,j,w
V = a,e,i,o,u
N = n

# the chance for each phoneme to appear, relative to the rest. It is possible to put multigraphs here, if you want to :3
m,n: 3,4
p,t,k: 2,4,3
s,l: 3
j,w: 2

a,e,i,o,u: 4,3,2,3,2

# these combinations of letters are forbidden sequences. It filters them out. If you had the
# "it just kept trying to add a syllable and failing"-error, you probably have to look here.
!ti
!ji
!wo, wu
!nn, nm

# these are rewriting rules. Put either as many outputs as inputs, or only one output. If you put only one output, 
# everything will become that output. So, in this example, 'tokipona' > 'dogybona'. You can put in digraphs or
# trigraphs or whatever you want.
p,t,k,s > b,d,g,z
i,j > y




~E~m~i~k~a~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|++++++++++++++++++++++++++++++++++++++++=+++####################*++++#####%**%@#*%@@@##+*++++|
|+++++++++++++++++++++++++++++++++++++++==*##########################*+++###*%#+%@*#@%@%#**+++|
|+++++++++++++++++++++++++++++++++++++==*+###############%#**%##%%%###%%%#+%%@%+@+@%%%%%%##*++|
|++++++++++++++++++++++++++++++++++++-++*#############**#%%%###*%##%%%%%@@@@#%@@@#@#@#%%@%##*+|
|++++++++++++++++++++++++++++++++++=-+**#############%%%#++#%%%%@#%%*%@@@@@@@@%@@@@#@%@#%%%##*|
|+++++++++++++++++++++++++++++++++=-+++###############%%%%%#+#%%%@@%%#*#@@@%+%%@@@@@@@@@%@%%##|
|++++++++++++++++++++++++++++++++=-=+*###########***###%%%%#%%+#%@@@@@##*#@@@@@@@@@@@@%@@@@%@#|
|++++++++++++++++++++++++++++++++==+#########%%%%%%#+%%%%%%%%#+#+#@@@@%%%**@@@@@@@@@@@@@%@@@@@|
|+++++++++++++++++++++++++++++++=++*###########%%%@@@##@@@@@@%@%@%+%@@@@@@**%@@@@@@@@@@@@#@@@@|
|+++++++++++++++++++++++++++++++=++#########**###@%@@@@*@+@@@@@%@@@@%@@@@@@##%@@@@@@@@@@@@%@@@|
|++++++++++++++++++++++++++++++++############*+#%@@@@@@@#%=@@@@@@@%@@@%@@@@@%#@@@@@@@@@@@@@@%@|
|++++++++++++++++++++++++++++++#%@@%%#+**##@##+#+*%@@@@@@%@@@@@@@@@@@@@%@@@@@%%@@@@@@@@@@@@@@#|
|++++++++++++++=-=*=+++++++++#%%#%%##@@##*@@%@##**+%@@@@@@%@@@@@@@@@@@@%@@@@@@#@@@@@@@@@@@@@@@|
|+++++++++++++=---+#+++++%##%##%##%#%*%@%#@@%%==%*#+*@@@@@@@@@@@@@@@@@@@%@@@@@@#@@@@@@@@@@@@@@|
|+++++++++++++-----#%++#@%#%#%##%#%#%###@@@@%#====%##+%@@@@%@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@|
|++++++++++=--------@@@@%#%#%#%%%%#%#%##+@@@@+=--===#*+*%@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++=---------@@@%%#%%%%%%%%%%%%%%%=@@@%=---=-==++++#%%##@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@|
|+++++++++=---------%@%%%%%%%%%%%%%%%%%%%%#@@@%=-------=+*+++%##@@@@%@@@@%%@@@@@@@@@@@@@@@@@@@|
|+++++++++=---------%@%%%%%%%%%%%%%%%%%%%%%#@@%%=----=+####%++%**@@%%@@@@%%@@@@@@@@@@@@@@@@@@@|
|++++++++++---------%%%%%%%%%%%%%%%%%%%%%%%%#@@#%+-=*=-===+++@+@+*@%%@@@@@%@@@@@@@@@@@@@@@@@@@|
|+++++++++*---------@%%%%%%%%%%%%%%%%%%%%%%%#%@%*#----=####%@@%%%*#@@@@@@@%@@@@@@@@@@@@@@@@@@@|
|++++++++@%--------=@%%%%%%%%%%%%%%%%%%%%%%%%%@@%#=-=-=#%%@@@@@@@@*@@@@@@@%@@@@@@+=%@@@@@@@@@@|
|++++++#@@%--------=@%%%%%%%%%%%%%%%%%%%%%%%%%@@%%#==-=#%%@@@@@@*@%%@@#%%@@@@@@@@@%=@@@@@@@@@@|
|++++++@@@#-------==@%%%%%%%%%%%%%%%%%%%%%%%%%%@%%=+======#%@%%%+=##%#*##%@@@@@@@%%+@@@@@@@@@@|
|+++++@@@++------===@%%%%%%%%%%%%%%%%%%%%%%%%#%@@%=========+++%+==++%+*##@@@@@@@%@%+@@@@@@@@@@|
|+++#@@@++++-@@@@@==@%%%%%%%---------%%%%%%%##%@%%=-===============+*+%#%@@@@@@%%%#@@@@@@@@@@@|
|+=%@@@+++++=@%%%%*=@%%%%%%%%%%%-----%%%%%%%%#%@%%==================+%@#@@@@@@%%%@@@@@@@@@@@@@|
|=%@@@++++++===-==-=%%%%%%%%%%%%%%%%%%%%%%%%##@@%%=-===============++%#@@@@@@%%@@@@@@@@@@@@@@@|
|#@@%+++++++=-=--==+%%%%%%%%%%%%%%%%%%%%%%%%%*@@%%==================%%@@@@@@@@@@@@@@@@@@@@@@@@|
|@%%++++++++==-=-==+%%%%%%%%%%%%%%%%%%%%%%%%%*@@%%=================%*@@@@@@@@@@@@@@@@@@@@@@@@@|
|%@+++++++++==-===#*@%%%%%%%%%%%%%%%%%%%%%%%%%@%%#===============+%#@@@@@%@%@@@@@@@@@@@@@@@@@@|
|%+++++++++++=--==+#@%%%%%%%%%%%%%%%%%%%%%%%#@%@*#==============%+%@@@@@%%%@@@@@@@@@@@@@@@@@@@|
|#+++++++++++++==-+%@%%%%%%%%%%%%%%%%%%%%%%%@@@@@%====----====*##@@@@@@%%%%@@@@@@@@@@@@@@@@@@@|
|++++++++++++=-+--%@@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@%=========+#%@@@@@@%%@@%@@@@@@@@@@@@@@@@@@@|
|++++++++++++--=-#@%@@%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@+=====+#*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++=-+--#%%@@%%%%%%%%%%%%%%%%%%%%@%@@@@@@@%@@%-=+=**%@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++=-#--+#%%@@%%%%%%%%%%%%%%%%%%@@@@@@++%@@@@@%#@+#@@@#@#@@@%##@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++--#--=#%%+@@%%%%%%%%%%%%%%%%=#%@@@@%++++%@*@#*#@@@@@#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++--+---%#+++@@%%%%%%%%%%%%%*=+++@@%%%#*+*%#%**#@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++--+--++-=-*%%@%%%%%%%%%#*=*++++@@@++##@###%+%@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++--=-==--##=-=-%%%%%#+#+=**+++++%#@*+%%#%#%*%@@@@#@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@|
|*+++++++++#%------=-----%@@##%=-++++++++++*%##+*%%#%#%@@@#@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@|
|#*+++++++#%%+--------=-=@%#=-++++++++++++*=###+*##%+%@@@+@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@|
|+########%%%#----=-=-=-+%%*++++++++++++++*#+*##*#@=*%@@+@@@@@@@%%@%%%%@@@@@@@@@@@@@@@@@@@@@@@|
|+*#%%%%%%%%%+=--------=-=%#*+++++++++++++*%#%###@#=#@%#@@@%@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@|
|++++++++++++++=--------=-=%#*+++++++++--+#%%#=@%%++##@+@@@@#@#%%%%%@@@@@%@@@@@@@@@@@@@@@@@@@@|
|+++++++++++++++=---=-=----#%#++++++++=%=-=-+=@@@@++#%%#@@@@#%%%%%%@@@%%%@@@@@@@@@@@@@@@@@@@@@|
|++++++++++++++++=----=----*%##+*++++++%=+--+%@@@@%+*#@%*#*%@%%%%@@%%%%%@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++++++=-+%------*%%@@#*++++++%=+==#@@@@@@%*=%@@@@@@#%%@%%%%%+@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++++++=--*%%@#+#@@@%%%#++++++%%%=#@%%@@@@@@=+#@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@|
|+++++++++++++++=---===#%%%@%%%#++++++++%@%@@%%@@@@@@@@+--*#+**%%%%%%*@@@@@@@@@@@@@@@@@@@@@@@@|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~14~06~2024~
