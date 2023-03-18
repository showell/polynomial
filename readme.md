### Overview ###

The "polynomial" library allows you to create polynomials using
natural **Python** syntax. It performs **symbolic manipulation** when
you combine polynomials with each other or with constants. It assumes
simple **non-negative integer exponents**.  You can configure the
class to work with **abstract Math** types, but it also works with
integers and fractions out of the box. It allows **multiple variables**.

You can perform **substitution** and **composition** on the polynomials,
and the library automatically simplifies them at the symbolic level.
Of course, you can also **evaluate polynomials** with actual values
such as **integers** or **fractions**.

The software is **completely free** (i.e public domain)  and is mostly intended for **academic** use cases.

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

### Limitations ###

If you are evaluating several polynomial libraries, let me tell you what this library is **NOT** intended for:

* **serious number crunching** - For small polynomials, the library will work perfectly well, but the calculations run as vanilla interpreted Python (i.e. no C extensions), and there aren't any fancy algebra tricks under the hood.

* **general math** -- This only computes polynomials.  I do think you can make the library play nice with any reasonable general-math library.

* **infinite polynomials** -- Our polynomials are just a finite list of terms.

* **negative exponentation** -- We adhere to the strict definition of a polynomial as described in https://en.wikipedia.org/wiki/Polynomial

* **non-integer exponents** -- (same as above)

* **easy installation** -- I haven't packaged this library yet.  (As you can see, it is small enough to easily subsume into your own project, if that works.)

* **active developer community** -- This is a one-person project, and I don't intend any long-term support for the library.  I believe it to be fairly complete and bug-free. (If you do contact me, I will certainly try to be as helpful as I can insofar as I have bandwidth.)

If none of the limitations are deal-breakers, then please read on!


