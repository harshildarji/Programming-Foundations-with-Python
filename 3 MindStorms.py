import turtle

def tri(tName, color, length):
    tName.color(color)
    tName.speed(50)
    for i in range(36):
        for count in range(3):
            tName.forward(length)
            tName.right(120)
        tName.left(10)
        
def main():
    window = turtle.Screen()
    window.bgcolor('#012456')
    brad = turtle.Turtle()
    
    tri(brad, 'pink', 100)
    tri(brad, '#a6a6a6', 50)
    tri(brad, 'yellow', 75)
    
    brad.right(90)
    brad.forward(200)
    window.exitonclick()
    
if __name__ == '__main__':
    main()
