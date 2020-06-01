#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
import numpy as np
text1='パトカー'
text2='タクシー'

out=np.zeros(0)
for i in range(4):
    out=np.append(out,text1[i])
    out=np.append(out,text2[i])
print(out)
ans = ''
for i in range(len(text1)):
    ans += text1[i]
    ans += text2[i]
print(ans)

