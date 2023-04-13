with open('C:\\Users\\armando.fontainhas\\OneDrive - ccg.pt\\Learn Code\\Python\\PyNative\\sample.txt' , 'r')as file:
    data = file.read().replace('\n', " ")
    print (data)