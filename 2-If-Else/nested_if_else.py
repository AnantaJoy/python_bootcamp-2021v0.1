ielts = 5.5 

if ielts>=7 and ielts<=9:
    if ielts>=7 and ielts < 8:
        print("Self Funded")
        
    elif ielts>=8 and ielts <=9:  
        print("Full Funded")
        
elif ielts>=5 and ielts < 7:
    print("Waiting List")
    
elif ielts<5:
    print("Rejected")
    