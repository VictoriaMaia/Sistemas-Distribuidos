from classUser import User

if __name__ == "__main__":
    user = User()
    print ("soma op1 op2\nsub op1 op2\nmult op1 op2\ndiv op1 op2\nsair\n")
    while True:
        if user.readRequest() == 1:
            user.sair()
            break
        user.writeAnswer()
        