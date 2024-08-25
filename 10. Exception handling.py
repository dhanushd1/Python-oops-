try:
    a=int(input())
    b=int(input())
    
    
except valueError as e:
    print(e)
except Exception:
    print("something Wrong")
finally:
    print("Done")

