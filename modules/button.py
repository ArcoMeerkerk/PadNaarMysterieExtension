def circleButton(self, cx, cy, radius) :
    self.fill(0)
    self.noStroke()
    self.ellipse(cx,cy, radius, radius)
    return pointCircle(self, cx, cy, radius)

def pointCircle(self, cx, cy, r) :
    distX = self.mouseX - cx
    distY = self.mouseY - cy
    distance = sqrt((distX*distX) + (distY*distY))

    if (distance <= r) and self.MouseReleased :
        return True
    return False