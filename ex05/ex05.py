name = 'Kangwon Lee'
age = 25  # a lie
height_cm = 184.5
cm_to_inch = 1.0 / 2.54
height_inch = height_cm * cm_to_inch
weight_kg = 80
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %g cm tall." % height_cm
print "He's %g inches tall." % height_inch
print "He's %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
