# Design

<h2> Class Structure </h2>

In order to have an easy to maintain and expand code, most "endpoint" classes inherit from one abstract template class. But for performance and maintainability reasons, complecated inheritance stractures are avoided.

Note: The datastructures classes are preaty elementary for this tool and resonable expantions of it. If this changes in future iterations a more comprehensive inheritance structure might be optimal to avoid repetitive code.

<h2> Main Algorithm </h2>

From the specification Document it seems that both the main data and the samples are changed daily. This means that saving the data in a database or another datastructure would mean a non-negligible performance hit. 

So the decision is to save only data necessary to produce the outputfiles. Also everything is printed as it is found. This is likly to be faster than saving in a list and printing in bulck at the end. This assumption might not be true so benchmarking might be a good idea.

Note: In case sampling on customers has kept the relative order, or other fields (of foreign keys) are sorted, there is a faster implementation that avoids dictionaries. The difference though is likly to be negligible due to the small size of the dicts.

<h2> Format In Dictionaries </h2>

When saving data in a dictionary, the "primary key" is used as key, and the hole object as value. This is suboptimal in terms of performans because there are parts of data saved twice. That being said, this way helps alote with the readablity of the code and the simplicity of the classes so it is preferable.

Specificly, Customer_Samples could have been saved in a set because they have only one value. This way again is preferable because it is more modular and it is resiliant in the case more fields are added.

<h2> Automated Testing of Tool </h2>

Automated Testing was done in an as-you-go basis. It is defenetly both slower and worse for expanding and maintaining. This is less important because accept from the Utilities which are well writen, tests will be added with functionality. 

That being said if I had to do the project again more thought would have gone in struucturing the testing.