def setup():
    global maxThickness
    size(1000,600)
    strokeWeight(10)
    background(255)
    maxThickness=15

def draw():
   return

def mousePressed():
    global lastX,lastY,vx,vy,lastThickness 
    lastX=mouseX
    lastY=mouseY
    vx=0
    vy=0
    lastThickness=1
   
def mouseDragged():
    global lastX,lastY,vx,vy,lastThickness
    vx=0.7*vx+0.3*(mouseX-lastX)
    vy=0.7*vy+0.3*(mouseY-lastY)
    v=sqrt(vx*vx+vy*vy)

    nextThickness=maxThickness-v
    if nextThickness <0:
       nextThickness =0
    nextThickness=0.5* nextThickness+0.5*lastThickness
 
    n=10+int(v/2)
    for i in range(1,n+1):
        x1=map(i-1,0,n,lastX,mouseX)
        y1=map(i-1,0,n,lastY,mouseY)
        x2=map(i,0,n,lastX,mouseX)
        y2=map(i,0,n,lastY,mouseY)
        offset =2
        thickness=map(i-1,0,n, lastThickness,nextThickness)
        strokeWeight(thickness+offset)
        line(x1,y1,x2,y2)
        strokeWeight(thickness)
        line(x1+offset*2,y1+offset*2,x2+offset*2,y2+offset*2)
        line(x1-offset,y1-offset, x2-offset,y2-offset)


        lastX=mouseX 
        lastY=mouseY
        lastThickness=nextThickness
   
def keyPressed():
    background(255)
