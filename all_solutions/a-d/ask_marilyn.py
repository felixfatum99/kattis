letter_to_number = {"A":0, "B":1, "C":2}
number_to_letter = {0:"A", 1:"B", 2:"C"}
for i in range(1000):
    boxes = "ABC"
    box_chosen = number_to_letter[i%3]
    print(box_chosen)
    box, value = input() .split()
    if value == "1":
        print(box)
    else: 
        boxes = boxes.replace(box_chosen, "")
        if box == box_chosen:
            if i % 2 == 0:
                print(boxes[0])
            else:
                print(boxes[1])
        else:
            boxes = boxes.replace(box, "")
            print(boxes)
           
    val, answer = input().split()