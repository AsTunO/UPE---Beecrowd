A = float(input())
B = float(input())
C = float(input())
if( A not in range(0,11) or B not in range(0,11) or C not in range(0,11)):
    print()
else:
    MEDIA = ((A.__round__(1) * 2) + (B.__round__(1) * 3) + (C.__round__(1) * 5)) / 10
    print("MEDIA = %.1f" % MEDIA)
    
