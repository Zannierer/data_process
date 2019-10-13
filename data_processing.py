def config():
    '''
    return a set of 3 elements: const, variable, time
    
    '''
    pass
    counter = 0 #displaying position of about-to-be-input var or const
    
    #enquire constant in the equation
    const = {} #dictionary storing const
    while True:
        symbol = input("Constant symbol num.%d ('done' = stop input): "%(counter))#symbol input
        if symbol == "done":
            counter = 0
            break
        value = input("Value of %s: "%(symbol))#value input
        if value == "done":
            counter = 0
            break
        else:
            const[symbol] = value
            counter += 1

    #enquire variable in the equation
    variable = [] #empty array for storing var
    while True:
        grab = input("Measured variable num.%d (type 'done' if complete): "%(counter))
        if grab == "done":
            counter = 0
            break
        else:
            variable += grab
            counter += 1

    #enquire number of trials of variable
    time = int(input("Enter number of trial: "))
    #for (a,b) in const.items():
    #    print("{}: {}".format(a,b))
    #print(variable)
    #print(time)
    return [const,
            variable,
            time,]
               
def display_config():
    pass
    for (a,b) in const.items():
        print("{}: {}".format(a,b))
    print(variable)
    print(time)
    

def equation():
    pass
    display_config()

def main():
    pass
    config()
    display_config()#display all entered information prior to data input
    
    #dict[var] = array of values

if __name__ == "__main__":
    main()
