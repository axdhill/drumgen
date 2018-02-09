import numpy as np
import os


l = 16
hh_dict = np.array([("r",0), ("hh",1)])
sn_dict = np.array([("r",0), ("sn",1)])
bd_dict = np.array([("r",0), ("bd",1)])
hhp_dict = np.array([("r",0), ("hhp",1)])

p_hh = 0.7
p_bd = 0.4
p_sn = 0.75
p_hhp = 0
hh_pts = np.random.choice([0,1],l,p=[1-p_hh,p_hh])
sn_pts = np.random.choice([0,1],l,p=[1-p_sn,p_sn])
bd_pts = np.random.choice([0,1],l,p=[1-p_bd,p_bd])
hhp_pts = np.random.choice([0,1],l,p=[1-p_hhp,p_hhp])



hh_list = [hh_dict[elem][0] for elem in hh_pts]
sn_list = [sn_dict[elem][0] for elem in sn_pts]
bd_list = [bd_dict[elem][0] for elem in bd_pts]
hhp_list = [hhp_dict[elem][0] for elem in hhp_pts]

print(hh_list)
print(sn_list)
print(bd_list)
print(hhp_list)

top_voice = ""
for i in range(l) :
    if((hh_pts[i] == 0) & (sn_pts[i] == 0)) :
        top_voice += 'r8 '
    if((hh_pts[i] == 1) & (sn_pts[i] == 0)) :
        top_voice += 'hh8 '
    if((hh_pts[i] == 0) & (sn_pts[i] == 1)) :
        top_voice += 'sn8'
        if(np.random.rand(1) < 0.2) :
            top_voice += "->"
        top_voice += " "

    if((hh_pts[i] == 1) & (sn_pts[i] == 1)) :
        top_voice += '<hh sn>8'
        if(np.random.rand(1) < 0.2) :
            top_voice += "->"
        top_voice += " "

print(top_voice)



bottom_voice = ""
for i in range(l) :
    if((bd_pts[i] == 0) & (hhp_pts[i] == 0)) :
        bottom_voice += 'r8 '
    if((bd_pts[i] == 1) & (hhp_pts[i] == 0)) :
        bottom_voice += 'bd8 '
    if((bd_pts[i] == 0) & (hhp_pts[i] == 1)) :
        bottom_voice += 'hhp8 '
    if((bd_pts[i] == 1) & (hhp_pts[i] == 1)) :
        bottom_voice += '<bd hhp>8 '


print(bottom_voice)


ly_file = open("temp.ly","w")
ly_file.write("\paper { \n #(set-paper-size \"a6\" 'landscape) \n}\n")
ly_file.write("up = \drummode {\n\t"+top_voice \
    +"\n}\ndown = \drummode {\n\t"+bottom_voice \
    +"\n}\n\\new DrumStaff <<\n   \\new DrumVoice { \\voiceOne \up } \n   \\new DrumVoice { \\voiceTwo \down }\n >>")
ly_file.write(" \layout {\n \context {\n\Score \n\t\override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/16) \n} \n}")
ly_file.close()

os.system("lilypond temp.ly")
os.system("open temp.pdf")
