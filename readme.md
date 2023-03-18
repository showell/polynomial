### Overview ###

The "polynomial" library allows you to create polynomials using
natural **Python** syntax. It performs **symbolic manipulation** when
you combine polynomials with each other or with constants. It assumes
simple **non-negative integer exponents**.  You can configure the
class to work with **abstract Math** types, but it also works with
integers and fractions out of the box. It allows **multiple variables**.

Example usage:

<pre>
x = Poly.var("x")
y = Poly.var("y")

p = (x + y) ** 6
# str(p) == "(x**6)+6*(x**5)*y+15*(x**4)*(y**2)+20*(x**3)*(y**3)+15*(x**2)*(y**4)+6*x*(y**5)+(y**6)"

h = Poly.var("height")
w = Poly.var("width")
a = w * h
assert_str(a, "height*width")
assert_equal(a.eval(width=10, height=5), 50)

</pre>
